import pydantic
from uuid import UUID
from typing import Optional 


class ArticleShema(pydantic.BaseModel):
    name: str
    description: str
    category: str
    
    
class ArticleGetShema(pydantic.BaseModel):
    id: UUID | None = pydantic.Field(None)
    name: str | None = pydantic.Field(None)
    description: str | None = pydantic.Field(None)
    category: str
    
    
class ArticleUpdateSchema(pydantic.BaseModel):  
    name: str | None = pydantic.Field(None)
    description: str | None = pydantic.Field(None)
    category: str