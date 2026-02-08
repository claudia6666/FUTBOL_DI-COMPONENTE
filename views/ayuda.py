import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
class Ayuda:
    """Carga y muestra `ui/ayuda.ui` tal cual fue creado en Qt Designer."""
    def __init__(self, parent=None):
        ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_ui = os.path.join(ruta_base, "ui", "ayuda.ui")
        if os.path.exists(ruta_ui):
            try:
                loader = QUiLoader()
                ui_file = QFile(ruta_ui)
                if ui_file.open(QIODevice.ReadOnly):
                    self.dialog = loader.load(ui_file, None)
                    ui_file.close()
                    if self.dialog:
                        print(f"Ayuda: .ui cargado desde {ruta_ui}")
                        return
            except Exception as e:
                print(f"Error al cargar {ruta_ui}: {e}")
        from PySide6.QtWidgets import QDialog, QTextEdit, QVBoxLayout, QPushButton
        self.dialog = QDialog(parent)
        self.dialog.setWindowTitle("Ayuda - Gestión de Torneo")
        self.dialog.setGeometry(100, 100, 600, 500)
        layout = QVBoxLayout(self.dialog)
        text = QTextEdit()
        text.setReadOnly(True)
        text.setText(
            "BIENVENIDO A LA GESTIÓN DE TORNEO DE FÚTBOL\n\n"
            "Esta aplicación permite gestionar un torneo deportivo completo de forma sencilla.\n\n"
            "GESTIÓN DE CALENDARIO\n"
            "• Crear, editar y eliminar partidos\n"
            "• Seleccionar equipos, árbitro, fecha y ronda\n\n"
            "RESULTADOS Y ESTADÍSTICAS\n"
            "• Registrar goles y tarjetas de cada jugador\n\n"
            "CONSEJOS DE USO\n"
            "• Seleccione siempre un elemento antes de editar o eliminar\n"
        )
        layout.addWidget(text)
        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.clicked.connect(self.dialog.close)
        layout.addWidget(btn_cerrar)
        print("Ayuda: fallback usado")
    def show(self):
        """Muestra la ventana de ayuda."""
        if self.dialog:
            self.dialog.show()
    def close(self):
        """Cierra la ventana de ayuda."""
        if self.dialog:
            self.dialog.close()
