import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QDate
from PySide6.QtWidgets import QLineEdit, QComboBox, QDateEdit, QMessageBox, QSpinBox
from PySide6.QtSql import QSqlQuery
from models.globals import get_db_connection
class FormJugador:
    def __init__(self, parent=None):
        self.parent = parent
        self.jugador_id = None
        self.modo_edicion = False
        ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_ui = os.path.join(ruta_base, "ui", "form_participantes.ui")
        if os.path.exists(ruta_ui):
            try:
                loader = QUiLoader()
                ui_file = QFile(ruta_ui)
                if ui_file.open(QIODevice.ReadOnly):
                    self.dialog = loader.load(ui_file, None)
                    ui_file.close()
                    if self.dialog:
                        self._conectar_botones()
                        try:
                            self._cargar_datos_combobox()
                        except Exception as e:
                            print(f"[WARN] No se pudo cargar datos en el formulario: {e}")
                        self._ocultar_controles_innecesarios()
                        print(f"FormJugador: .ui cargado desde {ruta_ui}")
                        return
            except Exception as e:
                print(f"Error al cargar {ruta_ui}: {e}")
        from PySide6.QtWidgets import QDialog
        self.dialog = QDialog(parent)
        self.dialog.setWindowTitle("Agregar Jugador")
        print("FormJugador: fallback usado")
    def _ocultar_controles_innecesarios(self):
        try:
            from PySide6.QtWidgets import QLabel, QRadioButton, QCheckBox
            for widget in self.dialog.findChildren(QRadioButton):
                if widget.objectName() in ["rbJugador", "rbArbitro", "chkJugador", "chkArbitro"]:
                    widget.hide()
            for widget in self.dialog.findChildren(QCheckBox):
                if widget.objectName() in ["rbJugador", "rbArbitro", "chkJugador", "chkArbitro"]:
                    widget.hide()
            for label in self.dialog.findChildren(QLabel):
                if "Tipo" in label.text() or "Rol" in label.text():
                    label.hide()
            print("[DEBUG] Controles innecesarios ocultados")
        except Exception as e:
            print(f"Error al ocultar controles: {e}")
    def _conectar_botones(self):
        try:
            from PySide6.QtWidgets import QPushButton
            buttons = self.dialog.findChildren(QPushButton)
            for btn in buttons:
                if "OK" in btn.text() or "Aceptar" in btn.text() or "Guardar" in btn.text():
                    btn.clicked.connect(self._guardar_jugador)
                elif "Cancel" in btn.text() or "Cancelar" in btn.text():
                    btn.clicked.connect(self._cancelar)
            from PySide6.QtWidgets import QDialogButtonBox
            button_box = self.dialog.findChild(QDialogButtonBox, "buttonBox")
            if button_box:
                try:
                    button_box.accepted.connect(self._guardar_jugador)
                    button_box.rejected.connect(self._cancelar)
                except Exception:
                    pass
        except Exception as e:
            print(f"Error al conectar botones: {e}")
    def _cargar_datos_combobox(self):
        db = get_db_connection()
        cmb_equipo = self.dialog.findChild(QComboBox, "cmbEquipo")
        if cmb_equipo:
            query = QSqlQuery(db)
            query.exec("SELECT id, nombre FROM equipos ORDER BY nombre")
            cmb_equipo.clear()
            cmb_equipo.addItem("-- Seleccionar --", None)
            while query.next():
                equipo_id = query.value(0)
                nombre = query.value(1)
                cmb_equipo.addItem(nombre, equipo_id)
        cmb_curso = self.dialog.findChild(QComboBox, "cmbCurso")
        if cmb_curso:
            query = QSqlQuery(db)
            query.exec("SELECT DISTINCT curso FROM equipos ORDER BY curso")
            cmb_curso.clear()
            cmb_curso.addItem("-- Seleccionar --")
            while query.next():
                curso = query.value(0)
                if curso:
                    cmb_curso.addItem(str(curso))
        cmb_posicion = self.dialog.findChild(QComboBox, "cmbPosicion")
        if cmb_posicion:
            cmb_posicion.clear()
            cmb_posicion.addItem("-- Seleccionar --")
            for posicion in ["Portero", "Defensa", "Centrocampista", "Delantero"]:
                cmb_posicion.addItem(posicion)
    def _guardar_jugador(self):
        try:
            db = get_db_connection()
            txt_nombre = self.dialog.findChild(QLineEdit, "txtNombre")
            date_nacimiento = self.dialog.findChild(QDateEdit, "dateFechaNac")
            cmb_curso = self.dialog.findChild(QComboBox, "cmbCurso")
            cmb_equipo = self.dialog.findChild(QComboBox, "cmbEquipo")
            cmb_posicion = self.dialog.findChild(QComboBox, "cmbPosicion")
            spin_goles = self.dialog.findChild(QSpinBox, "spinGoles")
            spin_amarillas = self.dialog.findChild(QSpinBox, "spinTarjetasAmarillas")
            spin_rojas = self.dialog.findChild(QSpinBox, "spinTarjetasRojas")
            if not txt_nombre or not txt_nombre.text().strip():
                QMessageBox.warning(self.dialog, "Validación", "El nombre no puede estar vacío")
                return
            if not cmb_curso or cmb_curso.currentText() == "-- Seleccionar --":
                QMessageBox.warning(self.dialog, "Validación", "Debe seleccionar un curso")
                return
            if not cmb_equipo or cmb_equipo.currentData() is None:
                QMessageBox.warning(self.dialog, "Validación", "Debe seleccionar un equipo")
                return
            if not cmb_posicion or cmb_posicion.currentText() == "-- Seleccionar --":
                QMessageBox.warning(self.dialog, "Validación", "Debe seleccionar una posición")
                return
            query = QSqlQuery(db)
            if self.modo_edicion:
                query.prepare("""
                    UPDATE participantes SET
                        nombre = ?,
                        fecha_nacimiento = ?,
                        curso = ?,
                        equipo_id = ?,
                        posicion = ?,
                        goles = ?,
                        tarjetas_amarillas = ?,
                        tarjetas_rojas = ?
                    WHERE id = ? AND tipo_participante = 'Jugador'
                """)
                query.addBindValue(txt_nombre.text().strip())
                query.addBindValue(date_nacimiento.date().toString("yyyy-MM-dd") if date_nacimiento else "")
                query.addBindValue(cmb_curso.currentText())
                query.addBindValue(cmb_equipo.currentData())
                query.addBindValue(cmb_posicion.currentText())
                query.addBindValue(spin_goles.value() if spin_goles else 0)
                query.addBindValue(spin_amarillas.value() if spin_amarillas else 0)
                query.addBindValue(spin_rojas.value() if spin_rojas else 0)
                query.addBindValue(self.jugador_id)
            else:
                query.prepare("""
                    INSERT INTO participantes (nombre, fecha_nacimiento, curso, equipo_id, posicion, goles, tarjetas_amarillas, tarjetas_rojas, tipo_participante)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'Jugador')
                """)
                query.addBindValue(txt_nombre.text().strip())
                query.addBindValue(date_nacimiento.date().toString("yyyy-MM-dd") if date_nacimiento else "")
                query.addBindValue(cmb_curso.currentText())
                query.addBindValue(cmb_equipo.currentData())
                query.addBindValue(cmb_posicion.currentText())
                query.addBindValue(spin_goles.value() if spin_goles else 0)
                query.addBindValue(spin_amarillas.value() if spin_amarillas else 0)
                query.addBindValue(spin_rojas.value() if spin_rojas else 0)
            if query.exec():
                accion = "actualizado" if self.modo_edicion else "guardado"
                print(f"[DEBUG] Jugador '{txt_nombre.text()}' {accion} correctamente")
                QMessageBox.information(self.dialog, "Éxito", f"Jugador {accion} correctamente")
                self._limpiar_formulario()
                self.jugador_id = None
                self.modo_edicion = False
                print("[DEBUG] Cerrando diálogo con accept()")
                self.dialog.accept()
            else:
                error_msg = query.lastError().text()
                print(f"[ERROR] Error al guardar jugador: {error_msg}")
                QMessageBox.critical(self.dialog, "Error", f"Error al guardar: {error_msg}")
        except Exception as e:
            print(f"[ERROR] Error inesperado al guardar jugador: {str(e)}")
            import traceback
            traceback.print_exc()
            QMessageBox.critical(self.dialog, "Error", f"Error inesperado: {str(e)}")
    def _limpiar_formulario(self):
        txt_nombre = self.dialog.findChild(QLineEdit, "txtNombre")
        if txt_nombre:
            txt_nombre.clear()
        cmb_curso = self.dialog.findChild(QComboBox, "cmbCurso")
        if cmb_curso:
            cmb_curso.setCurrentIndex(0)
        cmb_equipo = self.dialog.findChild(QComboBox, "cmbEquipo")
        if cmb_equipo:
            cmb_equipo.setCurrentIndex(0)
        cmb_posicion = self.dialog.findChild(QComboBox, "cmbPosicion")
        if cmb_posicion:
            cmb_posicion.setCurrentIndex(0)
        spin_goles = self.dialog.findChild(QSpinBox, "spinGoles")
        if spin_goles:
            spin_goles.setValue(0)
        spin_amarillas = self.dialog.findChild(QSpinBox, "spinTarjetasAmarillas")
        if spin_amarillas:
            spin_amarillas.setValue(0)
        spin_rojas = self.dialog.findChild(QSpinBox, "spinTarjetasRojas")
        if spin_rojas:
            spin_rojas.setValue(0)
        date_nacimiento = self.dialog.findChild(QDateEdit, "dateFechaNac")
        if date_nacimiento:
            date_nacimiento.setDate(QDate.currentDate())
        from PySide6.QtWidgets import QGroupBox
        group_datos = self.dialog.findChild(QGroupBox, "groupDatosJugador")
        if group_datos:
            group_datos.setEnabled(True)
        self.modo_edicion = False
        self.jugador_id = None
    def _cancelar(self):
        print("[DEBUG] Formulario cancelado")
        self._limpiar_formulario()
        self.dialog.reject()
    def cargar_para_editar(self, jugador_id):
        try:
            db = get_db_connection()
            query = QSqlQuery(db)
            query.prepare("""
                SELECT id, nombre, fecha_nacimiento, curso, equipo_id, posicion, goles, tarjetas_amarillas, tarjetas_rojas
                FROM participantes
                WHERE id = ? AND tipo_participante = 'Jugador'
            """)
            query.addBindValue(jugador_id)
            if not query.exec():
                raise Exception(f"Error al cargar jugador: {query.lastError().text()}")
            if not query.first():
                raise Exception("Jugador no encontrado")
            nombre = query.value(1)
            fecha_nac = query.value(2)
            curso = query.value(3)
            equipo_id = query.value(4)
            posicion = query.value(5)
            goles = query.value(6)
            amarillas = query.value(7)
            rojas = query.value(8)
            txt_nombre = self.dialog.findChild(QLineEdit, "txtNombre")
            if txt_nombre:
                txt_nombre.setText(nombre)
            date_nacimiento = self.dialog.findChild(QDateEdit, "dateFechaNac")
            if date_nacimiento and fecha_nac:
                date_nacimiento.setDate(QDate.fromString(str(fecha_nac), "yyyy-MM-dd"))
            cmb_curso = self.dialog.findChild(QComboBox, "cmbCurso")
            if cmb_curso and curso:
                idx = cmb_curso.findText(curso)
                if idx >= 0:
                    cmb_curso.setCurrentIndex(idx)
            cmb_equipo = self.dialog.findChild(QComboBox, "cmbEquipo")
            if cmb_equipo and equipo_id:
                for i in range(cmb_equipo.count()):
                    if cmb_equipo.itemData(i) == equipo_id:
                        cmb_equipo.setCurrentIndex(i)
                        break
            cmb_posicion = self.dialog.findChild(QComboBox, "cmbPosicion")
            if cmb_posicion and posicion:
                idx = cmb_posicion.findText(posicion)
                if idx >= 0:
                    cmb_posicion.setCurrentIndex(idx)
            spin_goles = self.dialog.findChild(QSpinBox, "spinGoles")
            if spin_goles:
                spin_goles.setValue(goles if goles else 0)
            spin_amarillas = self.dialog.findChild(QSpinBox, "spinTarjetasAmarillas")
            if spin_amarillas:
                spin_amarillas.setValue(amarillas if amarillas else 0)
            spin_rojas = self.dialog.findChild(QSpinBox, "spinTarjetasRojas")
            if spin_rojas:
                spin_rojas.setValue(rojas if rojas else 0)
            from PySide6.QtWidgets import QGroupBox
            group_datos = self.dialog.findChild(QGroupBox, "groupDatosJugador")
            if group_datos:
                group_datos.setEnabled(True)
            self.jugador_id = jugador_id
            self.modo_edicion = True
            print(f"[DEBUG] Jugador {nombre} cargado para editar")
        except Exception as e:
            print(f"[ERROR] Error al cargar jugador: {e}")
            QMessageBox.critical(self.dialog, "Error", f"Error al cargar: {e}")
    def show(self):
        if self.dialog:
            if not self.modo_edicion:
                self._limpiar_formulario()
            self.dialog.show()
    def close(self):
        if self.dialog:
            self.dialog.close()
