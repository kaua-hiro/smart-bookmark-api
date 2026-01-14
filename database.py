from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mssql+pyodbc://SEU_USUARIO:SUA_SENHA@SEU_SERVIDOR/NOME_DO_BANCO?driver=ODBC+Driver+17+for+SQL+Server"

# echo=True ajuda a ver o SQL gerado no terminal (bom pra aprender)
engine = create_engine(DATABASE_URL, echo=False)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    # Cria as tabelas baseadas nos Models
    SQLModel.metadata.create_all(engine)