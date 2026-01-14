import httpx
from bs4 import BeautifulSoup

class LinkScraperService:
    @staticmethod
    async def extract_title(url: str) -> str:
        """
        Serviço responsavel por ir na web e buscar metadados.
        Isolado para nao poluir o controller.
        """
        try:
            async with httpx.AsyncClient() as client:
                # Converte HttpUrl para string se necessario
                url_str = str(url)
                response = await client.get(url_str, timeout=10)

                if response.status_code >= 400:
                    return "Site inacessível"

                soup = BeautifulSoup(response.text, 'html.parser')
                if soup.title and soup.title.string:
                    return soup.title.string.strip()
                return "Sem título identificado"

        except Exception as e:
            # Em prod, aqui entraria um logger real
            print(f"Erro no scraper: {e}")
            return "Erro ao processar"