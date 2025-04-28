from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.responses import FileResponse
import xml.etree.ElementTree as ET
import os

app = FastAPI()
XML_FILE = "livros.xml"

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int
    genero: str

def inicializar_xml():
    if not os.path.exists(XML_FILE):
        root = ET.Element("livros")
        tree = ET.ElementTree(root)
        tree.write(XML_FILE)

def ler_livros():
    inicializar_xml()
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    livros = []
    for elem in root.findall("livro"):
        livro = Livro(
            id=int(elem.find("id").text),
            titulo=elem.find("titulo").text,
            autor=elem.find("autor").text,
            ano=int(elem.find("ano").text),
            genero=elem.find("genero").text
        )
        livros.append(livro)
    return livros

def escrever_livros(livros: List[Livro]):
    root = ET.Element("livros")
    for livro in livros:
        e = ET.SubElement(root, "livro")
        ET.SubElement(e, "id").text = str(livro.id)
        ET.SubElement(e, "titulo").text = livro.titulo
        ET.SubElement(e, "autor").text = livro.autor
        ET.SubElement(e, "ano").text = str(livro.ano)
        ET.SubElement(e, "genero").text = livro.genero
    tree = ET.ElementTree(root)
    tree.write(XML_FILE)

@app.post("/livros", response_model=Livro)
def criar_livro(livro: Livro):
    livros = ler_livros()
    if any(l.id == livro.id for l in livros):
        raise HTTPException(status_code=400, detail="ID já existe")
    livros.append(livro)
    escrever_livros(livros)
    return livro

@app.get("/livros", response_model=List[Livro])
def listar_livros():
    return ler_livros()

@app.get("/livros/{id}", response_model=Livro)
def buscar_livro(id: int):
    livros = ler_livros()
    for livro in livros:
        if livro.id == id:
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.put("/livros/{id}", response_model=Livro)
def atualizar_livro(id: int, livro_atualizado: Livro):
    livros = ler_livros()
    for i, livro in enumerate(livros):
        if livro.id == id:
            livros[i] = livro_atualizado
            escrever_livros(livros)
            return livro_atualizado
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.delete("/livros/{id}")
def deletar_livro(id: int):
    livros = ler_livros()
    novos_livros = [l for l in livros if l.id != id]
    if len(novos_livros) == len(livros):
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    escrever_livros(novos_livros)
    return {"mensagem": "Livro deletado com sucesso"}