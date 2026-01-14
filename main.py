from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import create_db_and_tables, get_session
from models import Link
from services import get_page_title

app = FastAPI()

# Cria as tabelas quando o app inicia
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/links/", response_model=Link)
async def create_link(link_data: Link, session: Session = Depends(get_session)):
    # Primeiro pega o titulo automatico
    title = await get_page_title(link_data.url)
    link_data.title = title

    session.add(link_data)
    session.commit()
    session.refresh(link_data)
    return link_data

@app.get("/links/", response_model=list[Link])
def read_links(session: Session = Depends(get_session)):
    links = session.exec(select(Link)).all()
    return links