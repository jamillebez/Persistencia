from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import select, Session
from models import Projeto
from database import get_session

router = APIRouter(prefix="/projetos", tags=["Projetos"])

@router.post("", response_model=Projeto)
def criar_projeto(projeto: Projeto, session: Session = Depends(get_session)) -> Projeto:
    session.add(projeto)
    session.commit()
    session.refresh(projeto)
    return projeto

@router.get("", response_model=list[Projeto])
def listar_projetos(session: Session = Depends(get_session)):
    return session.exec(select(Projeto)).all()

@router.get("/{projeto_id}", response_model=Projeto)
def buscar_projeto(projeto_id: int, session: Session = Depends(get_session)):
    projeto = session.get(Projeto, projeto_id)
    
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return projeto

@router.put("/{projeto_id}", response_model=Projeto)
def atualizar_projeto(projeto_id: int, projeto: Projeto, session: Session = Depends(get_session)):
    projeto_atual = session.get(Projeto, projeto_id)
    
    if not projeto_atual:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    
    projeto_data = projeto.model_dump(exclude_unset=True)
    for key, value in projeto_data.items():
        setattr(projeto_atual, key, value)
        
    session.add(projeto_atual)
    session.commit()
    session.refresh(projeto_atual)
    return projeto_atual

@router.delete("/{projeto_id}")
def excluir_projeto(projeto_id: int, session: Session = Depends(get_session)):
    projeto = session.get(Projeto, projeto_id)
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    session.delete(projeto)
    session.commit()
    return {"message": "Projeto excluído com sucesso"}