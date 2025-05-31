from fastapi import Query, Depends
from sqlalchemy.orm import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.models import Comment
from app.schemas import CommentSchema, CommentCreateSchema
from app.database import get_db

class CommentRouter(SQLAlchemyCRUDRouter):
    def list(self, skip: int = Query(0, ge=0), limit: int = Query(10, gt=0, le=100), db: Session = Depends(get_db)):
        return db.query(self.db_model).offset(skip).limit(limit).all()

comment_router = CommentRouter(
    schema=CommentSchema,
    create_schema=CommentCreateSchema,
    db_model=Comment,
    db=get_db,
    prefix="comments",
)
