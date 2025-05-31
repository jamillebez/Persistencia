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

user_router = SQLAlchemyCRUDRouter(
    schema=UserSchema,
    create_schema=UserCreateSchema,
    db_model=User,
    db=get_db,
    prefix="users"
)