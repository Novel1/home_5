import pydantic
from uuid import UUID
from typing import Optional 


class ArticleShema(pydantic.BaseModel):
    name: str
    description: str
    author_id: int
    
    
class ArticleGetShema(pydantic.BaseModel):
    id: UUID | None = pydantic.Field(None)
    name: str | None = pydantic.Field(None)
    description: str | None = pydantic.Field(None)
    
    
class ArticleUpdateSchema(pydantic.BaseModel):  
    name: str | None = pydantic.Field(None)
    description: str | None = pydantic.Field(None)


class CommentShema(pydantic.BaseModel):
    description: str
    
    
class CommentGetShema(pydantic.BaseModel):
    id: UUID | None = pydantic.Field(None)
    description: str | None = pydantic.Field(None)
    
    
class CommentUpdateSchema(pydantic.BaseModel):  
    name: str | None = pydantic.Field(None)
    description: str | None = pydantic.Field(None)