from fastapi import FastAPI
from typing import List
from .models import Livro
from . import crud

app = FastAPI()

@app.post("/livros", response_model=Livro)
def criar_livro(livro: Livro):
    return crud.criar_livro(livro)

@app.get("/livros", response_model=List[Livro])
def listar_livros():
    return crud.listar_livros()

@app.get("/livros/{id}", response_model=Livro)
def buscar_livro(id: int):
    return crud.buscar_livro(id)

@app.put("/livros/{id}", response_model=Livro)
def atualizar_livro(id: int, livro_atualizado: Livro):
    return crud.atualizar_livro(id, livro_atualizado)

@app.delete("/livros/{id}")
def deletar_livro(id: int):
    return crud.deletar_livro(id)
