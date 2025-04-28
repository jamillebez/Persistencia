import os
import xml.etree.ElementTree as ET
from typing import List
from .models import Livro
import xml.dom.minidom

XML_FILE = "livros.xml"

def inicializar_xml():
    if not os.path.exists(XML_FILE) or os.path.getsize(XML_FILE) == 0:
        root = ET.Element("livros")
        tree = ET.ElementTree(root)
        salvar_xml_formatado(tree)

def ler_livros() -> List[Livro]:
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
    salvar_xml_formatado(tree)

def salvar_xml_formatado(tree: ET.ElementTree):
    xml_str = ET.tostring(tree.getroot(), 'utf-8')
    parsed_str = xml.dom.minidom.parseString(xml_str)
    # Remover a declaração XML
    pretty_xml = parsed_str.toprettyxml(indent="  ", newl='\n')
    pretty_xml = "\n".join(pretty_xml.splitlines()[1:])  # Remove the first line with XML declaration
    with open(XML_FILE, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
