from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass


class Documento(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(String)
    email = Column(String)
