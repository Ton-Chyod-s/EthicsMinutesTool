import sys
from PySide6.QtWidgets import QApplication
from document_filler_app.interfaces import MainController
from document_filler_app.domain.models import Base

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainController()
    window.show()
    sys.exit(app.exec())
