from uuid import UUID
import pydantic

class CommentShema(pydantic.BaseModel):
    description: str
    article_id: UUID | None = pydantic.Field(None)
    
    
class CommentGetShema(pydantic.BaseModel):
    id: UUID | None = pydantic.Field(None)
    description: str | None = pydantic.Field(None)
    
    
class CommentUpdateSchema(pydantic.BaseModel):  
    description: str | None = pydantic.Field(None)
    article_id: UUID