import httpx
from bs4 import BeautifulSoup

async def get_page_title(url: str) -> str:
    try:
        # Client assincrono para nao travar a api
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10)

            if response.status_code >= 400:
                return "Erro ao acessar site"

            soup = BeautifulSoup(response.text, 'html.parser')

            # Pega o titulo ou retorna desconhecido se nao tiver
            if soup.title and soup.title.string:
                return soup.title.string
            return "Sem título"

    except Exception as e:
        print(f"Erro na url {url}: {e}")
        return "Erro na extração"