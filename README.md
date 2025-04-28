## CRUD de Livros com FastAPI e Persistência em XML

## Objetivo
Desenvolver uma API utilizando o framework FastAPI que realiza operações de CRUD (Create, Read, Update, Delete) para gerenciar informações sobre livros.  
A persistência dos dados é feita em um arquivo XML, garantindo que as informações estejam disponíveis entre as execuções do programa.

## Estrutura de Dados - Livro
Cada livro contém os seguintes campos:
- **id** (int): Identificador único do livro.
- **titulo** (str): Título do livro.
- **autor** (str): Nome do autor do livro.
- **ano** (int): Ano de publicação do livro.
- **genero** (str): Gênero literário do livro.

## Operações CRUD disponíveis

- **Criar Livro (Create)**  
  Rota: `POST /livros`  
  Descrição: Recebe um JSON com as informações de um novo livro e adiciona ao arquivo XML.

- **Listar Livros (Read)**  
  Rota: `GET /livros`  
  Descrição: Retorna a lista completa de livros, carregada do arquivo XML.

- **Buscar Livro por ID (Read)**  
  Rota: `GET /livros/{id}`  
  Descrição: Busca um livro específico pelo seu `id`.

- **Atualizar Livro (Update)**  
  Rota: `PUT /livros/{id}`  
  Descrição: Recebe os dados atualizados de um livro e modifica as informações no arquivo XML.

- **Deletar Livro (Delete)**  
  Rota: `DELETE /livros/{id}`  
  Descrição: Remove um livro do arquivo XML.

## Persistência em XML
Todos os dados dos livros são armazenados no arquivo `livros.xml`, localizado na raiz do projeto.  
A manipulação do arquivo XML é feita utilizando a biblioteca `xml.etree.ElementTree`, garantindo que os dados persistam entre reinicializações da aplicação.

Se o arquivo `livros.xml` não existir ou estiver vazio, ele é criado automaticamente com a estrutura básica necessária.

## Como executar o projeto

1. Instale as dependências:

```json
pip install -r requirements.txt

2. Instale o FastAPI e o Uvicorn: 

pip install fastapi uvicorn

3. Rode o servidor:

python -m uvicorn app.main:app --reload

4. Acesse a documentação interativa (Swagger UI) em:

http://127.0.0.1:8000/docs

## Exemplo de Requisição JSON para Criar Livro

```json
{
 "id": 1,
 "titulo": "Dom Quixote",
 "autor": "Miguel de Cervantes",
 "ano": 1605,
 "genero": "Romance"
}

