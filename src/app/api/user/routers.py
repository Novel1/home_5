import fastapi as fa
from db.repository import UserRepository


router_user = fa.APIRouter(prefix='/user')
repo = UserRepository