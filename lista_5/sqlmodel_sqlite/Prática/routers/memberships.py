from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Membership

router = APIRouter(prefix="/memberships", tags=["Memberships"])

@router.post("", response_model=Membership)
def criar_membership(membership: Membership, session: Session = Depends(get_session)) -> Membership:
    session.add(membership)
    session.commit()
    session.refresh(membership)
    return membership

@router.get("", response_model=list[Membership])
def listar_memberships(session: Session = Depends(get_session)):
    return session.exec(select(Membership)).all()

@router.get("/{membership_id}", response_model=Membership)
def buscar_membership(membership_id: int, session: Session = Depends(get_session)):
    membership = session.get(Membership, membership_id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membership não encontrado")
    return membership

@router.put("/{membership_id}", response_model=Membership)
def atualizar_membership(membership_id: int, membership: Membership, session: Session = Depends(get_session)):
    membership_atual = session.get(Membership, membership_id)
    if not membership_atual:
        raise HTTPException(status_code=404, detail="Membership não encontrado")
    membership_data = membership.model_dump(exclude_unset=True)
    for key, value in membership_data.items():
        setattr(membership_atual, key, value)
    session.add(membership_atual)
    session.commit()
    session.refresh(membership_atual)
    return membership_atual

@router.delete("/{membership_id}")
def excluir_membership(membership_id: int, session: Session = Depends(get_session)):
    membership = session.get(Membership, membership_id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membership não encontrado")
    session.delete(membership)
    session.commit()
    return {"message": "Membership excluído com sucesso"}
