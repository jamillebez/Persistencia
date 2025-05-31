from pydantic import BaseModel
from typing import List, Optional

class UserCreateSchema(BaseModel):
    username: str
    email: str

class UserSchema(UserCreateSchema):
    id: int
    class Config:
        orm_mode = True

class CategoryCreateSchema(BaseModel):
    name: str

class CategorySchema(CategoryCreateSchema):
    id: int
    class Config:
        orm_mode = True

class PostCreateSchema(BaseModel):
    title: str
    content: str
    author_id: int
    category: List[int] = []

class PostSchema(PostCreateSchema):
    id: int
    class Config:
        orm_mode = True

class CommentCreateSchema(BaseModel):
    content: str
    post_id: int
    user_id: int

class CommentSchema(CommentCreateSchema):
    id: int
    class Config:
        orm_mode = True

class LikeCreateSchema(BaseModel):
    user_id: int
    post_id: int

class LikeSchema(LikeCreateSchema):
    id: int
    class Config:
        orm_mode = True
