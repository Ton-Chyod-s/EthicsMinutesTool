from document_filler_app.interfaces.views.main_window import MainWindow


class MainController(MainWindow):
    def __init__(self):
        super().__init__()
        self.button.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        self.label.setText("Você clicou no botão!")
