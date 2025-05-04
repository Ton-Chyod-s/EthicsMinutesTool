from PySide6.QtWidgets import QFileDialog, QMessageBox, QDialog, QVBoxLayout, QListWidget, QPushButton
from document_filler_app.interfaces.views.main_window import MainWindow
import os
import shutil

class MainController(MainWindow):
    def __init__(self):
        super().__init__()

        self.arquivo_btn.clicked.connect(self.selecionar_arquivo)
        self.gerar_btn.clicked.connect(self.gerar_documento)
        self.limpar_btn.clicked.connect(self.limpar_formulario)

    def selecionar_arquivo(self):
        arquivo, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar arquivo ataProjetos",
            "",
            "PDF Files (*.pdf);;All Files (*)"
        )

        if arquivo:
            # Pasta de destino (cria se não existir)
            pasta_destino = os.path.join(os.getcwd(), "resources")
            os.makedirs(pasta_destino, exist_ok=True)

            # Nome do arquivo original
            nome_arquivo = os.path.basename(arquivo)

            # Caminho final de destino
            destino = os.path.join(pasta_destino, nome_arquivo)

            # Copiar o arquivo
            shutil.copy2(arquivo, destino)

            # Atualizar texto do botão com o caminho final
            self.arquivo_btn.setText(f"📎 {destino}")

    def gerar_documento(self):
        self.resultado_label.setText("✅ Documento gerado com sucesso! Salvo em: /docs/...")
        QMessageBox.information(self, "Documento", "Documento gerado com sucesso!")

    def limpar_formulario(self):
        self.nome_input.clear()
        self.email_input.clear()
        self.arquivo_btn.setText("📎 Inserir")
        self.resultado_label.setText("")

    