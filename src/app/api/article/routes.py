import fastapi as fa
from api.shemas import ArticleGetShema, ArticleShema, ArticleUpdateSchema
from db.repository import ArticleRepository
from exceptions import common as common_exc, http as http_exc
from uuid import UUID
from api import shemas
from starlette import status


router = fa.APIRouter(prefix='/article')
repo = ArticleRepository()


@router.get('')
async def get_articles(query: shemas.ArticleGetShema = fa.Depends()):
    return await repo.get_list(**query.model_dump(exclude_none=True))


@router.get('/{id}')
async def get_articles(id: UUID):
    try:
        return await repo.get(id)
    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))


@router.post('')
async def create_article(body: shemas.ArticleShema):
    try:
        return await repo.create(**body.model_dump())
    
    except common_exc.CreateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    
@router.patch('/{id}')
async def upadate_article(id: UUID, body: shemas.ArticleUpdateSchema):
    try:
        return await repo.update(id, **body.model_dump(exclude_none=True))
    except common_exc.CreateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))
    
@router.delete('/{id}')
async def delete_article(id: UUID):
    try:
        await repo.delete(id)
        return fa.responses.Response(status_code=status.HTTP_204_NO_CONTENT)
    except common_exc.DeleteException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))