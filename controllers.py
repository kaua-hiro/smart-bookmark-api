from typing import Optional
from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from schemas import LinkCreate, LinkRead
from services import LinkService

router = APIRouter(prefix="/links", tags=["Links"])

@router.post("/", response_model=LinkRead)
async def create_link(
    link_input: LinkCreate, 
    session: Session = Depends(get_session)
):
    # O Controller apenas repassa para o Service
    return await LinkService.create_link(session=session, url=link_input.url)

@router.get("/", response_model=list[LinkRead])
def list_links(
    q: Optional[str] = None, 
    session: Session = Depends(get_session)
):
    # O Controller nao faz query SQL, ele pede os dados prontos
    return LinkService.list_links(session=session, search_term=q)