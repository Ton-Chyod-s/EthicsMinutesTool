from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Preenchimento de Documento  ")
        self.adjustSize()
        # self.resize(300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.label = QLabel("Clique no botão")
        self.button = QPushButton("Clique aqui")
        self.button.setFixedSize(320, 25)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.central_widget.setLayout(layout)
