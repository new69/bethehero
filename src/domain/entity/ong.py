from pydantic import BaseModel


class Ong(BaseModel):
    name: str
    email: str
    whatsapp: str
    document: str
