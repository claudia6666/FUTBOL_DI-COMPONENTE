import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QDate
from PySide6.QtWidgets import QPushButton, QSpinBox, QLineEdit, QComboBox, QDateEdit, QMessageBox, QCheckBox, QRadioButton, QDialog
from PySide6.QtGui import QColor
from PySide6.QtSql import QSqlQuery
from models.globals import get_db_connection
class FormParticipante:
    def __init__(self, parent=None):
        self.parent = parent
        self.equipo_id = None
        self.participante_id = None
        self.modo_edicion = False
        self.tipo_participante = None
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
                        self._conectar_controles()
                        self._conectar_botones_guardado()
                        self._conectar_checkboxes_tipo()
                        self._cargar_datos_combobox()
                        self._mejorar_estilos_formulario()
                        self._cargar_datos_combobox()
                        print(f"FormParticipante: .ui cargado desde {ruta_ui}")
                        return
            except Exception as e:
                print(f"Error al cargar {ruta_ui}: {e}")
        from PySide6.QtWidgets import QDialog
        self.dialog = QDialog(parent)
        self.dialog.setWindowTitle("Formulario de Participante")
        self.dialog.setGeometry(100, 100, 900, 1000)
        print("FormParticipante: fallback usado")
    def _conectar_controles(self):
        try:
            spin_goles = self.dialog.findChild(QSpinBox, "spinGoles")
            spin_amarillas = self.dialog.findChild(QSpinBox, "spinTarjetasAmarillas")
            spin_rojas = self.dialog.findChild(QSpinBox, "spinTarjetasRojas")
            if spin_goles:
                spin_goles.setMinimum(0)
                spin_goles.setMaximum(999)
                spin_goles.setButtonSymbols(QSpinBox.UpDownArrows)
                spin_goles.setStyleSheet("""
                    QSpinBox {
                        color: black;
                        background-color: white;
                        border: 1px solid
                        padding: 2px;
                        border-radius: 4px;
                    }
                    QSpinBox::up-button {
                        width: 24px;
                        background-color:
                        border: 1px solid
                    }
                    QSpinBox::down-button {
                        width: 24px;
                        background-color:
                        border: 1px solid
                    }
                    QSpinBox::up-arrow {
                        image: url(:/icons/up);
                    }
                """)
            if spin_amarillas:
                spin_amarillas.setMinimum(0)
                spin_amarillas.setMaximum(999)
                spin_amarillas.setButtonSymbols(QSpinBox.UpDownArrows)
                spin_amarillas.setStyleSheet("""
                    QSpinBox {
                        color: black;
                        background-color: white;
                        border: 1px solid
                        padding: 2px;
                        border-radius: 4px;
                    }
                    QSpinBox::up-button {
                        width: 24px;
                        background-color:
                        border: 1px solid
                    }
                    QSpinBox::down-button {
                        width: 24px;
                        background-color:
                        border: 1px solid
                    }
                """)
            if spin_rojas:
                spin_rojas.setMinimum(0)
                spin_rojas.setMaximum(999)
                spin_rojas.setButtonSymbols(QSpinBox.UpDownArrows)
                spin_rojas.setStyleSheet("""
                    QSpinBox {
                        color: black;
                        background-color: white;
                        border: 1px solid
                        padding: 2px;
                        border-radius: 4px;
                    }
                    QSpinBox::up-button {
                        width: 24px;
                        background-color:
                        border: 1px solid
                    }
                    QSpinBox::down-button {
                        width: 24px;
                        background-color:
                        border: 1px solid
                    }
                """)
        except Exception as e:
            print(f"Error al conectar controles: {e}")
    def _mejorar_estilos_formulario(self):
        try:
            from PySide6.QtWidgets import QLabel
            for label in self.dialog.findChildren(QLabel):
                label.setStyleSheet("QLabel { color: black; font-weight: bold; }")
            for line_edit in self.dialog.findChildren(QLineEdit):
                line_edit.setStyleSheet("""
                    QLineEdit {
                        color: black;
                        background-color: white;
                        border: 1px solid
                        padding: 5px;
                        border-radius: 4px;
                    }
                """)
            for date_edit in self.dialog.findChildren(QDateEdit):
                date_edit.setStyleSheet("""
                    QDateEdit {
                        color: black;
                        background-color: white;
                        border: 1px solid
                        padding: 5px;
                        border-radius: 4px;
                    }
                """)
            for combo_box in self.dialog.findChildren(QComboBox):
                combo_box.setStyleSheet("""
                    QComboBox {
                        color: black;
                        background-color: white;
                        border: 1px solid
                        padding: 5px;
                        border-radius: 4px;
                    }
                    QComboBox::drop-down {
                        border: none;
                    }
                    QComboBox QAbstractItemView {
                        color: black;
                        background-color: white;
                        selection-background-color:
                    }
                """)
            for button in self.dialog.findChildren(QPushButton):
                button.setStyleSheet("""
                    QPushButton {
                        color: white;
                        background-color:
                        border: none;
                        padding: 8px;
                        border-radius: 4px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color:
                    }
                    QPushButton:pressed {
                        background-color:
                    }
                """)
            print("Estilos del formulario mejorados")
        except Exception as e:
            print(f"Error al mejorar estilos: {e}")
    def _cargar_datos_combobox(self):
        try:
            from PySide6.QtCore import Qt
            db = get_db_connection()
            cmb_equipo = self.dialog.findChild(QComboBox, "cmbEquipo")
            if cmb_equipo:
                query = QSqlQuery(db)
                query.exec("SELECT id, nombre FROM equipos ORDER BY nombre")
                cmb_equipo.clear()
                cmb_equipo.addItem("", None)
                while query.next():
                    equipo_id = query.value(0)
                    nombre = query.value(1)
                    cmb_equipo.addItem(nombre, equipo_id)
            cmb_curso = self.dialog.findChild(QComboBox, "cmbCurso")
            if cmb_curso:
                query = QSqlQuery(db)
                query.exec("SELECT DISTINCT curso FROM equipos")
                cmb_curso.clear()
                cmb_curso.addItem("")
                cursos_agregados = set()
                while query.next():
                    curso = query.value(0)
                    if curso and curso not in cursos_agregados:
                        cmb_curso.addItem(curso)
                        cursos_agregados.add(curso)
                if cmb_curso.count() == 1:
                    for curso in ["1º DAM", "2º DAM", "1º ASIR", "2º ASIR"]:
                        cmb_curso.addItem(curso)
            cmb_posicion = self.dialog.findChild(QComboBox, "cmbPosicion")
            if cmb_posicion:
                cmb_posicion.clear()
                cmb_posicion.addItem("")
                for posicion in ["Portero", "Defensa", "Centrocampista", "Delantero"]:
                    cmb_posicion.addItem(posicion)
        except Exception as e:
            print(f"Error al cargar datos en combobox: {e}")
    def _conectar_botones_guardado(self):
        try:
            button_box = self.dialog.findChild(type(self.dialog).__bases__[0], "buttonBox")
            for widget in self.dialog.findChildren(type(self.dialog).__bases__[0]):
                if hasattr(widget, 'objectName') and widget.objectName() == "buttonBox":
                    button_box = widget
                    break
            if self.dialog.findChildren(type(self.dialog).__bases__[0]):
                buttons = self.dialog.findChildren(QPushButton)
                for btn in buttons:
                    if "Save" in btn.text() or "Guardar" in btn.text():
                        btn.clicked.connect(self._guardar_participante)
                    elif "Cancel" in btn.text() or "Cancelar" in btn.text():
                        btn.clicked.connect(self._cancelar)
        except Exception as e:
            print(f"Error al conectar botones de guardado: {e}")
    def _conectar_checkboxes_tipo(self):
        try:
            jugador_btn = self.dialog.findChild(QRadioButton, "rbJugador") or self.dialog.findChild(QCheckBox, "chkJugador")
            arbitro_btn = self.dialog.findChild(QRadioButton, "rbArbitro") or self.dialog.findChild(QCheckBox, "chkArbitro")
            if jugador_btn:
                try:
                    jugador_btn.toggled.connect(self._actualizar_campos_segun_tipo)
                except Exception:
                    jugador_btn.stateChanged.connect(self._actualizar_campos_segun_tipo)
            if arbitro_btn:
                try:
                    arbitro_btn.toggled.connect(self._actualizar_campos_segun_tipo)
                except Exception:
                    arbitro_btn.stateChanged.connect(self._actualizar_campos_segun_tipo)
            print("[DEBUG] Role buttons connected (radio or checkbox)")
        except Exception as e:
            print(f"Error al conectar checkboxes: {e}")
    def _get_role_buttons(self):
        jugador_btn = self.dialog.findChild(QRadioButton, "rbJugador") or self.dialog.findChild(QCheckBox, "chkJugador")
        arbitro_btn = self.dialog.findChild(QRadioButton, "rbArbitro") or self.dialog.findChild(QCheckBox, "chkArbitro")
        return jugador_btn, arbitro_btn
    def _actualizar_campos_segun_tipo(self):
        try:
            jugador_btn, _ = self._get_role_buttons()
            cmb_posicion = self.dialog.findChild(QComboBox, "cmbPosicion")
            cmb_equipo = self.dialog.findChild(QComboBox, "cmbEquipo")
            spin_goles = self.dialog.findChild(QSpinBox, "spinGoles")
            spin_amarillas = self.dialog.findChild(QSpinBox, "spinTarjetasAmarillas")
            spin_rojas = self.dialog.findChild(QSpinBox, "spinTarjetasRojas")
            es_jugador = jugador_btn and getattr(jugador_btn, 'isChecked', lambda: False)()
            if cmb_posicion:
                cmb_posicion.setEnabled(es_jugador)
            if cmb_equipo:
                cmb_equipo.setEnabled(es_jugador)
            if spin_goles:
                spin_goles.setEnabled(es_jugador)
            if spin_amarillas:
                spin_amarillas.setEnabled(es_jugador)
            if spin_rojas:
                spin_rojas.setEnabled(es_jugador)
            print(f"[DEBUG] Campos actualizados. Es jugador: {es_jugador}")
        except Exception as e:
            print(f"Error al actualizar campos: {e}")
    def _guardar_participante(self):
        try:
            db = get_db_connection()
            txt_nombre = self.dialog.findChild(QLineEdit, "txtNombre")
            date_nacimiento = self.dialog.findChild(QDateEdit, "dateFechaNac")
            cmb_curso = self.dialog.findChild(QComboBox, "cmbCurso")
            cmb_posicion = self.dialog.findChild(QComboBox, "cmbPosicion")
            cmb_equipo = self.dialog.findChild(QComboBox, "cmbEquipo")
            spin_goles = self.dialog.findChild(QSpinBox, "spinGoles")
            spin_amarillas = self.dialog.findChild(QSpinBox, "spinTarjetasAmarillas")
            spin_rojas = self.dialog.findChild(QSpinBox, "spinTarjetasRojas")
            jugador_btn, arbitro_btn = self._get_role_buttons()
            if not txt_nombre or not txt_nombre.text().strip():
                QMessageBox.warning(self.dialog, "Validación", "El nombre no puede estar vacío")
                return
            tipo_participante = ""
            if jugador_btn and getattr(jugador_btn, 'isChecked', lambda: False)():
                tipo_participante = "Jugador"
            elif arbitro_btn and getattr(arbitro_btn, 'isChecked', lambda: False)():
                tipo_participante = "Árbitro"
            if not tipo_participante:
                QMessageBox.warning(self.dialog, "Validación", "Debe seleccionar el rol (Jugador o Árbitro)")
                return
            if tipo_participante == "Jugador":
                if not cmb_equipo or not cmb_equipo.currentData():
                    QMessageBox.warning(self.dialog, "Validación", "Un jugador debe tener un equipo asignado")
                    return
            query = QSqlQuery(db)
            if self.modo_edicion:
                query.prepare("""
                    UPDATE participantes SET
                        nombre = ?,
                        fecha_nacimiento = ?,
                        curso = ?,
                        tipo_participante = ?,
                        posicion = ?,
                        equipo_id = ?,
                        goles = ?,
                        tarjetas_amarillas = ?,
                        tarjetas_rojas = ?
                    WHERE id = ?
                """)
                query.addBindValue(txt_nombre.text().strip())
                query.addBindValue(date_nacimiento.date().toString("yyyy-MM-dd") if date_nacimiento else "")
                query.addBindValue(cmb_curso.currentText() if cmb_curso else "")
                query.addBindValue(tipo_participante)
                query.addBindValue(cmb_posicion.currentText() if cmb_posicion and tipo_participante == "Jugador" else "")
                query.addBindValue(cmb_equipo.currentData() if cmb_equipo and cmb_equipo.currentData() else None)
                query.addBindValue(spin_goles.value() if spin_goles and tipo_participante == "Jugador" else 0)
                query.addBindValue(spin_amarillas.value() if spin_amarillas and tipo_participante == "Jugador" else 0)
                query.addBindValue(spin_rojas.value() if spin_rojas and tipo_participante == "Jugador" else 0)
                query.addBindValue(self.participante_id)
            else:
                query.prepare("""
                    INSERT INTO participantes (nombre, fecha_nacimiento, curso, tipo_participante, posicion, equipo_id, goles, tarjetas_amarillas, tarjetas_rojas)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """)
                query.addBindValue(txt_nombre.text().strip())
                query.addBindValue(date_nacimiento.date().toString("yyyy-MM-dd") if date_nacimiento else "")
                query.addBindValue(cmb_curso.currentText() if cmb_curso else "")
                query.addBindValue(tipo_participante)
                query.addBindValue(cmb_posicion.currentText() if cmb_posicion and tipo_participante == "Jugador" else "")
                query.addBindValue(cmb_equipo.currentData() if cmb_equipo and cmb_equipo.currentData() else None)
                query.addBindValue(spin_goles.value() if spin_goles and tipo_participante == "Jugador" else 0)
                query.addBindValue(spin_amarillas.value() if spin_amarillas and tipo_participante == "Jugador" else 0)
                query.addBindValue(spin_rojas.value() if spin_rojas and tipo_participante == "Jugador" else 0)
            if query.exec():
                accion = "actualizado" if self.modo_edicion else "guardado"
                print(f"[DEBUG] Participante '{txt_nombre.text()}' {accion} correctamente en la BD")
                QMessageBox.information(self.dialog, "Éxito", f"Participante {accion} correctamente")
                self._limpiar_formulario()
                self.equipo_id = None
                self.participante_id = None
                self.modo_edicion = False
                print("[DEBUG] Cerrando diálogo con accept()")
                self.dialog.accept()
            else:
                error_msg = query.lastError().text()
                print(f"[ERROR] Error al guardar participante: {error_msg}")
                QMessageBox.critical(self.dialog, "Error", f"Error al guardar: {error_msg}")
        except Exception as e:
            print(f"[ERROR] Error inesperado al guardar participante: {str(e)}")
            import traceback
            traceback.print_exc()
            QMessageBox.critical(self.dialog, "Error", f"Error inesperado: {str(e)}")
    def _limpiar_formulario(self):
        txt_nombre = self.dialog.findChild(QLineEdit, "txtNombre")
        if txt_nombre:
            txt_nombre.clear()
        spin_goles = self.dialog.findChild(QSpinBox, "spinGoles")
        if spin_goles:
            spin_goles.setValue(0)
        spin_amarillas = self.dialog.findChild(QSpinBox, "spinTarjetasAmarillas")
        if spin_amarillas:
            spin_amarillas.setValue(0)
        spin_rojas = self.dialog.findChild(QSpinBox, "spinTarjetasRojas")
        if spin_rojas:
            spin_rojas.setValue(0)
        jugador_btn, arbitro_btn = self._get_role_buttons()
        if jugador_btn:
            try:
                jugador_btn.setChecked(False)
            except Exception:
                pass
        if arbitro_btn:
            try:
                arbitro_btn.setChecked(False)
            except Exception:
                pass
        cmb_equipo = self.dialog.findChild(QComboBox, "cmbEquipo")
        if cmb_equipo:
            cmb_equipo.setCurrentIndex(0)
            cmb_equipo.setEnabled(True)
        self.equipo_id = None
        self.participante_id = None
        self.modo_edicion = False
    def _cancelar(self):
        print("[DEBUG] Formulario cancelado por el usuario")
        self.dialog.reject()
    def show(self, tipo_participante=None):
        if self.dialog:
            try:
                self._cargar_datos_combobox()
            except Exception:
                pass
            if not self.modo_edicion:
                self._limpiar_formulario()
                if self.equipo_id:
                    self.tipo_participante = "Jugador"
                    self._preconfigurar_tipo("Jugador")
                elif tipo_participante:
                    self.tipo_participante = tipo_participante
                    self._preconfigurar_tipo(tipo_participante)
            self._preseleccionar_equipo()
            self.dialog.show()
    def _preconfigurar_tipo(self, tipo_participante):
        try:
            jugador_btn, arbitro_btn = self._get_role_buttons()
            if tipo_participante == "Jugador" and jugador_btn:
                try:
                    jugador_btn.setChecked(True)
                except Exception:
                    pass
                if arbitro_btn:
                    try:
                        arbitro_btn.setChecked(False)
                    except Exception:
                        pass
                print("[DEBUG] Formulario preconfigurado como Jugador")
            elif tipo_participante == "Arbitro" and arbitro_btn:
                try:
                    arbitro_btn.setChecked(True)
                except Exception:
                    pass
                if jugador_btn:
                    try:
                        jugador_btn.setChecked(False)
                    except Exception:
                        pass
                print("[DEBUG] Formulario preconfigurado como Árbitro")
        except Exception as e:
            print(f"Error al preconfigurar tipo: {e}")
    def cargar_para_editar(self, participante_id):
        try:
            db = get_db_connection()
            query = QSqlQuery(db)
            query.prepare("""
                SELECT id, nombre, fecha_nacimiento, curso, tipo_participante, posicion, equipo_id, goles, tarjetas_amarillas, tarjetas_rojas
                FROM participantes
                WHERE id = ?
            """)
            query.addBindValue(participante_id)
            if not query.exec():
                raise Exception(f"Error al cargar participante: {query.lastError().text()}")
            if not query.first():
                raise Exception("Participante no encontrado")
            nombre = query.value(1)
            fecha_nac = query.value(2)
            curso = query.value(3)
            tipo = query.value(4)
            posicion = query.value(5)
            equipo_id = query.value(6)
            goles = query.value(7)
            amarillas = query.value(8)
            rojas = query.value(9)
            txt_nombre = self.dialog.findChild(QLineEdit, "txtNombre")
            if txt_nombre:
                txt_nombre.setText(nombre)
            date_nacimiento = self.dialog.findChild(QDateEdit, "dateNacimiento")
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
            jugador_btn, arbitro_btn = self._get_role_buttons()
            if tipo == "Jugador" and jugador_btn:
                try:
                    jugador_btn.setChecked(True)
                except Exception:
                    pass
            elif tipo == "Árbitro" and arbitro_btn:
                try:
                    arbitro_btn.setChecked(True)
                except Exception:
                    pass
            self.participante_id = participante_id
            self.modo_edicion = True
            print(f"[DEBUG] Participante {nombre} cargado para editar")
        except Exception as e:
            print(f"[ERROR] Error al cargar participante: {e}")
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(self.dialog, "Error", f"Error al cargar: {e}")
    def _preseleccionar_equipo(self):
        if not self.equipo_id:
            return
        print(f"[DEBUG] Preseleccionando equipo ID: {self.equipo_id}")
        cmb_equipo = self.dialog.findChild(QComboBox, "cmbEquipo")
        cmb_curso = self.dialog.findChild(QComboBox, "cmbCurso")
        jugador_btn, _ = self._get_role_buttons()
        if jugador_btn:
            try:
                jugador_btn.setChecked(True)
                print(f"[DEBUG] Control de jugador marcado")
            except Exception:
                pass
        if cmb_equipo:
            for i in range(cmb_equipo.count()):
                if cmb_equipo.itemData(i) == self.equipo_id:
                    cmb_equipo.setCurrentIndex(i)
                    cmb_equipo.setEnabled(False)
                    print(f"[DEBUG] Equipo ID {self.equipo_id} seleccionado y deshabilitado")
                    try:
                        db = get_db_connection()
                        query = QSqlQuery(db)
                        query.prepare("SELECT curso FROM equipos WHERE id = ?")
                        query.addBindValue(self.equipo_id)
                        if query.exec() and query.next():
                            curso_equipo = query.value(0)
                            if curso_equipo and cmb_curso:
                                idx = cmb_curso.findText(curso_equipo)
                                if idx >= 0:
                                    cmb_curso.setCurrentIndex(idx)
                                    cmb_curso.setEnabled(False)
                                    print(f"[DEBUG] Curso '{curso_equipo}' preseleccionado y deshabilitado")
                    except Exception as e:
                        print(f"Error al obtener curso del equipo: {e}")
                    break
    def close(self):
        if self.dialog:
            self.dialog.close()
