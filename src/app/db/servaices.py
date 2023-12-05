from passlib.context import CryptContext
from datetime import datetime, timedelta

import fastapi as fa
import fastapi.security as fs
from jose import jwt, JWTError

from passlib.context import CryptContext
from pydantic import BaseModel

SECRET_KEY = '$2a$12$NdIA2k9tJIiOTYFKAjRHyOAtS50hrswIpPV62eteEs3DGE2LeQ2x6'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_db = {
    'johndoe': {
        'username': 'johndoe',
        'password': '$2a$12$T96vNdTLAmNlfAX4FNnG1.OSLvPuHlHj3RJ1bDcWlzeEbfHMAOGzi'
    },
}

class Token(BaseModel):
    token: str
    
class User(BaseModel):
    username: str
    password: str
    

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_shema = fs.OAuth2PasswordBearer(tokenUrl='/api/token')

app = fa.FastAPI()

def verity_password(plain_pass: str, hash_pass: str) -> bool:
    return pwd_context.verify(plain_pass, hash_pass)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def get_user(username: str) -> dict:
    if username in fake_db:
        return User(**fake_db[username])

def authenticate_user(username: str, password: str) -> dict:
    user = fake_db.get(username)

    if user is None:
        return None, False

    if not verity_password(password, user['password']):
        return user, False

    return user, True

    
def create_access_token(data: dict, expire_delta: timedelta | None = None):
    payload = data.copy()
    
    if expire_delta:
        expire = datetime.now() + expire_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
    payload.update({'exp': expire})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = fa.Depends(oauth2_shema)):
    creds_exception = fa.HTTPException(
        status_code=fa.status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={'WWW-Authenticate': 'Bearer'}
    )
    
    try: 
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = decoded_token.get('sub')

        if username is None:
            raise creds_exception
    
    except JWTError:
        raise creds_exception
    
    user = get_user(username)
    
    if user is None:
        raise creds_exception
    
    return user
