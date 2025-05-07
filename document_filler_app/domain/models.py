from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass


class MembrosConvidados(Base):
    __tablename__ = "membros_convocados"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(String)

    def __repr__(self):
        return f"<MembrosConvidados(nome={self.nome}, cpf={self.cpf})>"
        
    __doc__ = "Modelo que representa os membros convocados."

    id.__doc__ = "ID do membro convocado"
    nome.__doc__ = "Nome do membro convocado"
    cpf.__doc__ = "CPF do membro convocado"
    