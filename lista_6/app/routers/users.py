from fastapi import Query, Depends
from sqlalchemy.orm import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.models import User
from app.schemas import UserSchema, UserCreateSchema
from app.database import get_db

class UserRouter(SQLAlchemyCRUDRouter):
    def list(self, skip: int = Query(0, ge=0), limit: int = Query(10, gt=0, le=100), db: Session = Depends(get_db)):
        return db.query(self.db_model).offset(skip).limit(limit).all()

user_router = UserRouter(
    schema=UserSchema,
    create_schema=UserCreateSchema,
    db_model=User,
    db=get_db,
    prefix="users",
)
