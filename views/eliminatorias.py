from PySide6.QtWidgets import (
    QDialog, QTableWidgetItem, QMessageBox, 
    QFileDialog, QLabel, QFrame, QVBoxLayout, QHBoxLayout,
    QPushButton, QSpinBox, QWidget
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor, QBrush
from widgets.ui_eliminatorias import Ui_DialogEliminatorias
from datetime import datetime, timedelta
import csv
class Equipo:
    def __init__(self, nombre, grupo="A"):
        self.nombre = nombre
        self.grupo = grupo
        self.partidos_jugados = 0
        self.partidos_ganados = 0
        self.partidos_empatados = 0
        self.partidos_perdidos = 0
        self.goles_favor = 0
        self.goles_contra = 0
        self.puntos = 0
    @property
    def diferencia_goles(self):
        return self.goles_favor - self.goles_contra
    def registrar_victoria(self, goles_favor, goles_contra):
        self.partidos_jugados += 1
        self.partidos_ganados += 1
        self.goles_favor += goles_favor
        self.goles_contra += goles_contra
        self.puntos += 3
    def registrar_empate(self, goles_favor, goles_contra):
        self.partidos_jugados += 1
        self.partidos_empatados += 1
        self.goles_favor += goles_favor
        self.goles_contra += goles_contra
        self.puntos += 1
    def registrar_derrota(self, goles_favor, goles_contra):
        self.partidos_jugados += 1
        self.partidos_perdidos += 1
        self.goles_favor += goles_favor
        self.goles_contra += goles_contra
class PartidoEliminatoria:
    def __init__(self, id_partido, equipo1, equipo2, fase, ronda):
        self.id_partido = id_partido
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.fase = fase
        self.ronda = ronda
        self.goles_equipo1 = None
        self.goles_equipo2 = None
        self.ganador = None
        self.estado = "Pendiente"
        self.fecha = None
    def registrar_resultado(self, goles1, goles2):
        self.goles_equipo1 = goles1
        self.goles_equipo2 = goles2
        if goles1 > goles2:
            self.ganador = self.equipo1
        elif goles2 > goles1:
            self.ganador = self.equipo2
        else:
            self.ganador = None
        self.estado = "Finalizado"
        return self.ganador
    def get_resultado_texto(self):
        if self.goles_equipo1 is not None and self.goles_equipo2 is not None:
            return f"{self.goles_equipo1} - {self.goles_equipo2}"
        return "vs"
class GestorTorneo:
    def __init__(self):
        self.equipos = {}
        self.clasificacion = []
        self.equipos_clasificados = []
        self.partidos_eliminatorias = {
            "Cuartos de Final": [],
            "Semifinales": [],
            "Final": [],
            "Tercer Lugar": []
        }
        self.fase_actual = "Cuartos de Final"
        self.campeon = None
        self.subcampeon = None
        self.tercer_lugar = None
    def agregar_equipo(self, nombre, grupo="A"):
        equipo = Equipo(nombre, grupo)
        self.equipos[nombre] = equipo
        self.actualizar_clasificacion()
    def actualizar_clasificacion(self):
        self.clasificacion = sorted(
            self.equipos.values(),
            key=lambda e: (-e.puntos, -e.diferencia_goles, -e.goles_favor, e.nombre)
        )
    def obtener_equipos_clasificados(self, num_equipos=8):
        self.actualizar_clasificacion()
        self.equipos_clasificados = [e.nombre for e in self.clasificacion[:num_equipos]]
        return self.equipos_clasificados
    def generar_cuartos_final(self):
        if len(self.equipos_clasificados) < 8:
            raise ValueError("Se necesitan 8 equipos clasificados para cuartos de final")
        emparejamientos = [
            (self.equipos_clasificados[0], self.equipos_clasificados[7]),
            (self.equipos_clasificados[1], self.equipos_clasificados[6]),
            (self.equipos_clasificados[2], self.equipos_clasificados[5]),
            (self.equipos_clasificados[3], self.equipos_clasificados[4])
        ]
        self.partidos_eliminatorias["Cuartos de Final"] = []
        for i, (eq1, eq2) in enumerate(emparejamientos, 1):
            partido = PartidoEliminatoria(
                id_partido=f"CF{i}",
                equipo1=eq1,
                equipo2=eq2,
                fase="Cuartos de Final",
                ronda=i
            )
            self.partidos_eliminatorias["Cuartos de Final"].append(partido)
        self.fase_actual = "Cuartos de Final"
        return self.partidos_eliminatorias["Cuartos de Final"]
    def generar_semifinales(self):
        cuartos = self.partidos_eliminatorias["Cuartos de Final"]
        if not all(p.estado == "Finalizado" for p in cuartos):
            raise ValueError("Todos los partidos de cuartos deben estar finalizados")
        ganadores = [p.ganador for p in cuartos if p.ganador]
        if len(ganadores) < 4:
            raise ValueError("Se necesitan 4 ganadores de cuartos de final")
        emparejamientos = [
            (ganadores[0], ganadores[3]),
            (ganadores[1], ganadores[2])
        ]
        self.partidos_eliminatorias["Semifinales"] = []
        for i, (eq1, eq2) in enumerate(emparejamientos, 1):
            partido = PartidoEliminatoria(
                id_partido=f"SF{i}",
                equipo1=eq1,
                equipo2=eq2,
                fase="Semifinales",
                ronda=i
            )
            self.partidos_eliminatorias["Semifinales"].append(partido)
        self.fase_actual = "Semifinales"
        return self.partidos_eliminatorias["Semifinales"]
    def generar_final_y_tercer_lugar(self):
        semis = self.partidos_eliminatorias["Semifinales"]
        if not all(p.estado == "Finalizado" for p in semis):
            raise ValueError("Todos los partidos de semifinales deben estar finalizados")
        ganadores = [p.ganador for p in semis if p.ganador]
        perdedores = []
        for p in semis:
            if p.ganador == p.equipo1:
                perdedores.append(p.equipo2)
            else:
                perdedores.append(p.equipo1)
        if len(ganadores) < 2:
            raise ValueError("Se necesitan 2 ganadores de semifinales")
        partido_final = PartidoEliminatoria(
            id_partido="FIN",
            equipo1=ganadores[0],
            equipo2=ganadores[1],
            fase="Final",
            ronda=1
        )
        self.partidos_eliminatorias["Final"] = [partido_final]
        if len(perdedores) >= 2:
            partido_tercer = PartidoEliminatoria(
                id_partido="3ER",
                equipo1=perdedores[0],
                equipo2=perdedores[1],
                fase="Tercer Lugar",
                ronda=1
            )
            self.partidos_eliminatorias["Tercer Lugar"] = [partido_tercer]
        self.fase_actual = "Final"
        return self.partidos_eliminatorias["Final"], self.partidos_eliminatorias["Tercer Lugar"]
    def actualizar_resultado_eliminatoria(self, fase, id_partido, goles1, goles2):
        if fase not in self.partidos_eliminatorias:
            return False
        for partido in self.partidos_eliminatorias[fase]:
            if partido.id_partido == id_partido:
                partido.registrar_resultado(goles1, goles2)
                if fase == "Final":
                    self.campeon = partido.ganador
                    self.subcampeon = partido.equipo2 if partido.ganador == partido.equipo1 else partido.equipo1
                if fase == "Tercer Lugar":
                    self.tercer_lugar = partido.ganador
                return True
        return False
    def obtener_estadisticas(self):
        total_partidos = sum(len(partidos) for partidos in self.partidos_eliminatorias.values())
        partidos_jugados = sum(
            1 for fase in self.partidos_eliminatorias.values()
            for partido in fase if partido.estado == "Finalizado"
        )
        total_goles = sum(
            (p.goles_equipo1 or 0) + (p.goles_equipo2 or 0)
            for fase in self.partidos_eliminatorias.values()
            for p in fase if p.estado == "Finalizado"
        )
        equipos_clasificados = len(self.equipos_clasificados)
        equipos_eliminados = equipos_clasificados - len([
            p.ganador for fase in self.partidos_eliminatorias.values()
            for p in fase if p.ganador
        ]) if equipos_clasificados > 0 else 0
        return {
            "total_partidos": total_partidos,
            "partidos_jugados": partidos_jugados,
            "partidos_pendientes": total_partidos - partidos_jugados,
            "total_goles": total_goles,
            "equipos_participantes": len(self.equipos),
            "equipos_clasificados": equipos_clasificados,
            "equipos_eliminados": equipos_eliminados
        }
class DialogEliminatorias(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogEliminatorias()
        self.ui.setupUi(self)
        self.gestor = GestorTorneo()
        self.cargar_datos_ejemplo()
        self.conectar_senales()
        self.configurar_tablas()
        self.actualizar_tabla_clasificacion()
    def conectar_senales(self):
        self.ui.btnActualizarClasificacion.clicked.connect(self.actualizar_clasificacion)
        self.ui.btnGenerarEliminatorias.clicked.connect(self.generar_eliminatorias)
        self.ui.btnExportarClasificacion.clicked.connect(self.exportar_clasificacion)
        self.ui.cmbFiltroGrupo.currentTextChanged.connect(self.filtrar_por_grupo)
        self.ui.cmbFaseActual.currentTextChanged.connect(self.cambiar_vista_fase)
    def configurar_tablas(self):
        self.ui.tableClasificacion.setColumnWidth(0, 50)
        self.ui.tableClasificacion.setColumnWidth(1, 150)
        self.ui.tableClasificacion.setColumnWidth(2, 70)
        self.ui.tableClasificacion.setColumnWidth(3, 50)
        self.ui.tableClasificacion.setColumnWidth(4, 50)
        self.ui.tableClasificacion.setColumnWidth(5, 50)
        self.ui.tableClasificacion.setColumnWidth(6, 50)
        self.ui.tableClasificacion.setColumnWidth(7, 50)
        self.ui.tableClasificacion.setColumnWidth(8, 50)
        self.ui.tableClasificacion.setColumnWidth(9, 50)
        self.ui.tableClasificacion.setColumnWidth(10, 60)
    def cargar_datos_ejemplo(self):
        equipos_ejemplo = [
            ("Los Tigres", "1º ESO A", 6, 5, 1, 0, 15, 3),
            ("Águilas FC", "1º ESO B", 6, 4, 1, 1, 12, 5),
            ("Leones Dorados", "2º ESO A", 6, 3, 2, 1, 10, 6),
            ("Panteras Negras", "2º ESO B", 6, 2, 1, 3, 8, 10),
            ("Dragones Rojos", "3º ESO A", 6, 5, 0, 1, 18, 4),
            ("Halcones Azules", "3º ESO B", 6, 4, 2, 0, 14, 6),
            ("Lobos Grises", "4º ESO A", 6, 3, 1, 2, 11, 9),
            ("Fénix Dorado", "4º ESO B", 6, 2, 2, 2, 9, 10),
        ]
        for nombre, grupo, pj, pg, pe, pp, gf, gc in equipos_ejemplo:
            equipo = Equipo(nombre, grupo)
            equipo.partidos_jugados = pj
            equipo.partidos_ganados = pg
            equipo.partidos_empatados = pe
            equipo.partidos_perdidos = pp
            equipo.goles_favor = gf
            equipo.goles_contra = gc
            equipo.puntos = (pg * 3) + pe
            self.gestor.equipos[nombre] = equipo
        self.gestor.actualizar_clasificacion()
    def actualizar_tabla_clasificacion(self):
        self.ui.tableClasificacion.setRowCount(0)
        for pos, equipo in enumerate(self.gestor.clasificacion, 1):
            row = self.ui.tableClasificacion.rowCount()
            self.ui.tableClasificacion.insertRow(row)
            self.ui.tableClasificacion.setItem(row, 0, QTableWidgetItem(str(pos)))
            self.ui.tableClasificacion.setItem(row, 1, QTableWidgetItem(equipo.nombre))
            self.ui.tableClasificacion.setItem(row, 2, QTableWidgetItem(equipo.grupo))
            self.ui.tableClasificacion.setItem(row, 3, QTableWidgetItem(str(equipo.partidos_jugados)))
            self.ui.tableClasificacion.setItem(row, 4, QTableWidgetItem(str(equipo.partidos_ganados)))
            self.ui.tableClasificacion.setItem(row, 5, QTableWidgetItem(str(equipo.partidos_empatados)))
            self.ui.tableClasificacion.setItem(row, 6, QTableWidgetItem(str(equipo.partidos_perdidos)))
            self.ui.tableClasificacion.setItem(row, 7, QTableWidgetItem(str(equipo.goles_favor)))
            self.ui.tableClasificacion.setItem(row, 8, QTableWidgetItem(str(equipo.goles_contra)))
            self.ui.tableClasificacion.setItem(row, 9, QTableWidgetItem(str(equipo.diferencia_goles)))
            item_puntos = QTableWidgetItem(str(equipo.puntos))
            item_puntos.setFont(QFont("Arial", 10, QFont.Bold))
            self.ui.tableClasificacion.setItem(row, 10, item_puntos)
            if pos <= 8:
                estado = " Clasificado"
                color = QColor(147, 218, 151)
            else:
                estado = " Eliminado"
                color = QColor(255, 200, 200)
            item_estado = QTableWidgetItem(estado)
            item_estado.setBackground(QBrush(color))
            self.ui.tableClasificacion.setItem(row, 11, item_estado)
        clasificados = min(8, len(self.gestor.clasificacion))
        self.ui.lblClasificados.setText(f"Clasificados a Eliminatorias: {clasificados}")
    def actualizar_clasificacion(self):
        self.gestor.actualizar_clasificacion()
        self.actualizar_tabla_clasificacion()
        QMessageBox.information(self, "Actualizado", "Tabla de clasificación actualizada correctamente")
    def filtrar_por_grupo(self, grupo):
        if grupo == "Todos los grupos":
            for i in range(self.ui.tableClasificacion.rowCount()):
                self.ui.tableClasificacion.setRowHidden(i, False)
        else:
            grupo_letra = grupo.split()[-1]
            for i in range(self.ui.tableClasificacion.rowCount()):
                item_grupo = self.ui.tableClasificacion.item(i, 2)
                if item_grupo:
                    self.ui.tableClasificacion.setRowHidden(i, item_grupo.text() != grupo_letra)
    def generar_eliminatorias(self):
        try:
            clasificados = self.gestor.obtener_equipos_clasificados(8)
            if len(clasificados) < 8:
                QMessageBox.warning(
                    self,
                    "Equipos insuficientes",
                    f"Se necesitan 8 equipos clasificados. Actualmente hay {len(clasificados)}"
                )
                return
            partidos = self.gestor.generar_cuartos_final()
            self.ui.tabWidget.setCurrentIndex(1)
            self.mostrar_cuadro_eliminatorias()
            QMessageBox.information(
                self,
                "Eliminatorias Generadas",
                f"Se han generado {len(partidos)} partidos de Cuartos de Final.\n\n"
                f"Equipos clasificados:\n" + "\n".join(f"{i+1}. {eq}" for i, eq in enumerate(clasificados))
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al generar eliminatorias: {str(e)}")
    def mostrar_cuadro_eliminatorias(self):
        fase = self.ui.cmbFaseActual.currentText()
        if fase not in self.gestor.partidos_eliminatorias:
            return
        partidos = self.gestor.partidos_eliminatorias[fase]
        if not partidos:
            self.ui.lblInfoCuadro.setText(
                f"No hay partidos generados para {fase}.\n\n"
                "Genera las eliminatorias desde la pestaña de Clasificación."
            )
            return
        frame = self.ui.frameCuadro
        layout = frame.layout()
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        lbl_titulo = QLabel(f"{fase}")
        lbl_titulo.setStyleSheet("""
            font-size: 18pt;
            font-weight: bold;
            color: rgb(1, 107, 97);
            padding: 15px;
        """)
        lbl_titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl_titulo)
        for i, partido in enumerate(partidos, 1):
            partido_widget = self.crear_widget_partido(partido)
            layout.addWidget(partido_widget)
        layout.addStretch()
    def crear_widget_partido(self, partido):
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: rgb(147, 218, 151);
                border: 3px solid rgb(1, 107, 97);
                border-radius: 10px;
                padding: 15px;
                margin: 5px;
            }
        """)
        layout = QVBoxLayout(frame)
        lbl_id = QLabel(f"Partido {partido.id_partido}")
        lbl_id.setStyleSheet("""
            font-size: 12pt;
            font-weight: bold;
            color: rgb(1, 107, 97);
        """)
        lbl_id.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl_id)
        h_layout = QHBoxLayout()
        lbl_eq1 = QLabel(partido.equipo1)
        lbl_eq1.setStyleSheet("""
            font-size: 14pt;
            font-weight: bold;
            color: rgb(1, 107, 97);
            padding: 5px;
        """)
        lbl_eq1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        h_layout.addWidget(lbl_eq1, 2)
        lbl_resultado = QLabel(partido.get_resultado_texto())
        lbl_resultado.setStyleSheet("""
            font-size: 18pt;
            font-weight: bold;
            color: white;
            background-color: rgb(1, 107, 97);
            padding: 10px 20px;
            border-radius: 8px;
        """)
        lbl_resultado.setAlignment(Qt.AlignCenter)
        h_layout.addWidget(lbl_resultado, 1)
        lbl_eq2 = QLabel(partido.equipo2)
        lbl_eq2.setStyleSheet("""
            font-size: 14pt;
            font-weight: bold;
            color: rgb(1, 107, 97);
            padding: 5px;
        """)
        lbl_eq2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        h_layout.addWidget(lbl_eq2, 2)
        layout.addLayout(h_layout)
        lbl_estado = QLabel(f"Estado: {partido.estado}")
        if partido.estado == "Finalizado":
            lbl_estado.setStyleSheet("color: rgb(1, 107, 97); font-weight: bold;")
        else:
            lbl_estado.setStyleSheet("color: white; font-weight: bold;")
        lbl_estado.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl_estado)
        if partido.ganador:
            lbl_ganador = QLabel(f" Ganador: {partido.ganador}")
            lbl_ganador.setStyleSheet("""
                font-size: 12pt;
                font-weight: bold;
                color: white;
                background-color: rgb(1, 107, 97);
                padding: 8px;
                border-radius: 5px;
                margin-top: 5px;
            """)
            lbl_ganador.setAlignment(Qt.AlignCenter)
            layout.addWidget(lbl_ganador)
        btn_editar = QPushButton("Editar Resultado")
        btn_editar.setStyleSheet("""
            QPushButton {
                background-color: rgb(1, 107, 97);
                color: white;
                font-weight: bold;
                padding: 8px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: rgb(113, 177, 129);
            }
        """)
        btn_editar.clicked.connect(lambda: self._editar_resultado_partido(partido))
        layout.addWidget(btn_editar)
        return frame
    def _editar_resultado_partido(self, partido):
        dialogo = QDialog(self)
        dialogo.setWindowTitle(f"Editar Resultado: {partido.equipo1} vs {partido.equipo2}")
        dialogo.setGeometry(300, 300, 500, 300)
        layout = QVBoxLayout(dialogo)
        lbl_titulo = QLabel(f"{partido.equipo1} vs {partido.equipo2}")
        lbl_titulo.setStyleSheet("""
            font-size: 16pt;
            font-weight: bold;
            color: rgb(1, 107, 97);
            padding: 10px;
        """)
        lbl_titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl_titulo)
        frame_inputs = QFrame()
        frame_inputs.setStyleSheet("""
            QFrame {
                background-color: rgb(147, 218, 151);
                border: 2px solid rgb(1, 107, 97);
                border-radius: 5px;
                padding: 10px;
            }
        """)
        h_layout = QHBoxLayout(frame_inputs)
        v_layout1 = QVBoxLayout()
        lbl_eq1 = QLabel(partido.equipo1)
        lbl_eq1.setStyleSheet("font-weight: bold; color: rgb(1, 107, 97);")
        lbl_eq1.setAlignment(Qt.AlignCenter)
        v_layout1.addWidget(lbl_eq1)
        spin1 = QSpinBox()
        spin1.setValue(partido.goles_equipo1 if partido.goles_equipo1 is not None else 0)
        spin1.setMinimum(0)
        spin1.setMaximum(20)
        spin1.setStyleSheet("""
            QSpinBox {
                font-size: 24pt;
                font-weight: bold;
                background-color: white;
                border: 2px solid rgb(1, 107, 97);
                border-radius: 5px;
                padding: 5px;
                color: rgb(1, 107, 97);
            }
        """)
        v_layout1.addWidget(spin1)
        h_layout.addLayout(v_layout1)
        lbl_vs = QLabel("VS")
        lbl_vs.setStyleSheet("""
            font-size: 18pt;
            font-weight: bold;
            color: white;
            padding: 20px;
        """)
        lbl_vs.setAlignment(Qt.AlignCenter)
        h_layout.addWidget(lbl_vs)
        v_layout2 = QVBoxLayout()
        lbl_eq2 = QLabel(partido.equipo2)
        lbl_eq2.setStyleSheet("font-weight: bold; color: rgb(1, 107, 97);")
        lbl_eq2.setAlignment(Qt.AlignCenter)
        v_layout2.addWidget(lbl_eq2)
        spin2 = QSpinBox()
        spin2.setValue(partido.goles_equipo2 if partido.goles_equipo2 is not None else 0)
        spin2.setMinimum(0)
        spin2.setMaximum(20)
        spin2.setStyleSheet("""
            QSpinBox {
                font-size: 24pt;
                font-weight: bold;
                background-color: white;
                border: 2px solid rgb(1, 107, 97);
                border-radius: 5px;
                padding: 5px;
                color: rgb(1, 107, 97);
            }
        """)
        v_layout2.addWidget(spin2)
        h_layout.addLayout(v_layout2)
        layout.addWidget(frame_inputs)
        h_layout_botones = QHBoxLayout()
        btn_guardar = QPushButton("Guardar Resultado")
        btn_guardar.setStyleSheet("""
            QPushButton {
                background-color: rgb(1, 107, 97);
                color: white;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: rgb(113, 177, 129);
            }
        """)
        h_layout_botones.addWidget(btn_guardar)
        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.setStyleSheet("""
            QPushButton {
                background-color: rgb(200, 200, 200);
                color: black;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: rgb(230, 230, 230);
            }
        """)
        h_layout_botones.addWidget(btn_cancelar)
        layout.addLayout(h_layout_botones)
        btn_guardar.clicked.connect(lambda: self._guardar_resultado(partido, spin1.value(), spin2.value(), dialogo))
        btn_cancelar.clicked.connect(dialogo.reject)
        dialogo.exec()
    def _guardar_resultado(self, partido, goles1, goles2, dialogo):
        partido.goles_equipo1 = goles1
        partido.goles_equipo2 = goles2
        partido.estado = "Finalizado"
        if goles1 > goles2:
            partido.ganador = partido.equipo1
        elif goles2 > goles1:
            partido.ganador = partido.equipo2
        else:
            partido.ganador = None
        dialogo.accept()
        fase_actual = self.ui.cmbFaseActual.currentText()
        self.mostrar_cuadro_eliminatorias()
        self._verificar_fase_completa(fase_actual)
    def _verificar_fase_completa(self, fase):
        partidos_fase = self.gestor.partidos_eliminatorias.get(fase, [])
        if not partidos_fase:
            return
        si_completa = all(p.ganador and p.estado == "Finalizado" for p in partidos_fase)
        if not si_completa:
            return
        fases = ["Cuartos de Final", "Semifinales", "Final"]
        indice_actual = fases.index(fase) if fase in fases else -1
        if indice_actual == -1 or indice_actual >= len(fases) - 1:
            ganador = max(partidos_fase, key=lambda p: (p.ganador == p.ganador)).ganador
            QMessageBox.information(
                self,
                "¡Torneo Finalizado!",
                f"¡Felicidades! El campeón del torneo es:\n\n{ganador}"
            )
            return
        siguiente_fase = fases[indice_actual + 1]
        self._generar_siguiente_fase(fase, siguiente_fase)
        self.ui.cmbFaseActual.setCurrentText(siguiente_fase)
    def _generar_siguiente_fase(self, fase_actual, siguiente_fase):
        partidos_actual = self.gestor.partidos_eliminatorias.get(fase_actual, [])
        ganadores = [p.ganador for p in partidos_actual if p.ganador]
        if not ganadores:
            return
        nuevos_partidos = []
        for i in range(0, len(ganadores), 2):
            if i + 1 < len(ganadores):
                nuevo_partido = PartidoEliminatoria(
                    id_partido=len(nuevos_partidos) + 1,
                    equipo1=ganadores[i],
                    equipo2=ganadores[i + 1],
                    fase=siguiente_fase,
                    ronda=i // 2
                )
                nuevos_partidos.append(nuevo_partido)
        self.gestor.partidos_eliminatorias[siguiente_fase] = nuevos_partidos
        QMessageBox.information(
            self,
            f"{siguiente_fase}",
            f"Se han generado {len(nuevos_partidos)} partidos de {siguiente_fase}"
        )
    def actualizar_resultados(self):
        fase = self.ui.cmbFaseActual.currentText()
        if fase not in self.gestor.partidos_eliminatorias:
            QMessageBox.warning(self, "Sin partidos", "No hay partidos en esta fase")
            return
        partidos = self.gestor.partidos_eliminatorias[fase]
        if not partidos:
            QMessageBox.warning(self, "Sin partidos", "No hay partidos generados para esta fase")
            return
        from PySide6.QtWidgets import QInputDialog
        partidos_texto = [f"{p.id_partido}: {p.equipo1} vs {p.equipo2}" for p in partidos]
        partido_seleccionado, ok = QInputDialog.getItem(
            self,
            "Seleccionar Partido",
            "Selecciona el partido a actualizar:",
            partidos_texto,
            0,
            False
        )
        if not ok:
            return
        id_partido = partido_seleccionado.split(":")[0]
        partido = next((p for p in partidos if p.id_partido == id_partido), None)
        if not partido:
            return
        dialogo = QDialog(self)
        dialogo.setWindowTitle(f"Actualizar Resultado - {id_partido}")
        dialogo.setStyleSheet("background-color: rgb(113, 177, 129);")
        dialogo.setMinimumWidth(450)
        layout = QVBoxLayout(dialogo)
        lbl_titulo = QLabel(f"{partido.equipo1} vs {partido.equipo2}")
        lbl_titulo.setStyleSheet("""
            font-size: 14pt;
            font-weight: bold;
            color: white;
            padding: 10px;
        """)
        lbl_titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl_titulo)
        frame_inputs = QFrame()
        frame_inputs.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        h_layout = QHBoxLayout(frame_inputs)
        v_layout1 = QVBoxLayout()
        lbl_eq1 = QLabel(partido.equipo1)
        lbl_eq1.setStyleSheet("font-weight: bold; color: rgb(1, 107, 97); font-size: 11pt;")
        lbl_eq1.setAlignment(Qt.AlignCenter)
        spin1 = QSpinBox()
        spin1.setRange(0, 20)
        spin1.setStyleSheet("""
            QSpinBox {
                font-size: 16pt;
                font-weight: bold;
                padding: 10px;
                background-color: rgb(147, 218, 151);
                color: rgb(1, 107, 97);
                border: 2px solid rgb(1, 107, 97);
                border-radius: 5px;
            }
        """)
        v_layout1.addWidget(lbl_eq1)
        v_layout1.addWidget(spin1)
        h_layout.addLayout(v_layout1)
        lbl_vs = QLabel("VS")
        lbl_vs.setStyleSheet("""
            font-size: 16pt;
            font-weight: bold;
            color: rgb(1, 107, 97);
        """)
        lbl_vs.setAlignment(Qt.AlignCenter)
        h_layout.addWidget(lbl_vs)
        v_layout2 = QVBoxLayout()
        lbl_eq2 = QLabel(partido.equipo2)
        lbl_eq2.setStyleSheet("font-weight: bold; color: rgb(1, 107, 97); font-size: 11pt;")
        lbl_eq2.setAlignment(Qt.AlignCenter)
        spin2 = QSpinBox()
        spin2.setRange(0, 20)
        spin2.setStyleSheet("""
            QSpinBox {
                font-size: 16pt;
                font-weight: bold;
                padding: 10px;
                background-color: rgb(147, 218, 151);
                color: rgb(1, 107, 97);
                border: 2px solid rgb(1, 107, 97);
                border-radius: 5px;
            }
        """)
        v_layout2.addWidget(lbl_eq2)
        v_layout2.addWidget(spin2)
        h_layout.addLayout(v_layout2)
        layout.addWidget(frame_inputs)
        from PyQt5.QtWidgets import QDialogButtonBox
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.setStyleSheet("""
            QPushButton {
                background-color: rgb(1, 107, 97);
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: rgb(113, 177, 129);
            }
        """)
        botones.accepted.connect(dialogo.accept)
        botones.rejected.connect(dialogo.reject)
        layout.addWidget(botones)
        if dialogo.exec_() == QDialog.Accepted:
            goles1 = spin1.value()
            goles2 = spin2.value()
            if self.gestor.actualizar_resultado_eliminatoria(fase, id_partido, goles1, goles2):
                self.mostrar_cuadro_eliminatorias()
                self.actualizar_estadisticas()
                ganador = partido.ganador if partido.ganador else "Empate (se requieren penales)"
                QMessageBox.information(
                    self,
                    "Resultado Actualizado",
                    f"{partido.equipo1} {goles1} - {goles2} {partido.equipo2}\n\n"
                    f"Ganador: {ganador}"
                )
    def avanzar_fase(self):
        try:
            fase_actual = self.ui.cmbFaseActual.currentText()
            partidos = self.gestor.partidos_eliminatorias.get(fase_actual, [])
            si_todos_finalizados = all(p.estado == "Finalizado" for p in partidos)
            if not si_todos_finalizados:
                QMessageBox.warning(
                    self,
                    "Partidos pendientes",
                    f"Todos los partidos de {fase_actual} deben estar finalizados antes de avanzar"
                )
                return
            si_todos_con_ganador = all(p.ganador for p in partidos)
            if not si_todos_con_ganador:
                QMessageBox.warning(
                    self,
                    "Ganadores pendientes",
                    f"Se necesita determinar un ganador en todos los partidos de {fase_actual}"
                )
                return
            fases = ["Cuartos de Final", "Semifinales", "Final"]
            indice_actual = fases.index(fase_actual) if fase_actual in fases else -1
            if indice_actual == -1 or indice_actual >= len(fases) - 1:
                QMessageBox.information(
                    self,
                    "Torneo Finalizado",
                    "¡El torneo ha finalizado! No hay más fases por jugar."
                )
                return
            siguiente_fase = fases[indice_actual + 1]
            self._generar_siguiente_fase(fase_actual, siguiente_fase)
            self.ui.cmbFaseActual.setCurrentText(siguiente_fase)
            self.mostrar_cuadro_eliminatorias()
            QMessageBox.information(
                self,
                f"{siguiente_fase} Generadas",
                f"Los partidos de {siguiente_fase} han sido generados automáticamente"
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error al avanzar de fase: {str(e)}"
            )
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
    def cambiar_vista_fase(self, fase):
        self.mostrar_cuadro_eliminatorias()
    def ver_detalle(self):
        fase = self.ui.cmbFaseActual.currentText()
        partidos = self.gestor.partidos_eliminatorias.get(fase, [])
        if not partidos:
            QMessageBox.information(self, "Sin datos", "No hay partidos en esta fase")
            return
        detalle = f"Detalles de {fase}\n{'='*50}\n\n"
        for p in partidos:
            detalle += f"Partido {p.id_partido}:\n"
            detalle += f"  {p.equipo1} vs {p.equipo2}\n"
            detalle += f"  Resultado: {p.get_resultado_texto()}\n"
            detalle += f"  Estado: {p.estado}\n"
            if p.ganador:
                detalle += f"  Ganador: {p.ganador}\n"
            detalle += "\n"
        QMessageBox.information(self, "Detalles de Partidos", detalle)
    def actualizar_estadisticas(self):
        pass
    def actualizar_top_equipos(self):
        pass
    def exportar_clasificacion(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Exportar Clasificación",
            "clasificacion.csv",
            "CSV Files (*.csv)"
        )
        if filename:
            try:
                with open(filename, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        "Posición", "Equipo", "Grupo", "PJ", "PG", "PE", "PP",
                        "GF", "GC", "DG", "Puntos"
                    ])
                    for pos, equipo in enumerate(self.gestor.clasificacion, 1):
                        writer.writerow([
                            pos, equipo.nombre, equipo.grupo,
                            equipo.partidos_jugados, equipo.partidos_ganados,
                            equipo.partidos_empatados, equipo.partidos_perdidos,
                            equipo.goles_favor, equipo.goles_contra,
                            equipo.diferencia_goles, equipo.puntos
                        ])
                QMessageBox.information(
                    self,
                    "Exportación Exitosa",
                    f"Clasificación exportada a:\n{filename}"
                )
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al exportar: {str(e)}")
def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    dialogo = DialogEliminatorias()
    dialogo.exec_()
if __name__ == '__main__':
    main()
