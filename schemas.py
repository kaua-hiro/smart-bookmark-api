from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

# VIEW: O que o usuario manda pra criar (Input)
class LinkCreate(BaseModel):
    url: HttpUrl # Valida se eh URL mesmo

# VIEW: O que a API devolve (Output)
class LinkRead(BaseModel):
    id: int
    url: str
    title: Optional[str]
    created_at: datetime