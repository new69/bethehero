import uuid

from sqlalchemy import UUID, Column, String

from src.infra.db.conn import Base


class Ong(Base):
    __tablename__ = 'ongs'

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    whatsapp = Column(String, nullable=False)
    document = Column(String, nullable=False, unique=True)

    def __repr__(self) -> str:
        return (
            f'<Ong(id={self.id}, name={self.name}, email={self.email}, '
            'whastapp={self.whastapp}, document={self.document})>'
        )
