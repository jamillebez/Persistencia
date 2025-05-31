from fastapi import Query, Depends
from sqlalchemy.orm import Session
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.models import Category
from app.schemas import CategorySchema, CategoryCreateSchema
from app.database import get_db

class CategoryRouter(SQLAlchemyCRUDRouter):
    def list(self, skip: int = Query(0, ge=0), limit: int = Query(10, gt=0, le=100), db: Session = Depends(get_db)):
        return db.query(self.db_model).offset(skip).limit(limit).all()

category_router = CategoryRouter(
    schema=CategorySchema,
    create_schema=CategoryCreateSchema,
    db_model=Category,
    db=get_db,
    prefix="categories",
)
