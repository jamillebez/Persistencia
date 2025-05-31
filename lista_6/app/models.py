from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

# Associação Post <-> Categoria (N:N)
post_category = Table(
    'post_category',
    Base.metadata,
    Column('post_id', ForeignKey('posts.id'), primary_key=True),
    Column('category_id', ForeignKey('categories.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    posts = relationship('Post', back_populates='author', cascade="all, delete")
    comments = relationship('Comment', back_populates='user', cascade="all, delete")
    likes = relationship('Like', back_populates='user', cascade="all, delete")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    author = relationship('User', back_populates='posts')

    comments = relationship('Comment', back_populates='post', cascade="all, delete")
    likes = relationship('Like', back_populates='post', cascade="all, delete")
    categories = relationship('Category', secondary=post_category, back_populates='posts')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    posts = relationship('Post', secondary=post_category, back_populates='categories')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)

    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)

    user = relationship('User', back_populates='likes')
    post = relationship('Post', back_populates='likes')