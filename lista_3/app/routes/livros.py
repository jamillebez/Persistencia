from fastapi import APIRouter
from typing import List
from ..models import Livro
from .. import crud

router = APIRouter(prefix="/livros", tags=["Livros"])

@router.post("", response_model=Livro)
def criar_livro(livro: Livro):
    return crud.criar_livro(livro)

@router.get("", response_model=List[Livro])
def listar_livros():
    return crud.listar_livros()

@router.get("/{id}", response_model=Livro)
def buscar_livro(id: int):
    return crud.buscar_livro(id)

@router.put("/{id}", response_model=Livro)
def atualizar_livro(id: int, livro_atualizado: Livro):
    return crud.atualizar_livro(id, livro_atualizado)

@router.delete("/{id}")
def deletar_livro(id: int):
    return crud.deletar_livro(id)
