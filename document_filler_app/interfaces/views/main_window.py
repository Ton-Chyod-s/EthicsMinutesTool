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

        # if os.path.exists(css_path):
        #     with open(css_path, "r") as f:
        #         self.setStyleSheet(f.read())

        # Tipo de documento
        tipo_layout = QHBoxLayout()
        tipo_layout.addWidget(QLabel("🧾 Tipo de documento:"))
        self.tipo_combo = QComboBox()
        self.tipo_combo.addItems(["Ata de Reunião"])
        tipo_layout.addWidget(self.tipo_combo)
        layout.addLayout(tipo_layout)

        # Nome + Data na mesma linha (colunas)
        linha_nome_data = QHBoxLayout()

        # Coluna do Nome
        nome_coluna = QVBoxLayout()
        nome_coluna.addWidget(QLabel("Nome:"))
        self.nome_input = QLineEdit()
        nome_coluna.addWidget(self.nome_input)
        linha_nome_data.addLayout(nome_coluna)

        # Coluna da Data
        data_coluna = QVBoxLayout()
        data_coluna.addWidget(QLabel("Data:"))
        self.data_reuniao_input = QDateEdit()
        self.data_reuniao_input.setCalendarPopup(True)
        data_coluna.addWidget(self.data_reuniao_input)
        linha_nome_data.addLayout(data_coluna)

        # Adiciona a linha ao layout principal
        layout.addLayout(linha_nome_data)

        # Projetos
        projeto_layout = QHBoxLayout()
        projeto_layout.addWidget(QLabel("Projetos:"))
        self.arquivo_btn = QPushButton("📎 Inserir ")
        projeto_layout.addWidget(self.arquivo_btn)
        layout.addLayout(projeto_layout)

        # E-mail
        email_layout = QHBoxLayout()
        email_layout.addWidget(QLabel("E-mail:"))
        self.email_input = QLineEdit()
        email_layout.addWidget(self.email_input)
        layout.addLayout(email_layout)

        # Data de assinatura
        assinatura_layout = QHBoxLayout()
        assinatura_layout.addWidget(QLabel("Data de assinatura:"))
        self.data_assinatura_input = QDateEdit()
        self.data_assinatura_input.setDisplayFormat("dd/MM/yyyy")
        self.data_assinatura_input.setCalendarPopup(True)
        assinatura_layout.addWidget(self.data_assinatura_input)
        layout.addLayout(assinatura_layout)

        # Botões
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
