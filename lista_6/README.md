#  API de Blog Pessoal

##  Descrição

API RESTful que permite o gerenciamento de um **Blog Pessoal**, com suporte completo a operações de **CRUD**, utilizando o **FastAPI** e o **fastapi-crudrouter**.

## Entidades Principais

- **Usuário**: cria posts, comentários e curtidas.
- **Post**: publicado por um usuário; pode ter várias categorias, comentários e curtidas.
- **Categoria**: agrupa posts por temas.
- **Comentário**: texto associado a um post e escrito por um usuário.
- **Curtida**: "like" dado por um usuário em um post.

---

##  Funcionalidades Implementadas

-  CRUD automático para todas as entidades com **fastapi-crudrouter**.
- Relacionamentos entre entidades (posts, categorias, comentários, curtidas).
-  Paginação nas rotas de listagem.
-  Consultas avançadas:
  - Listar posts mais comentados (com paginação).
  - Listar categorias com contagem de posts, ordenadas da maior para a menor.
-  Filtros e buscas:
  - Buscar posts por palavra-chave no título ou conteúdo.
  - Filtrar posts por categoria.

---

##  Tecnologias Utilizadas

- **FastAPI**
- **fastapi-crudrouter**
- **SQLAlchemy**
- **PostgreSQL** 
- **Pydantic**


