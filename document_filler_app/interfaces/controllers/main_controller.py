from document_filler_app.interfaces.views.main_window import MainWindow
from PySide6.QtWidgets import QFileDialog, QMessageBox


class MainController(MainWindow):
    def __init__(self):
        super().__init__()
        self.arquivo_btn.clicked.connect(self.selecionar_arquivo)
        self.gerar_btn.clicked.connect(self.gerar_documento)
        self.limpar_btn.clicked.connect(self.limpar_formulario)

    def selecionar_arquivo(self):
        arquivo, _ = QFileDialog.getOpenFileName(
            self, "Selecionar arquivo base", "", "PDF Files (*.pdf);;All Files (*)"
        )
        if arquivo:
            self.arquivo_btn.setText(f"📎 {arquivo}")

    def gerar_documento(self):
        self.resultado_label.setText(
            "✅ Documento gerado com sucesso! Salvo em: /docs/..."
        )
        QMessageBox.information(self, "Documento", "Documento gerado com sucesso!")

    def limpar_formulario(self):
        self.nome_input.clear()
        self.cpf_input.clear()
        self.email_input.clear()
        self.arquivo_btn.setText("📎 Selecionar arquivo base...")
        self.resultado_label.setText("")
