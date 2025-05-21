from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Equipe, Membro

router = APIRouter(prefix="/membros", tags=["Membros"])

@router.post("", response_model=Membro)
def criar_membro(membro: Membro, session: Session = Depends(get_session)) -> Membro:
    session.add(membro)
    session.commit()
    session.refresh(membro)
    return membro

@router.get("", response_model=list[Membro])
def listar_membros(session: Session = Depends(get_session)):
    return session.exec(select(Membro)).all()

@router.get("/{membro_id}", response_model=Membro)
def buscar_membro(membro_id: int, session: Session = Depends(get_session)):
    membro = session.get(Membro, membro_id)
    if not membro:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return membro

@router.put("/{membro_id}", response_model=Membro)
def atualizar_membro(membro_id: int, membro: Membro, session: Session = Depends(get_session)):
    membro_atual = session.get(Membro, membro_id)
    if not membro_atual:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    
    membro_data = membro.model_dump(exclude_unset=True)
    for key, value in membro_data.items():
        setattr(membro_atual, key, value)

    session.add(membro_atual)
    session.commit()
    session.refresh(membro_atual)
    return membro_atual

