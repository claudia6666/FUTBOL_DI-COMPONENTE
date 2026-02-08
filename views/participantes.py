from PySide6.QtWidgets import QDialog, QTableWidgetItem, QComboBox, QVBoxLayout, QLabel
from PySide6.QtSql import QSqlQuery
from widgets.ui_participantes import Ui_DialogParticipantes
from views.form_jugador import FormJugador
from views.form_arbitro import FormArbitro
try:
    from modules.reloj_digital.views.AppReloj import TestWindow
except Exception:
    TestWindow = None
from views.form_equipo import FormEquipo
from models.globals import get_db_connection
class Participantes(QDialog):
    def __init__(self, calendario_window=None):
        super().__init__()
        self.ui = Ui_DialogParticipantes()
        self.ui.setupUi(self)
        self.form_jugador_window = FormJugador()
        self.form_arbitro_window = FormArbitro()
        self.form_equipo_window = FormEquipo()
        if TestWindow is not None:
            try:
                self.match_window = TestWindow()
            except Exception:
                self.match_window = None
        else:
            self.match_window = None
        self.calendario_window = calendario_window
        self.equipo_filtro_id = None
        self.ui.btnNuevoJugador.clicked.connect(self._abrir_formulario_jugador)
        self.ui.btnEditarJugador.clicked.connect(self._editar_jugador_seleccionado)
        self.ui.btnEliminarJugador.clicked.connect(self._eliminar_jugador_seleccionado)
        self.ui.btnNuevoArbitro.clicked.connect(self._abrir_formulario_arbitro)
        self.ui.btnEditarArbitro.clicked.connect(self._editar_arbitro_seleccionado)
        self.ui.btnEliminarArbitro.clicked.connect(self._eliminar_arbitro_seleccionado)
        self.ui.btnAsignarPartido.clicked.connect(self._asignar_arbitro_a_partido)
        try:
            pass
        except Exception:
            pass
        self.ui.txtBuscarJugador.textChanged.connect(self._filtrar_jugadores_por_nombre)
        self.ui.txtBuscarArbitro.textChanged.connect(self._filtrar_arbitros_por_nombre)
        self.ui.btnExportarJugadores.clicked.connect(self._exportar_jugadores_csv)
        self._agregar_filtro_equipo()
        self._cargar_jugadores()
        self._cargar_arbitros()
        print("Gestión de participantes lista")
    def _agregar_filtro_equipo(self):
        try:
            cmb_equipo = self.findChild(QComboBox, "cmbFiltroEquipo")
            if cmb_equipo:
                print("[OK] cmbFiltroEquipo encontrado")
                self._cargar_equipos_en_combo(cmb_equipo)
                cmb_equipo.currentIndexChanged.connect(self._aplicar_filtro_equipo)
                print("[OK] Filtro de equipos conectado")
            else:
                print("[ERROR] cmbFiltroEquipo NO encontrado - el filtro no funcionara")
        except Exception as e:
            print(f"[ERROR] Error al agregar filtro: {e}")
            import traceback
            traceback.print_exc()
    def _abrir_formulario_jugador(self):
        try:
            self.form_jugador_window.dialog.finished.disconnect()
        except RuntimeError:
            pass
        self.form_jugador_window.dialog.finished.connect(self._cargar_jugadores)
        self.form_jugador_window.show()
    def _editar_jugador_seleccionado(self):
        try:
            table = self.ui.tableJugadores
            selected_row = table.currentRow()
            if selected_row < 0:
                from PySide6.QtWidgets import QMessageBox
                QMessageBox.warning(self, "Error", "Por favor selecciona un jugador para editar")
                return
            jugador_id = int(table.item(selected_row, 0).text())
            try:
                self.form_jugador_window.dialog.finished.disconnect()
            except RuntimeError:
                pass
            self.form_jugador_window.dialog.finished.connect(self._cargar_jugadores)
            self.form_jugador_window.cargar_para_editar(jugador_id)
            self.form_jugador_window.show()
        except Exception as e:
            print(f"[ERROR] Error al editar jugador: {e}")
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Error", f"Error al editar: {e}")
    def _eliminar_jugador_seleccionado(self):
        try:
            from PySide6.QtWidgets import QMessageBox
            table = self.ui.tableJugadores
            selected_row = table.currentRow()
            if selected_row < 0:
                QMessageBox.warning(self, "Error", "Por favor selecciona un jugador para eliminar")
                return
            jugador_id = int(table.item(selected_row, 0).text())
            jugador_nombre = table.item(selected_row, 1).text()
            respuesta = QMessageBox.question(
                self,
                "Confirmar eliminación",
                f"¿Estás seguro de que deseas eliminar a {jugador_nombre}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if respuesta != QMessageBox.StandardButton.Yes:
                return
            db = get_db_connection()
            query = QSqlQuery(db)
            query.prepare("DELETE FROM participantes WHERE id = ? AND tipo_participante = 'Jugador'")
            query.addBindValue(jugador_id)
            if query.exec():
                QMessageBox.information(self, "Éxito", f"Jugador {jugador_nombre} eliminado correctamente")
                self._cargar_jugadores()
            else:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar el jugador: {query.lastError().text()}")
        except Exception as e:
            print(f"[ERROR] Error al eliminar jugador: {e}")
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Error", f"Error al eliminar: {e}")
    def _filtrar_jugadores_por_nombre(self):
        try:
            txt_buscar = self.ui.txtBuscarJugador.text().lower()
            table = self.ui.tableJugadores
            for row in range(table.rowCount()):
                nombre_item = table.item(row, 1)
                if nombre_item:
                    nombre = nombre_item.text().lower()
                    table.setRowHidden(row, txt_buscar not in nombre)
        except Exception as e:
            print(f"[ERROR] Error al filtrar jugadores: {e}")
    def _filtrar_arbitros_por_nombre(self):
        try:
            txt_buscar = self.ui.txtBuscarArbitro.text().lower()
            table = self.ui.tableArbitros
            for row in range(table.rowCount()):
                nombre_item = table.item(row, 1)
                if nombre_item:
                    nombre = nombre_item.text().lower()
                    table.setRowHidden(row, txt_buscar not in nombre)
        except Exception as e:
            print(f"[ERROR] Error al filtrar árbitros: {e}")
    def _editar_arbitro_seleccionado(self):
        try:
            table = self.ui.tableArbitros
            selected_row = table.currentRow()
            if selected_row < 0:
                from PySide6.QtWidgets import QMessageBox
                QMessageBox.warning(self, "Error", "Por favor selecciona un árbitro para editar")
                return
            arbitro_id = int(table.item(selected_row, 0).text())
            try:
                self.form_arbitro_window.dialog.finished.disconnect()
            except RuntimeError:
                pass
            self.form_arbitro_window.dialog.finished.connect(self._cargar_arbitros)
            self.form_arbitro_window.cargar_para_editar(arbitro_id)
            self.form_arbitro_window.show()
        except Exception as e:
            print(f"[ERROR] Error al editar árbitro: {e}")
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Error", f"Error al editar: {e}")
    def _eliminar_arbitro_seleccionado(self):
        try:
            from PySide6.QtWidgets import QMessageBox
            table = self.ui.tableArbitros
            selected_row = table.currentRow()
            if selected_row < 0:
                QMessageBox.warning(self, "Error", "Por favor selecciona un árbitro para eliminar")
                return
            arbitro_id = int(table.item(selected_row, 0).text())
            arbitro_nombre = table.item(selected_row, 1).text()
            respuesta = QMessageBox.question(
                self,
                "Confirmar eliminación",
                f"¿Estás seguro de que deseas eliminar a {arbitro_nombre}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if respuesta != QMessageBox.StandardButton.Yes:
                return
            db = get_db_connection()
            query = QSqlQuery(db)
            query.prepare("DELETE FROM participantes WHERE id = ? AND tipo_participante = 'Arbitro'")
            query.addBindValue(arbitro_id)
            if query.exec():
                QMessageBox.information(self, "Éxito", f"Árbitro {arbitro_nombre} eliminado correctamente")
                self._cargar_arbitros()
            else:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar el árbitro: {query.lastError().text()}")
        except Exception as e:
            print(f"[ERROR] Error al eliminar árbitro: {e}")
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Error", f"Error al eliminar: {e}")
    def _abrir_formulario_arbitro(self):
        try:
            self.form_arbitro_window.dialog.finished.disconnect()
        except RuntimeError:
            pass
        self.form_arbitro_window.dialog.finished.connect(self._cargar_arbitros)
        self.form_arbitro_window.show()
    def _asignar_arbitro_a_partido(self):
        try:
            table = self.ui.tableArbitros
            selected_row = table.currentRow()
            from PySide6.QtWidgets import QMessageBox
            if selected_row < 0:
                QMessageBox.warning(self, "Error", "Por favor selecciona un árbitro para asignar a un partido")
                return
            arbitro_id = int(table.item(selected_row, 0).text())
            try:
                if self.match_window:
                    self.match_window.show()
                else:
                    QMessageBox.critical(self, "Error", "La gestión de partidos no está disponible")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo abrir la gestión: {e}")
        except Exception as e:
            print(f"Error en asignar árbitro a partido: {e}")
    def _recargar_calendario(self):
        if self.calendario_window:
            try:
                if hasattr(self.calendario_window, '_cargar_partidos'):
                    self.calendario_window._cargar_partidos()
                elif hasattr(self.calendario_window, 'cargar_partidos'):
                    self.calendario_window.cargar_partidos()
                else:
                    self.calendario_window.show()
                print("[OK] Calendario recargado tras asignar árbitro")
            except Exception as e:
                print(f"Advertencia: No se pudo recargar calendario: {e}")
    def _cargar_equipos_en_combo(self, cmb):
        try:
            db = get_db_connection()
            query = QSqlQuery(db)
            query.exec("SELECT id, nombre FROM equipos ORDER BY nombre")
            cmb.clear()
            cmb.addItem("- Todos los equipos -", None)
            while query.next():
                equipo_id = query.value(0)
                equipo_nombre = query.value(1)
                cmb.addItem(equipo_nombre, equipo_id)
        except Exception as e:
            print(f"Error al cargar equipos en combobox: {e}")
    def _aplicar_filtro_equipo(self):
        try:
            cmb_equipo = self.findChild(QComboBox, "cmbFiltroEquipo")
            if cmb_equipo:
                self.equipo_filtro_id = cmb_equipo.currentData()
                self._cargar_jugadores()
        except Exception as e:
            print(f"Error al aplicar filtro: {e}")
    def _cargar_jugadores(self):
        try:
            from PySide6.QtGui import QColor
            db = get_db_connection()
            table = self.ui.tableJugadores
            table.setRowCount(0)
            table.setColumnCount(8)
            table.setHorizontalHeaderLabels(["ID", "Nombre", "Equipo", "Curso", "Posición", "Goles", "T. Amarillas", "T. Rojas"])
            query = QSqlQuery(db)
            if self.equipo_filtro_id is not None:
                query.exec(f"""SELECT p.id, p.nombre, e.nombre, p.curso, p.posicion, p.goles, p.tarjetas_amarillas, p.tarjetas_rojas 
                          FROM participantes p 
                          LEFT JOIN equipos e ON p.equipo_id = e.id 
                          WHERE p.tipo_participante = 'Jugador' AND p.equipo_id = {self.equipo_filtro_id}
                          ORDER BY p.nombre""")
            else:
                query.exec("""SELECT p.id, p.nombre, e.nombre, p.curso, p.posicion, p.goles, p.tarjetas_amarillas, p.tarjetas_rojas 
                          FROM participantes p 
                          LEFT JOIN equipos e ON p.equipo_id = e.id 
                          WHERE p.tipo_participante = 'Jugador'
                          ORDER BY p.nombre""")
            row = 0
            while query.next():
                table.insertRow(row)
                for col in range(8):
                    item = QTableWidgetItem(str(query.value(col)) if query.value(col) else "")
                    item.setForeground(QColor("black"))
                    table.setItem(row, col, item)
                row += 1
        except Exception as e:
            print(f"Error al cargar jugadores: {e}")
    def _cargar_arbitros(self):
        try:
            from PySide6.QtGui import QColor
            db = get_db_connection()
            table = self.ui.tableArbitros
            table.setRowCount(0)
            table.setColumnCount(5)
            table.setHorizontalHeaderLabels(["ID", "Nombre", "Curso", "Fecha Nacimiento", "Fecha Registro"])
            query = QSqlQuery(db)
            query.exec("SELECT id, nombre, curso, fecha_nacimiento, fecha_registro FROM participantes WHERE tipo_participante = 'Arbitro'")
            row = 0
            while query.next():
                table.insertRow(row)
                for col in range(5):
                    item = QTableWidgetItem(str(query.value(col)))
                    item.setForeground(QColor("black"))
                    table.setItem(row, col, item)
                row += 1
        except Exception as e:
            print(f"Error al cargar árbitros: {e}")
    def _exportar_jugadores_csv(self):
        try:
            from PySide6.QtWidgets import QFileDialog, QMessageBox
            import csv
            ruta_archivo, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar como CSV",
                "jugadores.csv",
                "Archivos CSV (*.csv);;Todos los archivos (*)"
            )
            if not ruta_archivo:
                return
            table = self.ui.tableJugadores
            with open(ruta_archivo, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                encabezados = []
                for col in range(table.columnCount()):
                    encabezados.append(table.horizontalHeaderItem(col).text())
                writer.writerow(encabezados)
                for row in range(table.rowCount()):
                    if not table.isRowHidden(row):
                        fila = []
                        for col in range(table.columnCount()):
                            item = table.item(row, col)
                            fila.append(item.text() if item else "")
                        writer.writerow(fila)
            QMessageBox.information(
                self,
                "Éxito",
                f"Datos exportados correctamente a:\n{ruta_archivo}"
            )
            print(f"[OK] Jugadores exportados a {ruta_archivo}")
        except Exception as e:
            print(f"[ERROR] Error al exportar CSV: {e}")
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Error", f"Error al exportar: {e}")
        except Exception as e:
            print(f"Error al cargar árbitros: {e}")
