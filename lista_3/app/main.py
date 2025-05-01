from fastapi import FastAPI
from .routes import livros

app = FastAPI()
app.include_router(livros.router)
