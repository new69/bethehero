from uuid import uuid4

from pydantic import BaseModel, Field, field_validator

from src.domain.entity.validators.brazilian_document import BrazilianDocument
from src.domain.entity.validators.email import Email
from src.domain.entity.validators.phone_number import PhoneNumber


class Ong(BaseModel):
    id: str = Field(..., default_factory=lambda: str(uuid4()))
    name: str
    email: str
    whatsapp: str
    document: str

    @field_validator('email')
    @classmethod
    def email_validator(cls, v: str) -> str:
        return Email(v).get_value()

    @field_validator('whatsapp')
    @classmethod
    def phone_number_validator(cls, v: str) -> str:
        return PhoneNumber(v).get_value()

    @field_validator('document')
    @classmethod
    def document_validator(cls, v: str) -> str:
        return BrazilianDocument(v).get_value()
