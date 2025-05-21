from fastapi import FastAPI
from database import create_db_and_tables
from routers import equipes, membros, projetos, tarefas, memberships


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
@app.get("/")
def home():
    return {"mensagem": "Bem vindo"}

app.include_router(equipes.router)
app.include_router(membros.router)
app.include_router(projetos.router)
app.include_router(tarefas.router)
app.include_router(memberships.router)