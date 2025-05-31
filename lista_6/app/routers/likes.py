from fastapi import Query, Depends
from sqlalchemy.orm import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.models import Like
from app.schemas import LikeSchema, LikeCreateSchema
from app.database import get_db

class LikeRouter(SQLAlchemyCRUDRouter):
    def list(self, skip: int = Query(0, ge=0), limit: int = Query(10, gt=0, le=100), db: Session = Depends(get_db)):
        return db.query(self.db_model).offset(skip).limit(limit).all()

like_router = LikeRouter(
    schema=LikeSchema,
    create_schema=LikeCreateSchema,
    db_model=Like,
    db=get_db,
    prefix="likes",
)
