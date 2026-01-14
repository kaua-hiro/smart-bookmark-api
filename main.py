from fastapi import FastAPI
from database import create_db_and_tables
from controllers import router as link_router

app = FastAPI(title="Smart Bookmark API - MVC Version")


@app.on_event("startup")
def on_startup():
    # Garante que as tabelas existam no SQL Server ao iniciar
    create_db_and_tables()


# Registra as rotas (Controllers)
app.include_router(link_router)


@app.get("/")
def root():
    return {"message": "API Online. Acesse /docs para testar."}
