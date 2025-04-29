from typing import List
from fastapi import HTTPException
from .models import Livro
from .xml_utils import ler_livros, escrever_livros

def criar_livro(livro: Livro) -> Livro:
    livros = ler_livros()
    if any(l.id == livro.id for l in livros):
        raise HTTPException(status_code=400, detail="ID já existe")
    livros.append(livro)
    escrever_livros(livros)
    return livro

def listar_livros() -> List[Livro]:
    return ler_livros()

def buscar_livro(id: int) -> Livro:
    livros = ler_livros()
    for livro in livros:
        if livro.id == id:
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")

def atualizar_livro(id: int, livro_atualizado: Livro) -> Livro:
    livros = ler_livros()
    for i, livro in enumerate(livros):
        if livro.id == id:
            livros[i] = livro_atualizado
            escrever_livros(livros)
            return livro_atualizado
    raise HTTPException(status_code=404, detail="Livro não encontrado")

def deletar_livro(id: int) -> dict:
    livros = ler_livros()
    novos_livros = [l for l in livros if l.id != id]
    if len(novos_livros) == len(livros):
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    escrever_livros(novos_livros)
    return {"mensagem": "Livro deletado com sucesso"}
