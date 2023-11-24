import fastapi as fa
from api.shemas import CommentGetShema, CommentUpdateSchema
from db.repository import CommentRepository
from exceptions import common as common_exc, http as http_exc
from uuid import UUID
from api import shemas
from starlette import status


router = fa.APIRouter(prefix='/article/comment')
repo = CommentRepository()



@router.get('')
async def get_articles(query: shemas.CommentGetShema = fa.Depends()):
    return await repo.get_list(**query.model_dump(exclude_none=True))


@router.get('/{id}')
async def get_comments(id: UUID):
    try:
        return await repo.get(id)
    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))
    
    
@router.post('/{article_id}')
async def create_comment(article_id: UUID,body: shemas.CommentShema):
    try:
        return await repo.create(article_id=article_id, **body.model_dump())
    
    except common_exc.CreateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    
@router.delete('/{id}')
async def delete_comment(id: UUID):
    try:
        await repo.delete(id)
        return fa.responses.Response(status_code=status.HTTP_204_NO_CONTENT)
    except common_exc.DeleteException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))