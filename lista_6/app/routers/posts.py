from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.models import User, Post, Comment, Category, Like
from app.schemas import (
    UserSchema, UserCreateSchema,
    PostSchema, PostCreateSchema,
    CommentSchema, CommentCreateSchema,
    CategorySchema, CategoryCreateSchema,
    LikeSchema, LikeCreateSchema
)
from app.database import get_db

post_router = SQLAlchemyCRUDRouter(
    schema=PostSchema,
    create_schema=PostCreateSchema,
    db_model=Post,
    db=get_db,
    prefix="posts"
)

