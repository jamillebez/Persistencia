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

like_router = SQLAlchemyCRUDRouter(
    schema=LikeSchema,
    create_schema=LikeCreateSchema,
    db_model=Like,
    db=get_db,
    prefix="likes"
)
