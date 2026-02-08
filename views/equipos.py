from PySide6.QtWidgets import (QDialog, QTableWidgetItem, QLabel, QLineEdit, QComboBox,
                             QMessageBox, QFileDialog, QVBoxLayout, QPushButton)
from PySide6.QtGui import QColor, QPixmap, QIcon, QBrush, QFont
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlQuery
from widgets.ui_equipos import Ui_DialogEquipos
from views.form_equipo import FormEquipo
from views.form_participante import FormParticipante
from models.globals import get_db_connection
class Equipos(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogEquipos()
        self.ui.setupUi(self)
        self.equipo_seleccionado_id = None
        self.form_equipo_window = FormEquipo()
        self.form_participante_window = FormParticipante()
        self.ui.btnNuevoEquipo.clicked.connect(self._abrir_formulario_equipo)
        self.ui.btnEditarEquipo.clicked.connect(self._editar_equipo_seleccionado)
        self.ui.btnEliminarEquipo.clicked.connect(self._eliminar_equipo_seleccionado)
        self.ui.btnAgregarJugador.clicked.connect(self._abrir_agregar_jugador)
        self.ui.btnQuitarJugador.clicked.connect(self._eliminar_jugador_seleccionado)
        self.ui.tableEquipos.itemSelectionChanged.connect(self._equipo_seleccionado)
        self._cargar_equipos()
        print("Gestion de equipos lista")
    def _abrir_formulario_equipo(self):
        try:
            self.form_equipo_window.dialog.finished.disconnect()
        except RuntimeError:
            pass
        self.form_equipo_window.dialog.finished.connect(self._cargar_equipos)
        self.form_equipo_window.show()
    def _abrir_agregar_jugador(self):
        if not self.equipo_seleccionado_id:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona un equipo primero")
            return
        print(f"[DEBUG] Abriendo formulario para equipo ID: {self.equipo_seleccionado_id}")
        self.form_participante_window.equipo_id = self.equipo_seleccionado_id
        result = self.form_participante_window.dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            self._cargar_jugadores_equipo_por_id(self.equipo_seleccionado_id)
            print(f"[DEBUG] Jugadores recargados para equipo {self.equipo_seleccionado_id}")
        else:
            print("[DEBUG] Dialog cancelado, no se recargaron jugadores")
    def _eliminar_jugador_seleccionado(self):
        list_widget = self.ui.listJugadores
        item_seleccionado = list_widget.currentItem()
        if not item_seleccionado:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona un jugador para eliminar")
            return
        jugador_id = item_seleccionado.data(Qt.UserRole)
        if jugador_id is None:
            QMessageBox.warning(self, "Advertencia", "No se pudo identificar el jugador seleccionado")
            return
        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Estás seguro de que deseas eliminar este jugador?\n\n{item_seleccionado.text()}",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if respuesta == QMessageBox.StandardButton.Yes:
            try:
                db = get_db_connection()
                query = QSqlQuery(db)
                query.prepare("DELETE FROM participantes WHERE id = ? AND tipo_participante = 'Jugador'")
                query.addBindValue(jugador_id)
                if query.exec():
                    QMessageBox.information(self, "Éxito", "Jugador eliminado correctamente")
                    self._cargar_jugadores_equipo_por_id(self.equipo_seleccionado_id)
                    print(f"[OK] Jugador {jugador_id} eliminado")
                else:
                    QMessageBox.critical(self, "Error", f"Error al eliminar el jugador: {query.lastError().text()}")
                    print(f"[ERROR] Error al eliminar jugador: {query.lastError().text()}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error inesperado: {str(e)}")
                print(f"[ERROR] Error inesperado al eliminar jugador: {e}")
                import traceback
                traceback.print_exc()
    def _cargar_equipos(self):
        try:
            db = get_db_connection()
            if db is None:
                print("[ERROR] La conexión a la base de datos no está disponible")
                return
            table = self.ui.tableEquipos
            table.setRowCount(0)
            table.setColumnCount(4)
            table.setHorizontalHeaderLabels(["ID", "Nombre", "Curso", "Color"])
            query = QSqlQuery(db)
            sql = "SELECT id, nombre, curso, color_camiseta FROM equipos ORDER BY nombre"
            if not query.exec(sql):
                print(f"[ERROR] Error en la consulta SQL: {query.lastError().text()}")
                return
            color_map = {
                'naranja': '#FFA500', 'azul': '#0000FF', 'amarillo': '#FFFF00', 
                'negro': '#000000', 'rojo': '#FF0000', 'gris': '#808080', 
                'verde': '#008000', 'oro': '#FFD700', 'purpura': '#800080', 
                'azul cielo': '#87CEEB', 'plata': '#C0C0C0', 'blanco': '#FFFFFF'
            }
            row = 0
            while query.next():
                equipo_id = query.value(0)
                equipo_nombre = query.value(1)
                equipo_curso = query.value(2)
                equipo_color = query.value(3)
                table.insertRow(row)
                item_id = QTableWidgetItem(str(equipo_id))
                table.setItem(row, 0, item_id)
                item_nombre = QTableWidgetItem(equipo_nombre)
                item_nombre.setForeground(QColor("black"))
                table.setItem(row, 1, item_nombre)
                item_curso = QTableWidgetItem(equipo_curso if equipo_curso else "")
                item_curso.setForeground(QColor("black"))
                table.setItem(row, 2, item_curso)
                item_color = QTableWidgetItem("")
                if equipo_color:
                    color_obj = self._parse_color_value(equipo_color, color_map)
                    item_color.setBackground(color_obj)
                    item_color.setText("")
                    r = color_obj.red()
                    g = color_obj.green()
                    b = color_obj.blue()
                    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
                    if luminance < 128:
                        item_color.setForeground(QColor('white'))
                    else:
                        item_color.setForeground(QColor('black'))
                else:
                    item_color.setForeground(QColor("black"))
                table.setItem(row, 3, item_color)
                row += 1
            print(f"[OK] Equipos cargados: {row}")
        except Exception as e:
            print(f"[ERROR] Error al cargar equipos: {e}")
            import traceback
            traceback.print_exc()
    def _parse_color_value(self, value, color_map):
        try:
            sep = None
            if ',' in value:
                sep = ','
            elif ' ' in value:
                sep = ' '
            if sep:
                parts = [p.strip() for p in value.split(sep) if p.strip()]
                if len(parts) >= 3:
                    r = int(parts[0])
                    g = int(parts[1])
                    b = int(parts[2])
                    c = QColor(r, g, b)
                    if c.isValid():
                        return c
        except Exception:
            pass
        c = QColor(value)
        if c.isValid():
            return c
        return QColor('#CCCCCC')
    def _equipo_seleccionado(self):
        selected_items = self.ui.tableEquipos.selectedItems()
        if selected_items:
            fila = self.ui.tableEquipos.row(selected_items[0])
            equipo_id = self.ui.tableEquipos.item(fila, 0).text()
            equipo_nombre = self.ui.tableEquipos.item(fila, 1).text()
            self.equipo_seleccionado_id = int(equipo_id)
            self._cargar_jugadores_equipo()
            try:
                db = get_db_connection()
                query = QSqlQuery(db)
                query.exec(f"SELECT nombre FROM equipos WHERE id = {self.equipo_seleccionado_id}")
                if query.next():
                    print(f"[OK] Equipo seleccionado: ID={self.equipo_seleccionado_id}, Nombre={equipo_nombre}")
            except Exception as e:
                print(f"[ERROR] Error al seleccionar equipo: {e}")
    def _cargar_jugadores_equipo(self):
        if self.equipo_seleccionado_id is None:
            return
        self._cargar_jugadores_equipo_por_id(self.equipo_seleccionado_id)
    def _cargar_jugadores_equipo_por_id(self, equipo_id):
        print(f"[DEBUG] Cargando jugadores para equipo ID: {equipo_id}")
        try:
            db = get_db_connection()
            list_widget = self.ui.listJugadores
            list_widget.clear()
            query = QSqlQuery(db)
            sql = f"""
                SELECT id, nombre, posicion, goles, tarjetas_amarillas, tarjetas_rojas 
                FROM participantes 
                WHERE tipo_participante = 'Jugador' AND equipo_id = {equipo_id}
                ORDER BY nombre
            """
            if not query.exec(sql):
                print(f"[ERROR] Error en la consulta: {query.lastError().text()}")
                return
            jugadores_count = 0
            while query.next():
                jugador_id = query.value(0)
                nombre = query.value(1)
                posicion = query.value(2)
                goles = query.value(3)
                amarillas = query.value(4)
                rojas = query.value(5)
                texto = f"[J] {nombre:<20} | POS: {posicion:<10} | GOLES: {goles} AMARILLAS: {amarillas} ROJAS: {rojas}"
                list_widget.addItem(texto)
                item = list_widget.item(jugadores_count)
                item.setData(Qt.UserRole, jugador_id)
                item.setForeground(QColor("black"))
                if jugadores_count % 2 == 0:
                    item.setBackground(QColor(240, 248, 255))
                else:
                    item.setBackground(QColor(255, 255, 255))
                jugadores_count += 1
            if jugadores_count == 0:
                list_widget.addItem("No hay jugadores en este equipo")
                list_widget.item(0).setForeground(QColor("gray"))
            print(f"[OK] Cargados {jugadores_count} jugadores del equipo {equipo_id}")
        except Exception as e:
            print(f"[ERROR] Error al cargar jugadores: {e}")
            import traceback
            traceback.print_exc()
    def _editar_equipo_seleccionado(self):
        if self.equipo_seleccionado_id is None:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona un equipo para editar")
            return
        try:
            try:
                self.form_equipo_window.dialog.finished.disconnect()
            except RuntimeError:
                pass
            db = get_db_connection()
            query = QSqlQuery(db)
            query.exec(f"SELECT id, nombre, curso, color_camiseta FROM equipos WHERE id = {self.equipo_seleccionado_id}")
            if query.next():
                self.form_equipo_window.modo_edicion = True
                self.form_equipo_window.equipo_id = self.equipo_seleccionado_id
                equipo_id = query.value(0)
                equipo_nombre = query.value(1)
                equipo_curso = query.value(2)
                equipo_color = query.value(3)
                print(f"DEBUG: Editando equipo ID={equipo_id}, Nombre={equipo_nombre}, Curso={equipo_curso}, Color={equipo_color}")
                self.form_equipo_window._cargar_datos_combobox()
                txt_nombre = self.form_equipo_window.dialog.findChild(QLineEdit, "txtNombre")
                cmb_curso = self.form_equipo_window.dialog.findChild(QComboBox, "cmbCurso")
                txt_color = self.form_equipo_window.dialog.findChild(QLineEdit, "txtColor")
                if txt_nombre:
                    txt_nombre.setText(equipo_nombre if equipo_nombre else "")
                    print(f"[OK] Nombre cargado: {equipo_nombre}")
                if cmb_curso:
                    index = cmb_curso.findText(equipo_curso if equipo_curso else "")
                    if index >= 0:
                        cmb_curso.setCurrentIndex(index)
                        print(f"[OK] Curso cargado en índice {index}: {equipo_curso}")
                    else:
                        cmb_curso.addItem(equipo_curso if equipo_curso else "")
                        index = cmb_curso.findText(equipo_curso if equipo_curso else "")
                        if index >= 0:
                            cmb_curso.setCurrentIndex(index)
                        print(f"[ERROR] Curso no encontrado en combobox, se agrego: {equipo_curso}")
                if txt_color:
                    txt_color.setText(equipo_color if equipo_color else "")
                    print(f"[OK] Color cargado: {equipo_color}")
                self.form_equipo_window.dialog.finished.connect(self._cargar_equipos)
                print(f"[OK] Formulario abierto")
                self.form_equipo_window.show()
        except Exception as e:
            print(f"[ERROR] Error al editar equipo: {e}")
            import traceback
            traceback.print_exc()
    def _eliminar_equipo_seleccionado(self):
        if self.equipo_seleccionado_id is None:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona un equipo para eliminar")
            return
        try:
            db = get_db_connection()
            query = QSqlQuery(db)
            query.exec(f"SELECT nombre FROM equipos WHERE id = {self.equipo_seleccionado_id}")
            equipo_nombre = "desconocido"
            if query.next():
                equipo_nombre = query.value(0)
            respuesta = QMessageBox.question(
                self,
                "Confirmar eliminación",
                f"¿Estás seguro de que deseas eliminar el equipo '{equipo_nombre}'?\n\nEsto también eliminará todos los jugadores del equipo.",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if respuesta == QMessageBox.StandardButton.Yes:
                query = QSqlQuery(db)
                query.prepare("DELETE FROM equipos WHERE id = ?")
                query.addBindValue(self.equipo_seleccionado_id)
                if query.exec():
                    QMessageBox.information(self, "Éxito", f"Equipo '{equipo_nombre}' eliminado correctamente")
                    self.equipo_seleccionado_id = None
                    self._cargar_equipos()
                    self.ui.listJugadores.clear()
                    print(f"[OK] Equipo {self.equipo_seleccionado_id} eliminado")
                else:
                    QMessageBox.critical(self, "Error", f"Error al eliminar el equipo: {query.lastError().text()}")
                    print(f"[ERROR] Error al eliminar equipo: {query.lastError().text()}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error inesperado: {str(e)}")
            print(f"[ERROR] Error inesperado al eliminar equipo: {e}")
            import traceback
            traceback.print_exc()
