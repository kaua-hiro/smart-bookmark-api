import httpx
from bs4 import BeautifulSoup
from sqlmodel import Session, select
from models import Link

class LinkService:
    @staticmethod
    async def _get_title_from_web(url: str) -> str:
        """Metodo privado (interno) para fazer scraping"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(str(url), timeout=10)
                if response.status_code >= 400:
                    return "Site inacessível"
                
                soup = BeautifulSoup(response.text, 'html.parser')
                if soup.title and soup.title.string:
                    return soup.title.string.strip()
                return "Sem título identificado"
        except Exception as e:
            print(f"Erro no scraper: {e}")
            return "Erro ao processar"

    @classmethod
    async def create_link(cls, session: Session, url: str) -> Link:
        """
        Orquestra a criacao: 
        1. Vai na web pegar o titulo
        2. Salva no banco
        """
        # Regra de Negocio: Buscar o titulo antes de salvar
        title = await cls._get_title_from_web(url)
        
        # Persistencia: Salvar no banco
        new_link = Link(url=str(url), title=title)
        session.add(new_link)
        session.commit()
        session.refresh(new_link)
        
        return new_link

    @staticmethod
    def list_links(session: Session, search_term: str | None = None) -> list[Link]:
        """
        Regra de Leitura:
        Busca todos ou filtra se tiver termo de busca
        """
        statement = select(Link)
        
        if search_term:
            statement = statement.where(Link.title.contains(search_term))
            
        return session.exec(statement).all()