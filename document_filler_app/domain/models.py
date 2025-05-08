from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime


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

class VersaoAtaReuniao(Base):
    __tablename__ = "versao_ata_reuniao"

    id = Column(Integer, primary_key=True, index=True)
    versao = Column(DateTime)

    def __repr__(self):
        return f"<VersaoAtaReuniao(versao={self.versao})>"
        
    __doc__ = "Modelo que representa a versão da ata de reunião."

    id.__doc__ = "ID da versão da ata de reunião"
    versao.__doc__ = "Versão da ata de reunião"