import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QFileDialog, QLineEdit, QPushButton, QLabel, QMessageBox, QComboBox, QColorDialog
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtSql import QSqlQuery
from models.globals import get_db_connection
class FormEquipo:
    def __init__(self, parent=None):
        ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_ui = os.path.join(ruta_base, "ui", "form_equipo.ui")
        self.modo_edicion = False
        self.equipo_id = None
        if os.path.exists(ruta_ui):
            try:
                loader = QUiLoader()
                ui_file = QFile(ruta_ui)
                if ui_file.open(QIODevice.ReadOnly):
                    self.dialog = loader.load(ui_file, None)
                    ui_file.close()
                    if self.dialog:
                        btn_color = self.dialog.findChild(QPushButton, "btnSeleccionarColor")
                        if btn_color:
                            btn_color.clicked.connect(self._seleccionar_color)
                            print("Botón Color conectado")
                        self._conectar_botones_guardado()
                        self._cargar_datos_combobox()
                        print(f"FormEquipo: .ui cargado desde {ruta_ui}")
                        return
            except Exception as e:
                print(f"Error al cargar {ruta_ui}: {e}")
        from PySide6.QtWidgets import QDialog
        self.dialog = QDialog(parent)
        self.dialog.setWindowTitle("Formulario de Equipo")
        self.dialog.setGeometry(100, 100, 600, 500)
        print("FormEquipo: fallback usado")
    def _seleccionar_color(self):
        color = QColorDialog.getColor(QColor("white"), self.dialog, "Seleccionar Color de Camiseta")
        if color.isValid():
            txt_color = self.dialog.findChild(QLineEdit, "txtColor")
            if txt_color:
                color_name = color.name()
                txt_color.setText(color_name)
                print(f"Color seleccionado: {color_name}")
    def _cargar_datos_combobox(self):
        try:
            db = get_db_connection()
            cmb_curso = self.dialog.findChild(QComboBox, "cmbCurso")
            if cmb_curso:
                query = QSqlQuery(db)
                if self.modo_edicion and self.equipo_id:
                    query.exec(f"SELECT DISTINCT curso FROM equipos WHERE curso IS NOT NULL AND id != {self.equipo_id} ORDER BY curso")
                else:
                    query.exec("SELECT DISTINCT curso FROM equipos WHERE curso IS NOT NULL ORDER BY curso")
                cursos_asignados = set()
                while query.next():
                    curso = query.value(0)
                    if curso:
                        cursos_asignados.add(curso)
                cmb_curso.clear()
                cmb_curso.addItem("")
                cursos_defecto = [
                    "1 ESO A", "1 ESO B", "1 ESO C",
                    "2 ESO A", "2 ESO B", "2 ESO C",
                    "3 ESO A", "3 ESO B", "3 ESO C",
                    "4 ESO A", "4 ESO B", "4 ESO C",
                    "1 BAC A", "1 BAC B",
                    "2 BAC A", "2 BAC B"
                ]
                for curso in cursos_defecto:
                    if curso not in cursos_asignados:
                        cmb_curso.addItem(curso)
        except Exception as e:
            print(f"Error al cargar datos en combobox: {e}")
    def _conectar_botones_guardado(self):
        try:
            buttons = self.dialog.findChildren(QPushButton)
            for btn in buttons:
                if "Save" in btn.text() or "Guardar" in btn.text():
                    btn.clicked.connect(self._guardar_equipo)
                elif "Cancel" in btn.text() or "Cancelar" in btn.text():
                    btn.clicked.connect(self._cancelar)
        except Exception as e:
            print(f"Error al conectar botones de guardado: {e}")
    def _guardar_equipo(self):
        try:
            db = get_db_connection()
            txt_nombre = self.dialog.findChild(QLineEdit, "txtNombre")
            cmb_curso = self.dialog.findChild(QComboBox, "cmbCurso")
            txt_color = self.dialog.findChild(QLineEdit, "txtColor")
            if not txt_nombre or not txt_nombre.text().strip():
                QMessageBox.warning(self.dialog, "Validación", "El nombre del equipo no puede estar vacío")
                return
            query = QSqlQuery(db)
            nombre = txt_nombre.text().strip()
            curso = cmb_curso.currentText() if cmb_curso else ""
            color = txt_color.text() if txt_color else ""
            if self.modo_edicion and self.equipo_id:
                query.prepare("""
                    UPDATE equipos 
                    SET nombre = ?, curso = ?, color_camiseta = ?
                    WHERE id = ?
                """)
                query.addBindValue(nombre)
                query.addBindValue(curso)
                query.addBindValue(color)
                query.addBindValue(self.equipo_id)
                print(f"DEBUG UPDATE: ID={self.equipo_id}, nombre={nombre}, curso={curso}, color={color}")
                if query.exec():
                    QMessageBox.information(self.dialog, "Éxito", "Equipo actualizado correctamente")
                    self._limpiar_formulario()
                    self.modo_edicion = False
                    self.equipo_id = None
                    self.dialog.accept()
                else:
                    print(f"ERROR en UPDATE: {query.lastError().text()}")
                    QMessageBox.critical(self.dialog, "Error", f"Error al actualizar: {query.lastError().text()}")
            else:
                query.prepare("""
                    INSERT INTO equipos (nombre, curso, color_camiseta)
                    VALUES (?, ?, ?)
                """)
                query.addBindValue(nombre)
                query.addBindValue(curso)
                query.addBindValue(color)
                print(f"DEBUG INSERT: nombre={nombre}, curso={curso}, color={color}")
                if query.exec():
                    QMessageBox.information(self.dialog, "Éxito", "Equipo guardado correctamente")
                    self._limpiar_formulario()
                    self.modo_edicion = False
                    self.equipo_id = None
                    self.dialog.accept()
                else:
                    print(f"ERROR en INSERT: {query.lastError().text()}")
                    QMessageBox.critical(self.dialog, "Error", f"Error al guardar: {query.lastError().text()}")
        except Exception as e:
            QMessageBox.critical(self.dialog, "Error", f"Error inesperado: {str(e)}")
    def _limpiar_formulario(self):
        txt_nombre = self.dialog.findChild(QLineEdit, "txtNombre")
        if txt_nombre:
            txt_nombre.clear()
        txt_color = self.dialog.findChild(QLineEdit, "txtColor")
        if txt_color:
            txt_color.clear()
    def _cancelar(self):
        self.modo_edicion = False
        self.equipo_id = None
        self.dialog.close()
    def show(self):
        if self.dialog:
            if self.modo_edicion:
                self.dialog.setWindowTitle("Editar Equipo")
            else:
                self.dialog.setWindowTitle("Nuevo Equipo")
                self._limpiar_formulario()
                self._cargar_datos_combobox()
            self.dialog.show()
    def close(self):
        if self.dialog:
            self.dialog.close()
