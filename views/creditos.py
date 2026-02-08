from PySide6.QtWidgets import QDialog
from widgets.ui_creditos import Ui_DialogCreditos
class Creditos(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogCreditos()
        self.ui.setupUi(self)
        print("Créditos cargados")
