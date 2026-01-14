from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv

# Carrega as variaveis do arquivo .env
load_dotenv()

# Pega a string de conexao segura
database_url = os.getenv("DB_CONNECTION_STRING")

# Verificacao de seguranca (caso esqueca de criar o .env)
if not database_url:
    raise ValueError("A variavel DB_CONNECTION_STRING não foi definida no .env")

engine = create_engine(database_url)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)