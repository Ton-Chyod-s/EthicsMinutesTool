from db.database import SessionLocal
from document_filler_app.domain.models import MembrosConvidados, VersaoAtaReuniao
from document_filler_app.utils.managed_session import get_session

class BaseRepository:
    def __init__(self, model):
        self.model = model

    def salvar(self, doc):
        with get_session() as session:
            session.add(doc)
            session.commit()
            session.refresh(doc)
            return doc

    def listar_todos(self):
        with get_session() as session:
            return session.query(self.model).all()

class DocumentoRepository(BaseRepository):
    def __init__(self):
        super().__init__(MembrosConvidados)

class VersaoAtaReuniaoRepository(BaseRepository):
    def __init__(self):
        super().__init__(VersaoAtaReuniao)