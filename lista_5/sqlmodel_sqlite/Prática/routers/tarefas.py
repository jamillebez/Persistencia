from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Tarefa

router = APIRouter(prefix="/tarefas", tags=["Tarefas"])

@router.post("", response_model=Tarefa)
def criar_tarefa(tarefa: Tarefa, session: Session = Depends(get_session)) -> Tarefa:
    session.add(tarefa)
    session.commit()
    session.refresh(tarefa)
    return tarefa

@router.get("", response_model=list[Tarefa])
def listar_tarefas(session: Session = Depends(get_session)):
    return session.exec(select(Tarefa)).all()

@router.get("/{tarefa_id}", response_model=Tarefa)
def buscar_tarefa(tarefa_id: int, session: Session = Depends(get_session)):
    tarefa = session.get(Tarefa, tarefa_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

@router.put("/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(tarefa_id: int, tarefa: Tarefa, session: Session = Depends(get_session)):
    tarefa_atual = session.get(Tarefa, tarefa_id)
    if not tarefa_atual:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa_data = tarefa.model_dump(exclude_unset=True)
    for key, value in tarefa_data.items():
        setattr(tarefa_atual, key, value)
    session.add(tarefa_atual)
    session.commit()
    session.refresh(tarefa_atual)
    return tarefa_atual

@router.delete("/{tarefa_id}")
def excluir_tarefa(tarefa_id: int, session: Session = Depends(get_session)):
    tarefa = session.get(Tarefa, tarefa_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    session.delete(tarefa)
    session.commit()
    return {"message": "Tarefa excluída com sucesso"}
