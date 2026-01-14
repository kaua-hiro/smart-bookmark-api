from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Link
from schemas import LinkCreate, LinkRead
from services import LinkScraperService

router = APIRouter(prefix="/links", tags=["Links"])


@router.post("/", response_model=LinkRead)
async def create_link(link_input: LinkCreate, session: Session = Depends(get_session)):
    # 1. Chama o Service para pegar a logica (Scraping)
    title_extracted = await LinkScraperService.extract_title(link_input.url)

    # 2. Prepara o Model para salvar
    new_link = Link(url=str(link_input.url), title=title_extracted)

    # 3. Interage com o Banco
    session.add(new_link)
    session.commit()
    session.refresh(new_link)

    return new_link


@router.get("/", response_model=list[LinkRead])
def list_links(session: Session = Depends(get_session)):
    statement = select(Link)
    results = session.exec(statement).all()
    return results
