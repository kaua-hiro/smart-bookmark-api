# Smart Bookmark API 🔖

API simples feita com **FastAPI** que salva links e busca automaticamente o título da página usando **Web Scraping Assíncrono**.

## Tecnologias
- Python 3.10+
- FastAPI (API)
- SQLModel (Banco de dados SQLite)
- HTTPX (Requisições Async)
- BeautifulSoup4 (Parsing HTML)

## Como rodar
1. Instale as dependências:
`pip install -r requirements.txt`

2. Rode o servidor:
`uvicorn main:app --reload`

3. Acesse a doc: `http://127.0.0.1:8000/docs`