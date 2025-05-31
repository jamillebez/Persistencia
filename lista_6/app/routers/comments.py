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

comment_router = SQLAlchemyCRUDRouter(
    schema=CommentSchema,
    create_schema=CommentCreateSchema,
    db_model=Comment,
    db=get_db,
    prefix="comments"
)