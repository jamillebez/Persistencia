from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, or_
from typing import List

from app.database import get_db
from app.models import Post, Category, Comment
from app.schemas import PostSchema, PostWithCommentCountSchema, CategoryWithPostCountSchema

router = APIRouter(tags=["Customized"])

# 1) Posts mais comentados, ordenados, paginados
@router.get("/posts/most_commented", response_model=List[PostWithCommentCountSchema])
def get_most_commented_posts(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0, le=100),
    db: Session = Depends(get_db),
):
    posts = (
        db.query(Post, func.count(Comment.id).label("comment_count"))
        .join(Comment, Comment.post_id == Post.id, isouter=True)
        .group_by(Post.id)
        .order_by(func.count(Comment.id).desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    
    result = []
    for post, count in posts:
        # Cria o schema manualmente, passando todos os campos esperados
        post_data = PostWithCommentCountSchema(
            id=post.id,
            title=post.title,
            content=post.content,
            author_id=post.author_id,
            categories=[CategorySchema.from_orm(cat) for cat in post.categories],
            comment_count=count
        )
        result.append(post_data)
    return result

# 2) Categorias com contagem de posts, ordenadas da maior para a menor
@router.get("/categories/with_post_counts", response_model=List[CategoryWithPostCountSchema])
def get_categories_with_post_counts(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0, le=100),
    db: Session = Depends(get_db),
):
    categories = (
        db.query(Category, func.count(Post.id).label("post_count"))
        .join(Category.posts)
        .group_by(Category.id)
        .order_by(func.count(Post.id).desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    result = []
    for cat, count in categories:
        result.append(CategoryWithPostCountSchema(
            category=cat,
            post_count=count
        ))
    return result

# 3) Buscar posts por palavra-chave no título ou conteúdo
@router.get("/posts/search", response_model=List[PostSchema])
def search_posts(
    query: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0, le=100),
    db: Session = Depends(get_db),
):
    posts = (
        db.query(Post)
        .filter(
            or_(
                Post.title.ilike(f"%{query}%"),
                Post.content.ilike(f"%{query}%")
            )
        )
        .offset(skip)
        .limit(limit)
        .all()
    )
    return posts

# 4) Filtrar posts por categoria(s)
@router.get("/posts/by_category", response_model=List[PostSchema])
def get_posts_by_category(
    category_ids: List[int] = Query(...),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0, le=100),
    db: Session = Depends(get_db),
):
    posts = (
        db.query(Post)
        .join(Post.categories)
        .filter(Category.id.in_(category_ids))
        .offset(skip)
        .limit(limit)
        .all()
    )
    return posts
