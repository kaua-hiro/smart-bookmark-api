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

## 🏗 Arquitetura e Design Patterns

Este projeto foi desenhado seguindo os princípios de **Separation of Concerns (SoC)** e **Layered Architecture**:

- **Controllers (`controllers.py`):** Responsáveis apenas pela camada de transporte (HTTP), validação de entrada/saída e injeção de dependências.
- **Service Layer (`services.py`):** Contém toda a lógica de negócio e orquestração. O padrão **Service Layer** foi aplicado para isolar o domínio, permitindo que a regra de "buscar título automaticamente" seja reutilizável e independente das rotas.
- **Models & Schemas:** Utilização do **SQLModel** e **Pydantic** para garantir integridade de dados e separação entre modelo de banco e modelo de visualização (DTOs).