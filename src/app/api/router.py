from fastapi import APIRouter
from api.article.routes import router as article_router
from api.comments.routers import router as comment_router


router = APIRouter(prefix='/api')
router.include_router(article_router)
router.include_router(comment_router)

@router.get('/articles/{id_}')
def get_article(id_: int):
    return {'id': id_, 'name': 'Test Article'}