import sys
from PySide6.QtWidgets import QApplication
from views.mainWindow import MainWindow
from models.database import conectar
from models.globals import set_db_connection
if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        db = conectar()
        set_db_connection(db)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
