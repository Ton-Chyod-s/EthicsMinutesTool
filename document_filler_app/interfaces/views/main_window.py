from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QVBoxLayout,
    QHBoxLayout,
    QDateEdit,
)
import os


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Preenchimento de Documento")
        self.setup_ui()

    def setup_ui(self):
        css_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "assets", "style.qss")
        )

        layout = QVBoxLayout()

        # Carregar o arquivo CSS
        if os.path.exists(css_path):
            with open(css_path, "r") as f:
                self.setStyleSheet(f.read())

        # Tipo de documento
        tipo_layout = QHBoxLayout()
        tipo_layout.addWidget(QLabel("🧾 Tipo de documento:"))
        self.tipo_combo = QComboBox()
        self.tipo_combo.addItems(["Ata de Reunião"])
        tipo_layout.addWidget(self.tipo_combo)
        layout.addLayout(tipo_layout)

        # Nome completo
        layout.addWidget(QLabel("Nome completo:"))
        self.nome_input = QLineEdit()
        layout.addWidget(self.nome_input)

        # CPF
        layout.addWidget(QLabel("CPF:"))
        self.cpf_input = QLineEdit()
        layout.addWidget(self.cpf_input)

        # E-mail
        layout.addWidget(QLabel("E-mail:"))
        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

        # Data de assinatura
        layout.addWidget(QLabel("Data de assinatura:"))
        self.data_input = QDateEdit()
        self.data_input.setDisplayFormat("dd/MM/yyyy")
        self.data_input.setCalendarPopup(True)
        layout.addWidget(self.data_input)

        # Seleção de arquivo
        self.arquivo_btn = QPushButton("📎 Selecionar arquivo base...")
        layout.addWidget(self.arquivo_btn)

        # Botões principais
        botoes_layout = QHBoxLayout()
        self.preview_btn = QPushButton("📄 Pré-visualizar")
        self.gerar_btn = QPushButton("💾 Gerar Documento")
        self.limpar_btn = QPushButton("❌ Limpar")
        botoes_layout.addWidget(self.preview_btn)
        botoes_layout.addWidget(self.gerar_btn)
        botoes_layout.addWidget(self.limpar_btn)
        layout.addLayout(botoes_layout)

        # Resultado
        self.resultado_label = QLabel("")
        layout.addWidget(self.resultado_label)

        self.setLayout(layout)
