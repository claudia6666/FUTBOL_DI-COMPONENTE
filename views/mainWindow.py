from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from widgets.ui_mainWindow import Ui_MainWindow
from views.calendario import Calendario
from views.resultados import Resultados
from views.eliminatorias import DialogEliminatorias
from views.creditos import Creditos
from views.equipos import Equipos
from views.participantes import Participantes
from views.ayuda import Ayuda
from views.gestion_partidos import GestionPartidos

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cargar_imagenes()
        self.calendario_window = Calendario()
        self.resultados_window = Resultados()
        self.eliminatorias_window = DialogEliminatorias()
        self.creditos_window = Creditos()
        self.equipos_window = Equipos()
        self.participantes_window = Participantes(calendario_window=self.calendario_window)
        self.ayuda_window = Ayuda()
        self.gestion_partidos_window = GestionPartidos()
        self.ui.btnCalendario.clicked.connect(self.calendario_window.show)
        self.ui.btnResultados.clicked.connect(self.resultados_window.show)
        self.ui.btnClasificacion.clicked.connect(self.eliminatorias_window.show)
        self.ui.btnEstadisticas.clicked.connect(self.gestion_partidos_window.show)
        self.ui.btnParticipantes.clicked.connect(self.participantes_window.show)
        self.ui.btnEquipos.clicked.connect(self.equipos_window.show)
        self.ui.actionAyuda.triggered.connect(self.ayuda_window.show)
        self.ui.actionCreditos.triggered.connect(self.creditos_window.show)
        self.ui.actionSalir.triggered.connect(self.close)
    def cargar_imagenes(self):
        import os
        import sys
        if getattr(sys, 'frozen', False):
            ruta_base = sys._MEIPASS
        else:
            ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_imagenes = os.path.join(ruta_base, "resources", "img")
        imagenes = {
            "label": os.path.join(ruta_imagenes, "Champ.jpg"),
            "label_2": os.path.join(ruta_imagenes, "equipo.jpg"),
            "label_3": os.path.join(ruta_imagenes, "entreno.jpg")
        }
        for nombre_label, ruta_imagen in imagenes.items():
            if os.path.exists(ruta_imagen):
                label = getattr(self.ui, nombre_label, None)
                if label:
                    pixmap = QPixmap(ruta_imagen)
                    pixmap = pixmap.scaledToWidth(300, Qt.SmoothTransformation)
                    label.setPixmap(pixmap)
                    print(f"Imagen cargada en {nombre_label}: {ruta_imagen}")
            else:
                print(f"Advertencia: No se encontró la imagen {ruta_imagen}")
