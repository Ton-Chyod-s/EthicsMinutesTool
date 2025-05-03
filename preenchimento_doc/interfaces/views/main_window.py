import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Título da janela
        self.setWindowTitle("Exemplo de GUI com PySide6")

        # Layout vertical
        layout = QVBoxLayout()

        # Rótulo (label)
        self.label = QLabel("Clique no botão!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        # Botão
        self.button = QPushButton("Clique aqui")
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        # Configura o layout na janela
        self.setLayout(layout)

    def on_button_click(self):
        """Método chamado quando o botão é pressionado."""
        # Altera o texto do rótulo
        self.label.setText("Botão pressionado!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
