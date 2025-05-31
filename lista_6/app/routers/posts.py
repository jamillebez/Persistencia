from fastapi_crudrouter import SQLAlchemyCRUDRouter
from fastapi import HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.models import Post, Category
from app.schemas import PostSchema, PostCreateSchema
from app.database import get_db

class PostRouter(SQLAlchemyCRUDRouter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create(self, obj_in: PostCreateSchema, db: Session = Depends(get_db)):
        # Buscar categorias pelo ID
        categories = db.query(Category).filter(Category.id.in_(obj_in.categories)).all()
        if len(categories) != len(obj_in.categories):
            raise HTTPException(status_code=400, detail="Uma ou mais categorias não foram encontradas")

        # Criar o post e associar as categorias
        db_post = Post(
            title=obj_in.title,
            content=obj_in.content,
            author_id=obj_in.author_id,
            categories=categories
        )
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post

    def list(
        self,
        skip: int = Query(0, ge=0),
        limit: int = Query(10, gt=0, le=100),
        db: Session = Depends(get_db)
    ):
        return db.query(self.db_model).offset(skip).limit(limit).all()

post_router = PostRouter(
    schema=PostSchema,
    create_schema=PostCreateSchema,
    db_model=Post,
    db=get_db,
    prefix="posts",
)
