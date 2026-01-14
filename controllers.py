from typing import Optional
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models import Link
from schemas import LinkCreate, LinkRead
from services import LinkScraperService

router = APIRouter(prefix="/links", tags=["Links"])

@router.post("/", response_model=LinkRead)
async def create_link(link_input: LinkCreate, session: Session = Depends(get_session)):
    # Mantivemos igual: chama o scraper, cria o objeto e salva
    title_extracted = await LinkScraperService.extract_title(link_input.url)
    
    new_link = Link(url=str(link_input.url), title=title_extracted)
    
    session.add(new_link)
    session.commit()
    session.refresh(new_link)
    
    return new_link

@router.get("/", response_model=list[LinkRead])
def list_links(
    q: Optional[str] = None,  # Query Param: Aceita ?q=valor (opcional)
    session: Session = Depends(get_session)
):
    """
    Lista todos os links.
    Se o parametro 'q' for passado, filtra pelo título.
    """
    statement = select(Link)
    
    # Se o usuario mandou algo no 'q', a gente filtra
    if q:
        # Busca onde o titulo CONTEM o texto (CASE INSENSITIVE na maioria dos bancos)
        statement = statement.where(Link.title.contains(q))
    
    results = session.exec(statement).all()
    return results