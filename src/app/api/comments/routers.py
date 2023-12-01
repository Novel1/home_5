import fastapi as fa
from db.repository import CommentRepository
from exceptions import common as common_exc, http as http_exc
from uuid import UUID
from api import shema_comment
from starlette import status


router_comment = fa.APIRouter(prefix='/article/comment')
repo = CommentRepository()



@router_comment.get('')
async def get_comments(query: shema_comment.CommentGetShema = fa.Depends()):
    return await repo.get_list(**query.model_dump(exclude_none=True))


@router_comment.get('/{id}')
async def get_comment(id: UUID):
    try:
        return await repo.get(id)
    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))
    
    
@router_comment.post('')
async def create_comment(body: shema_comment.CommentShema):
    try:
        return await repo.create(**body.model_dump())
    
    except common_exc.CreateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    
@router_comment.delete('/{id}')
async def delete_comment(id: UUID):
    try:
        await repo.delete(id)
        return fa.responses.Response(status_code=status.HTTP_204_NO_CONTENT)
    except common_exc.DeleteException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    except common_exc.NotFoundException as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))