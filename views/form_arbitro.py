import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QDate
from PySide6.QtWidgets import QLineEdit, QComboBox, QDateEdit, QMessageBox
from PySide6.QtSql import QSqlQuery
from models.globals import get_db_connection
class FormArbitro:
    def __init__(self, parent=None):
        self.parent = parent
        self.arbitro_id = None
        self.modo_edicion = False
        ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_ui = os.path.join(ruta_base, "ui", "form_arbitro.ui")
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
                            self._cargar_cursos()
                        except Exception as e:
                            print(f"[WARN] No se pudo cargar cursos en el formulario: {e}")
                        print(f"FormArbitro: .ui cargado desde {ruta_ui}")
                        return
            except Exception as e:
                print(f"Error al cargar {ruta_ui}: {e}")
        from PySide6.QtWidgets import QDialog
        self.dialog = QDialog(parent)
        self.dialog.setWindowTitle("Formulario de Árbitro")
        print("FormArbitro: fallback usado")
    def _conectar_botones(self):
        try:
            from PySide6.QtWidgets import QPushButton
            buttons = self.dialog.findChildren(QPushButton)
            for btn in buttons:
                if "OK" in btn.text() or "Aceptar" in btn.text():
                    btn.clicked.connect(self._guardar_arbitro)
                elif "Cancel" in btn.text() or "Cancelar" in btn.text():
                    btn.clicked.connect(self._cancelar)
        except Exception as e:
            print(f"Error al conectar botones: {e}")
        try:
            self._cargar_cursos()
        except Exception:
            pass
    def _guardar_arbitro(self):
        try:
            db = get_db_connection()
            txt_nombre = self.dialog.findChild(QLineEdit, "txtNombre")
            date_nacimiento = self.dialog.findChild(QDateEdit, "dateFechaNac")
            cmb_curso = self.dialog.findChild(QComboBox, "cmbCurso")
            if not txt_nombre or not txt_nombre.text().strip():
                QMessageBox.warning(self.dialog, "Validación", "El nombre no puede estar vacío")
                return
            if not cmb_curso or cmb_curso.currentText() == "-- Seleccionar --":
                QMessageBox.warning(self.dialog, "Validación", "Debe seleccionar un curso")
                return
            query = QSqlQuery(db)
            if self.modo_edicion:
                query.prepare("""
                    UPDATE participantes SET
                        nombre = ?,
                        fecha_nacimiento = ?,
                        curso = ?
                    WHERE id = ? AND tipo_participante = 'Arbitro'
                """)
                query.addBindValue(txt_nombre.text().strip())
                query.addBindValue(date_nacimiento.date().toString("yyyy-MM-dd") if date_nacimiento else "")
                query.addBindValue(cmb_curso.currentText())
                query.addBindValue(self.arbitro_id)
            else:
                query.prepare("""
                    INSERT INTO participantes (nombre, fecha_nacimiento, curso, tipo_participante)
                    VALUES (?, ?, ?, 'Arbitro')
                """)
                query.addBindValue(txt_nombre.text().strip())
                query.addBindValue(date_nacimiento.date().toString("yyyy-MM-dd") if date_nacimiento else "")
                query.addBindValue(cmb_curso.currentText())
            if query.exec():
                accion = "actualizado" if self.modo_edicion else "guardado"
                print(f"[DEBUG] Árbitro '{txt_nombre.text()}' {accion} correctamente")
                QMessageBox.information(self.dialog, "Éxito", f"Árbitro {accion} correctamente")
                self._limpiar_formulario()
                self.arbitro_id = None
                self.modo_edicion = False
                print("[DEBUG] Cerrando diálogo con accept()")
                self.dialog.accept()
            else:
                error_msg = query.lastError().text()
                print(f"[ERROR] Error al guardar árbitro: {error_msg}")
                QMessageBox.critical(self.dialog, "Error", f"Error al guardar: {error_msg}")
        except Exception as e:
            print(f"[ERROR] Error inesperado al guardar árbitro: {str(e)}")
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
        date_nacimiento = self.dialog.findChild(QDateEdit, "dateFechaNac")
        if date_nacimiento:
            date_nacimiento.setDate(QDate.currentDate())
    def _cargar_cursos(self):
        db = get_db_connection()
        query = QSqlQuery(db)
        if not query.exec("SELECT DISTINCT curso FROM equipos ORDER BY curso"):
            raise Exception(query.lastError().text())
        cmb_curso = self.dialog.findChild(QComboBox, "cmbCurso")
        if not cmb_curso:
            return
        cmb_curso.clear()
        cmb_curso.addItem("-- Seleccionar --")
        while query.next():
            curso = query.value(0)
            if curso:
                cmb_curso.addItem(str(curso))
    def _cancelar(self):
        print("[DEBUG] Formulario cancelado")
        self._limpiar_formulario()
        self.dialog.reject()
    def cargar_para_editar(self, arbitro_id):
        try:
            db = get_db_connection()
            query = QSqlQuery(db)
            query.prepare("""
                SELECT id, nombre, fecha_nacimiento, curso
                FROM participantes
                WHERE id = ? AND tipo_participante = 'Arbitro'
            """)
            query.addBindValue(arbitro_id)
            if not query.exec():
                raise Exception(f"Error al cargar árbitro: {query.lastError().text()}")
            if not query.first():
                raise Exception("Árbitro no encontrado")
            nombre = query.value(1)
            fecha_nac = query.value(2)
            curso = query.value(3)
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
            self.arbitro_id = arbitro_id
            self.modo_edicion = True
            print(f"[DEBUG] Árbitro {nombre} cargado para editar")
        except Exception as e:
            print(f"[ERROR] Error al cargar árbitro: {e}")
            QMessageBox.critical(self.dialog, "Error", f"Error al cargar: {e}")
    def show(self):
        if self.dialog:
            if not self.modo_edicion:
                self._limpiar_formulario()
            self.dialog.show()
    def close(self):
        if self.dialog:
            self.dialog.close()
