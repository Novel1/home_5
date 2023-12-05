from fastapi import APIRouter
from api.article.routes import router as article_router
from api.comments.routers import router_comment as comment_router
from api.user.routers import router_user as user_router
import json
import jwt
from base64 import b64encode
import hashlib


router = APIRouter(prefix='/api')
# router.include_router(article_router)
# router.include_router(comment_router)
# router.include_router(user_router)


# header = {
#     'alg': 'HS256',
#     'typ': 'JWT',
# }

# payload = {
#      'sub': 1,
#      'birth_date': '17.09.1990',
#      'exp': '05.12.2023 23:59',
# }


# SECRET_KEY = 'some_secret_key'

# unsigned_token = b64encode(json.dumps(header).encode('utf-8')).decode('utf-8') + '.' + b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8')

# encoded_jwt = hashlib.sha256(payload, SECRET_KEY, algorithm='HS256')
# print(b64encode(encoded_jwt))

