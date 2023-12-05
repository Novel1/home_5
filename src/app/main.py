import fastapi
import pydantic
from fastapi.security import OAuth2PasswordRequestForm

from tortoise.contrib.fastapi import register_tortoise
import db.servaices as services

from api.router import router
from db.conf import TORTOISE_ORM
from exceptions import handlers as exc_handlers, http as http_exc


def setup():
    app = fastapi.FastAPI()
    app.include_router(router)
    
    register_tortoise(
        app=app, config=TORTOISE_ORM, generate_schemas=True, add_exception_handlers=True,
    )
    
    app.exception_handler(pydantic.ValidationError)(exc_handlers.query_params_exc_handler)
    app.exception_handler(http_exc.BaseHTTPException)(exc_handlers.request_exc_handler)
    app.exception_handler(500)(exc_handlers.internal_exc_handler)
    
    return app


app = setup()


@app.post('/api/token')
async def login(form_data: OAuth2PasswordRequestForm = fastapi.Depends()):
    user = services.authenticate_user(form_data.username, form_data.password)
    
    if not user:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    
    access_token = services.create_access_token({'sup': user['username']})
    return {'access_token': access_token}

@app.get('/api/user/me')
async def get_current_user(current_user: services.User = fastapi.Depends(services.get_current_user),
                           ):
    return current_user

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)