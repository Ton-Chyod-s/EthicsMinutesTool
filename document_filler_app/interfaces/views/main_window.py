from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App PySide6")
        self.setFixedSize(300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.label = QLabel("Clique no botão")
        self.button = QPushButton("Clique aqui")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.central_widget.setLayout(layout)
