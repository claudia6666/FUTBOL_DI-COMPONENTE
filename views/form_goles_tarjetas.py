import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QPushButton, QComboBox, QSpinBox, QMessageBox
from PySide6.QtSql import QSqlQuery
from models.globals import get_db_connection
class FormGolesTarjetas:
    def __init__(self, parent=None):
        ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_ui = os.path.join(ruta_base, "ui", "form_GolesTarjetas.ui")
        if os.path.exists(ruta_ui):
            try:
                loader = QUiLoader()
                ui_file = QFile(ruta_ui)
                if ui_file.open(QIODevice.ReadOnly):
                    self.dialog = loader.load(ui_file, None)
                    ui_file.close()
                    if self.dialog:
                        self._conectar_botones_guardado()
                        print(f"FormGolesTarjetas: .ui cargado desde {ruta_ui}")
                        return
            except Exception as e:
                print(f"Error al cargar {ruta_ui}: {e}")
        from PySide6.QtWidgets import QDialog
        self.dialog = QDialog(parent)
        self.dialog.setWindowTitle("Registrar Goles/Tarjetas")
        self.dialog.setGeometry(100, 100, 600, 500)
        print("FormGolesTarjetas: fallback usado")
    def _conectar_botones_guardado(self):
        try:
            buttons = self.dialog.findChildren(QPushButton)
            for btn in buttons:
                if "Save" in btn.text() or "Guardar" in btn.text():
                    btn.clicked.connect(self._guardar_evento)
                elif "Cancel" in btn.text() or "Cancelar" in btn.text():
                    btn.clicked.connect(self._cancelar)
        except Exception as e:
            print(f"Error al conectar botones de guardado: {e}")
    def _cargar_partidos_y_jugadores(self):
        try:
            db = get_db_connection()
            cmb_partido = self.dialog.findChild(QComboBox, "cmbPartido")
            cmb_jugador = self.dialog.findChild(QComboBox, "cmbJugador")
            cmb_tipo = self.dialog.findChild(QComboBox, "cmbTipo")
            if cmb_partido:
                cmb_partido.clear()
                q = QSqlQuery(db)
                q.exec("SELECT id, COALESCE(e1.nombre,'') || ' vs ' || COALESCE(e2.nombre,'') FROM partidos p LEFT JOIN equipos e1 ON p.equipo1_id=e1.id LEFT JOIN equipos e2 ON p.equipo2_id=e2.id ORDER BY p.fecha DESC")
                while q.next():
                    pid = q.value(0)
                    label = q.value(1) or str(pid)
                    cmb_partido.addItem(label, pid)
            if cmb_jugador:
                cmb_jugador.clear()
                qj = QSqlQuery(db)
                qj.exec("SELECT id, nombre FROM participantes WHERE tipo_participante='Jugador' ORDER BY nombre")
                while qj.next():
                    jid = qj.value(0)
                    name = qj.value(1)
                    cmb_jugador.addItem(name, jid)
            if cmb_tipo and cmb_tipo.count() == 0:
                cmb_tipo.addItem("Gol")
                cmb_tipo.addItem("Tarjeta Amarilla")
                cmb_tipo.addItem("Tarjeta Roja")
        except Exception as e:
            print(f"Error cargando partidos/jugadores: {e}")
    def _guardar_evento(self):
        try:
            db = get_db_connection()
            cmb_partido = self.dialog.findChild(QComboBox, "cmbPartido")
            cmb_jugador = self.dialog.findChild(QComboBox, "cmbJugador")
            cmb_tipo = self.dialog.findChild(QComboBox, "cmbTipo")
            spin_minuto = self.dialog.findChild(QSpinBox, "spinMinuto")
            if not cmb_partido or cmb_partido.currentData() is None:
                QMessageBox.warning(self.dialog, "Validación", "Debe seleccionar un partido")
                return
            if not cmb_jugador or cmb_jugador.currentData() is None:
                QMessageBox.warning(self.dialog, "Validación", "Debe seleccionar un jugador")
                return
            if not cmb_tipo or not cmb_tipo.currentText():
                QMessageBox.warning(self.dialog, "Validación", "Debe seleccionar el tipo de evento")
                return
            participante_id = cmb_jugador.currentData() if cmb_jugador else None
            partido_id = cmb_partido.currentData() if cmb_partido else None
            tipo = cmb_tipo.currentText()
            if tipo == "Gol":
                query = QSqlQuery(db)
                query.prepare("""
                    INSERT INTO goles (participante_id, partido_id, minuto)
                    VALUES (?, ?, ?)
                """)
                query.addBindValue(participante_id)
                query.addBindValue(partido_id)
                query.addBindValue(spin_minuto.value() if spin_minuto else 0)
                executed = query.exec()
                if executed:
                    q_up = QSqlQuery(db)
                    q_up.prepare("UPDATE participantes SET goles = COALESCE(goles,0) + 1 WHERE id = ?")
                    q_up.addBindValue(participante_id)
                    q_up.exec()
                    q_part = QSqlQuery(db)
                    q_part.prepare("SELECT equipo1_id, equipo2_id FROM partidos WHERE id = ?")
                    q_part.addBindValue(partido_id)
                    if q_part.exec() and q_part.next():
                        eq1 = q_part.value(0)
                        eq2 = q_part.value(1)
                        q_pe = QSqlQuery(db)
                        q_pe.prepare("SELECT equipo_id FROM participantes WHERE id = ?")
                        q_pe.addBindValue(participante_id)
                        if q_pe.exec() and q_pe.next():
                            equipo_part = q_pe.value(0)
                            if equipo_part == eq1:
                                q_up2 = QSqlQuery(db)
                                q_up2.prepare("UPDATE partidos SET goles_equipo1 = COALESCE(goles_equipo1,0) + 1 WHERE id = ?")
                                q_up2.addBindValue(partido_id)
                                q_up2.exec()
                            elif equipo_part == eq2:
                                q_up2 = QSqlQuery(db)
                                q_up2.prepare("UPDATE partidos SET goles_equipo2 = COALESCE(goles_equipo2,0) + 1 WHERE id = ?")
                                q_up2.addBindValue(partido_id)
                                q_up2.exec()
            else:
                tipo_tarjeta = "Amarilla" if tipo == "Tarjeta Amarilla" else "Roja"
                query = QSqlQuery(db)
                query.prepare("""
                    INSERT INTO tarjetas (participante_id, partido_id, tipo, minuto)
                    VALUES (?, ?, ?, ?)
                """)
                query.addBindValue(participante_id)
                query.addBindValue(partido_id)
                query.addBindValue(tipo_tarjeta)
                query.addBindValue(spin_minuto.value() if spin_minuto else 0)
                executed = query.exec()
                if executed:
                    if tipo_tarjeta == 'Amarilla':
                        q_up = QSqlQuery(db)
                        q_up.prepare("UPDATE participantes SET tarjetas_amarillas = COALESCE(tarjetas_amarillas,0) + 1 WHERE id = ?")
                        q_up.addBindValue(participante_id)
                        q_up.exec()
                    else:
                        q_up = QSqlQuery(db)
                        q_up.prepare("UPDATE participantes SET tarjetas_rojas = COALESCE(tarjetas_rojas,0) + 1 WHERE id = ?")
                        q_up.addBindValue(participante_id)
                        q_up.exec()
            if 'executed' in locals():
                ok = executed
            else:
                ok = query.exec()
            if ok:
                QMessageBox.information(self.dialog, "Éxito", f"{tipo} registrado correctamente")
                self._limpiar_formulario()
                self.dialog.close()
            else:
                QMessageBox.critical(self.dialog, "Error", f"Error al guardar: {query.lastError().text()}")
        except Exception as e:
            QMessageBox.critical(self.dialog, "Error", f"Error inesperado: {str(e)}")
    def _limpiar_formulario(self):
        spin_minuto = self.dialog.findChild(QSpinBox, "spinMinuto")
        if spin_minuto:
            spin_minuto.setValue(0)
    def _cancelar(self):
        self.dialog.close()
    def show(self):
        if self.dialog:
            try:
                self._cargar_partidos_y_jugadores()
                self._aplicar_estilos()
            except Exception:
                pass
            self.dialog.show()
    def _aplicar_estilos(self):
        try:
            style_combobox = """
                QComboBox {
                    background-color:
                    color: black;
                    font-weight: bold;
                    border: 2px solid
                    border-radius: 4px;
                    padding: 4px;
                    font-size: 12pt;
                }
            """
            style_spinbox = """
                QSpinBox {
                    background-color:
                    color: black;
                    font-weight: bold;
                    border: 2px solid
                    border-radius: 4px;
                    padding: 4px;
                    font-size: 12pt;
                }
            """
            combos = self.dialog.findChildren(QComboBox)
            for cmb in combos:
                cmb.setStyleSheet(style_combobox)
            spinboxes = self.dialog.findChildren(QSpinBox)
            for spin in spinboxes:
                spin.setStyleSheet(style_spinbox)
        except Exception as e:
            print(f"Error aplicando estilos: {e}")
    def close(self):
        if self.dialog:
            self.dialog.close()
