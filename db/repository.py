from db.database import SessionLocal
from document_filler_app.domain.models import MembrosConvidados


class DocumentoRepository:
    def __init__(self):
        self.session = SessionLocal()

    def salvar(self, doc: MembrosConvidados):
        self.session.add(doc)
        self.session.commit()
        self.session.refresh(doc)
        return doc

    def listar_todos(self):
        return self.session.query(MembrosConvidados).all()
