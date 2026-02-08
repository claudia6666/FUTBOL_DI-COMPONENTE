import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QPushButton, QComboBox, QSpinBox, QMessageBox, QLabel
from PySide6.QtSql import QSqlQuery
from models.globals import get_db_connection
class FormResultado:
    def __init__(self, parent=None):
        ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_ui = os.path.join(ruta_base, "ui", "form_resultado.ui")
        self.partido_id = None
        if os.path.exists(ruta_ui):
            try:
                loader = QUiLoader()
                ui_file = QFile(ruta_ui)
                if ui_file.open(QIODevice.ReadOnly):
                    self.dialog = loader.load(ui_file, None)
                    ui_file.close()
                    if self.dialog:
                        self._conectar_botones_guardado()
                        print(f"FormResultado: .ui cargado desde {ruta_ui}")
                        return
            except Exception as e:
                print(f"Error al cargar {ruta_ui}: {e}")
        from PySide6.QtWidgets import QDialog
        self.dialog = QDialog(parent)
        self.dialog.setWindowTitle("Formulario de Resultado")
        self.dialog.setGeometry(100, 100, 600, 500)
        print("FormResultado: fallback usado")
    def cargar_partido(self, partido_id):
        self.partido_id = partido_id
        try:
            self._aplicar_estilos_goles()
            all_combos = self.dialog.findChildren(QComboBox)
            print(f"DEBUG: Todos los comboboxes encontrados: {[cb.objectName() for cb in all_combos]}")
            all_spinboxes = self.dialog.findChildren(QSpinBox)
            print(f"DEBUG: Todos los spinboxes encontrados: {[sb.objectName() for sb in all_spinboxes]}")
            db = get_db_connection()
            query = QSqlQuery(db)
            query.prepare("""
                SELECT p.id,
                       p.equipo1_id,
                       p.equipo2_id,
                       e1.nombre AS equipo1,
                       e2.nombre AS equipo2,
                       p.goles_equipo1,
                       p.goles_equipo2,
                       COALESCE(pa.nombre, 'Sin árbitro') AS arbitro
                FROM partidos p
                LEFT JOIN equipos e1 ON p.equipo1_id = e1.id
                LEFT JOIN equipos e2 ON p.equipo2_id = e2.id
                LEFT JOIN participantes pa ON p.arbitro_id = pa.id
                WHERE p.id = ?
            """)
            query.addBindValue(partido_id)
            if query.exec() and query.next():
                equipo1_id = query.value(1)
                equipo2_id = query.value(2)
                equipo1_nombre = query.value(3) or ''
                equipo2_nombre = query.value(4) or ''
                goles1 = query.value(5) if query.value(5) is not None else 0
                goles2 = query.value(6) if query.value(6) is not None else 0
                arbitro = query.value(7) or 'Sin árbitro'
                lbl_titulo = self.dialog.findChild(QLabel, "lblTitulo")
                if lbl_titulo:
                    lbl_titulo.setText(f"{equipo1_nombre} vs {equipo2_nombre}")
                query_equipos = QSqlQuery(db)
                query_equipos.exec("SELECT id, nombre FROM equipos ORDER BY nombre")
                equipos_dict = {}
                while query_equipos.next():
                    eq_id = query_equipos.value(0)
                    eq_nombre = query_equipos.value(1)
                    equipos_dict[eq_id] = eq_nombre
                print(f"DEBUG: equipos_dict = {equipos_dict}")
                combos = self.dialog.findChildren(QComboBox)
                print(f"DEBUG: Se encontraron {len(combos)} comboboxes")
                for i, cmb in enumerate(combos):
                    cmb.clear()
                    cmb.setEnabled(False)
                    for eq_id, eq_nombre in equipos_dict.items():
                        cmb.addItem(eq_nombre, eq_id)
                    print(f"DEBUG: ComboBox {i} ({cmb.objectName()}) cargado con {cmb.count()} items (DESHABILITADO en modo edición)")
                cmb_local = self.dialog.findChild(QComboBox, "cmbEquipoLocal")
                cmb_visitante = self.dialog.findChild(QComboBox, "cmbEquipoVisitante")
                if cmb_local:
                    idx = cmb_local.findData(equipo1_id)
                    if idx >= 0:
                        cmb_local.setCurrentIndex(idx)
                    print(f"DEBUG: cmbEquipoLocal seleccionado en índice {idx}")
                if cmb_visitante:
                    cmb_visitante.setEnabled(False)
                    cmb_visitante.show()
                    idx = cmb_visitante.findData(equipo2_id)
                    if idx >= 0:
                        cmb_visitante.setCurrentIndex(idx)
                    print(f"DEBUG: cmbEquipoVisitante encontrado y seleccionado en índice {idx} (DESHABILITADO)")
                else:
                    print(f"DEBUG: cmbEquipoVisitante no encontrado por nombre, buscando por posición")
                    combos_equipos = self.dialog.findChildren(QComboBox)
                    if len(combos_equipos) > 1:
                        cmb_visitante = combos_equipos[1]
                        cmb_visitante.setEnabled(False)
                        cmb_visitante.show()
                        if cmb_visitante.count() == 0:
                            for eq_id, eq_nombre in equipos_dict.items():
                                cmb_visitante.addItem(eq_nombre, eq_id)
                        idx = cmb_visitante.findData(equipo2_id)
                        if idx >= 0:
                            cmb_visitante.setCurrentIndex(idx)
                        print(f"DEBUG: Segundo combobox ({cmb_visitante.objectName()}) habilitado y seleccionado en índice {idx} (DESHABILITADO)")
                spin_goles_local = self.dialog.findChild(QSpinBox, "spinGolesLocal")
                if spin_goles_local:
                    spin_goles_local.setValue(int(goles1))
                    print(f"DEBUG: spinGolesLocal establecido a {goles1}")
                spin_goles_visitante = self.dialog.findChild(QSpinBox, "spinGolesVisitante")
                if spin_goles_visitante:
                    spin_goles_visitante.setValue(int(goles2))
                    print(f"DEBUG: spinGolesVisitante establecido a {goles2}")
                else:
                    spinboxes = self.dialog.findChildren(QSpinBox)
                    if len(spinboxes) > 1:
                        spinboxes[1].setValue(int(goles2))
                        print(f"DEBUG: Segundo spinbox establecido a {goles2}")
                print(f"Partido {partido_id} cargado: {equipo1_nombre} vs {equipo2_nombre}")
            else:
                QMessageBox.warning(self.dialog, "Error", f"No se encontró el partido {partido_id}")
        except Exception as e:
            print(f"Error al cargar partido: {e}")
            import traceback
            traceback.print_exc()
            QMessageBox.critical(self.dialog, "Error", f"Error al cargar partido: {str(e)}")
    def cargar_para_nuevo(self, equipo_local_id=None, equipo_visitante_id=None):
        try:
            self._aplicar_estilos_goles()
            db = get_db_connection()
            lbl_titulo = self.dialog.findChild(QLabel, "lblTitulo")
            if lbl_titulo:
                lbl_titulo.setText("Nuevo Resultado")
            query_equipos = QSqlQuery(db)
            query_equipos.exec("SELECT id, nombre FROM equipos ORDER BY nombre")
            equipos_dict = {}
            while query_equipos.next():
                eq_id = query_equipos.value(0)
                eq_nombre = query_equipos.value(1)
                equipos_dict[eq_id] = eq_nombre
            combos = self.dialog.findChildren(QComboBox)
            for cmb in combos:
                cmb.clear()
                cmb.setEnabled(True)
                for eq_id, eq_nombre in equipos_dict.items():
                    cmb.addItem(eq_nombre, eq_id)
            cmb_local = self.dialog.findChild(QComboBox, "cmbEquipoLocal")
            cmb_visitante = self.dialog.findChild(QComboBox, "cmbEquipoVisitante")
            if cmb_local and equipo_local_id is not None:
                idx = cmb_local.findData(equipo_local_id)
                if idx >= 0:
                    cmb_local.setCurrentIndex(idx)
            if cmb_visitante and equipo_visitante_id is not None:
                cmb_visitante.setEnabled(True)
                cmb_visitante.show()
                idx = cmb_visitante.findData(equipo_visitante_id)
                if idx >= 0:
                    cmb_visitante.setCurrentIndex(idx)
            elif not cmb_visitante and len(combos) > 1:
                cmb_visitante = combos[1]
                cmb_visitante.setEnabled(True)
                cmb_visitante.show()
                if equipo_visitante_id is not None:
                    idx = cmb_visitante.findData(equipo_visitante_id)
                    if idx >= 0:
                        cmb_visitante.setCurrentIndex(idx)
            spin_goles_local = self.dialog.findChild(QSpinBox, "spinGolesLocal")
            if spin_goles_local:
                spin_goles_local.setValue(0)
            spin_goles_visitante = self.dialog.findChild(QSpinBox, "spinGolesVisitante")
            if spin_goles_visitante:
                spin_goles_visitante.setValue(0)
            self.partido_id = None
        except Exception as e:
            print(f"Error en cargar_para_nuevo: {e}")
    def _conectar_botones_guardado(self):
        try:
            buttons = self.dialog.findChildren(QPushButton)
            for btn in buttons:
                if "Save" in btn.text() or "Guardar" in btn.text():
                    btn.clicked.connect(self._guardar_resultado)
                elif "Cancel" in btn.text() or "Cancelar" in btn.text():
                    btn.clicked.connect(self._cancelar)
        except Exception as e:
            print(f"Error al conectar botones de guardado: {e}")
    def _aplicar_estilos_goles(self):
        try:
            spin_local = self.dialog.findChild(QSpinBox, "spinGolesLocal")
            spin_visitante = self.dialog.findChild(QSpinBox, "spinGolesVisitante")
            cmb_local = self.dialog.findChild(QComboBox, "cmbEquipoLocal")
            cmb_visitante = self.dialog.findChild(QComboBox, "cmbEquipoVisitante")
            style_local = """
                QSpinBox, QComboBox {
                    background-color: white;
                    color: black;
                    font-weight: bold;
                    border: 2px solid #cccccc;
                    border-radius: 4px;
                    padding: 4px;
                    font-size: 14pt;
                }
            """
            style_visitante = """
                QSpinBox, QComboBox {
                    background-color: white;
                    color: black;
                    font-weight: bold;
                    border: 2px solid #cccccc;
                    border-radius: 4px;
                    padding: 4px;
                    font-size: 14pt;
                }
            """
            if spin_local:
                spin_local.setStyleSheet(style_local)
            if cmb_local:
                cmb_local.setStyleSheet(style_local)
            if spin_visitante:
                spin_visitante.setStyleSheet(style_visitante)
            if cmb_visitante:
                cmb_visitante.setStyleSheet(style_visitante)
            combos = self.dialog.findChildren(QComboBox)
            if len(combos) > 1 and not cmb_visitante:
                combos[1].setStyleSheet(style_visitante)
        except Exception as e:
            print(f"Error aplicando estilos: {e}")
    def _guardar_resultado(self):
        try:
            db = get_db_connection()
            cmb_local = self.dialog.findChild(QComboBox, "cmbEquipoLocal")
            cmb_visitante = self.dialog.findChild(QComboBox, "cmbEquipoVisitante")
            equipo1_id = None
            equipo2_id = None
            if cmb_local:
                equipo1_id = cmb_local.currentData()
            if cmb_visitante:
                equipo2_id = cmb_visitante.currentData()
            spin_goles_local = self.dialog.findChild(QSpinBox, "spinGolesLocal")
            spin_goles_visitante = self.dialog.findChild(QSpinBox, "spinGolesVisitante")
            goles_local = spin_goles_local.value() if spin_goles_local else 0
            goles_visitante = spin_goles_visitante.value() if spin_goles_visitante else 0
            if self.partido_id is None:
                if equipo1_id is None or equipo2_id is None:
                    QMessageBox.warning(self.dialog, "Validación", "Debe seleccionar ambos equipos")
                    return
                q_ins = QSqlQuery(db)
                q_ins.prepare("""
                    INSERT INTO partidos (equipo1_id, equipo2_id, goles_equipo1, goles_equipo2, estado)
                    VALUES (?, ?, ?, ?, 'Finalizado')
                """)
                q_ins.addBindValue(equipo1_id)
                q_ins.addBindValue(equipo2_id)
                q_ins.addBindValue(int(goles_local))
                q_ins.addBindValue(int(goles_visitante))
                if not q_ins.exec():
                    QMessageBox.critical(self.dialog, "Error", f"Error al insertar partido: {q_ins.lastError().text()}")
                    return
                q_last = QSqlQuery(db)
                if q_last.exec("SELECT last_insert_rowid()") and q_last.next():
                    self.partido_id = q_last.value(0)
                try:
                    self._apply_clasificacion(db, equipo1_id, equipo2_id, int(goles_local), int(goles_visitante))
                except Exception as e:
                    print(f"Error aplicando clasificación en inserción: {e}")
                QMessageBox.information(self.dialog, "Éxito", "Resultado creado y guardado correctamente")
                self._limpiar_formulario()
                self.dialog.close()
                return
            q_prev = QSqlQuery(db)
            q_prev.prepare("""
                SELECT equipo1_id, equipo2_id, goles_equipo1, goles_equipo2, estado
                FROM partidos WHERE id = ?
            """)
            q_prev.addBindValue(self.partido_id)
            prev = None
            if q_prev.exec() and q_prev.next():
                prev = {
                    'equipo1_id': q_prev.value(0),
                    'equipo2_id': q_prev.value(1),
                    'goles1': q_prev.value(2) or 0,
                    'goles2': q_prev.value(3) or 0,
                    'estado': q_prev.value(4)
                }
            query = QSqlQuery(db)
            query.prepare("""
                UPDATE partidos 
                SET goles_equipo1 = ?, goles_equipo2 = ?, estado = 'Finalizado'
                WHERE id = ?
            """)
            query.addBindValue(goles_local)
            query.addBindValue(goles_visitante)
            query.addBindValue(self.partido_id)
            if query.exec():
                try:
                    if prev and prev.get('estado') == 'Finalizado':
                        self._revert_clasificacion(db, prev['equipo1_id'], prev['equipo2_id'], prev['goles1'], prev['goles2'])
                    if prev:
                        self._apply_clasificacion(db, prev['equipo1_id'], prev['equipo2_id'], int(goles_local), int(goles_visitante))
                except Exception as e:
                    print(f"Error actualizando clasificación: {e}")
                QMessageBox.information(self.dialog, "Éxito", "Resultado guardado correctamente")
                self._limpiar_formulario()
                self.dialog.close()
            else:
                QMessageBox.critical(self.dialog, "Error", f"Error al guardar: {query.lastError().text()}")
        except Exception as e:
            QMessageBox.critical(self.dialog, "Error", f"Error inesperado: {str(e)}")
    def _apply_clasificacion(self, db, equipo1_id, equipo2_id, goles1, goles2):
        try:
            q = QSqlQuery(db)
            q.prepare("UPDATE clasificacion SET partidos_jugados = partidos_jugados + 1 WHERE equipo_id = ?")
            q.addBindValue(equipo1_id); q.exec()
            q.clear(); q.addBindValue(equipo2_id); q.exec()
            q.prepare("UPDATE clasificacion SET goles_favor = goles_favor + ?, goles_contra = goles_contra + ? WHERE equipo_id = ?")
            q.addBindValue(goles1); q.addBindValue(goles2); q.addBindValue(equipo1_id); q.exec()
            q.clear(); q.addBindValue(goles2); q.addBindValue(goles1); q.addBindValue(equipo2_id); q.exec()
            q.prepare("UPDATE clasificacion SET diferencia_goles = goles_favor - goles_contra WHERE equipo_id = ?")
            q.addBindValue(equipo1_id); q.exec()
            q.clear(); q.addBindValue(equipo2_id); q.exec()
            if goles1 > goles2:
                q.prepare("UPDATE clasificacion SET partidos_ganados = partidos_ganados + 1, puntos = puntos + 3 WHERE equipo_id = ?")
                q.addBindValue(equipo1_id); q.exec()
                q.clear(); q.exec("UPDATE clasificacion SET partidos_perdidos = partidos_perdidos + 1 WHERE equipo_id = %s" % equipo2_id)
            elif goles1 < goles2:
                q.prepare("UPDATE clasificacion SET partidos_ganados = partidos_ganados + 1, puntos = puntos + 3 WHERE equipo_id = ?")
                q.addBindValue(equipo2_id); q.exec()
                q.clear(); q.exec("UPDATE clasificacion SET partidos_perdidos = partidos_perdidos + 1 WHERE equipo_id = %s" % equipo1_id)
            else:
                q.prepare("UPDATE clasificacion SET partidos_empatados = partidos_empatados + 1, puntos = puntos + 1 WHERE equipo_id = ?")
                q.addBindValue(equipo1_id); q.exec()
                q.clear(); q.addBindValue(equipo2_id); q.exec()
        except Exception as e:
            print(f"Error en _apply_clasificacion: {e}")
    def _revert_clasificacion(self, db, equipo1_id, equipo2_id, goles1, goles2):
        try:
            q = QSqlQuery(db)
            q.exec("UPDATE clasificacion SET partidos_jugados = CASE WHEN partidos_jugados>0 THEN partidos_jugados-1 ELSE 0 END WHERE equipo_id = %s" % equipo1_id)
            q.exec("UPDATE clasificacion SET partidos_jugados = CASE WHEN partidos_jugados>0 THEN partidos_jugados-1 ELSE 0 END WHERE equipo_id = %s" % equipo2_id)
            q.exec("UPDATE clasificacion SET goles_favor = CASE WHEN goles_favor>=%s THEN goles_favor-%s ELSE 0 END, goles_contra = CASE WHEN goles_contra>=%s THEN goles_contra-%s ELSE 0 END WHERE equipo_id = %s" % (goles1, goles1, goles2, goles2, equipo1_id))
            q.exec("UPDATE clasificacion SET goles_favor = CASE WHEN goles_favor>=%s THEN goles_favor-%s ELSE 0 END, goles_contra = CASE WHEN goles_contra>=%s THEN goles_contra-%s ELSE 0 END WHERE equipo_id = %s" % (goles2, goles2, goles1, goles1, equipo2_id))
            q.exec("UPDATE clasificacion SET diferencia_goles = goles_favor - goles_contra WHERE equipo_id = %s" % equipo1_id)
            q.exec("UPDATE clasificacion SET diferencia_goles = goles_favor - goles_contra WHERE equipo_id = %s" % equipo2_id)
            if goles1 > goles2:
                q.exec("UPDATE clasificacion SET partidos_ganados = CASE WHEN partidos_ganados>0 THEN partidos_ganados-1 ELSE 0 END, puntos = CASE WHEN puntos>=3 THEN puntos-3 ELSE 0 END WHERE equipo_id = %s" % equipo1_id)
                q.exec("UPDATE clasificacion SET partidos_perdidos = CASE WHEN partidos_perdidos>0 THEN partidos_perdidos-1 ELSE 0 END WHERE equipo_id = %s" % equipo2_id)
            elif goles1 < goles2:
                q.exec("UPDATE clasificacion SET partidos_ganados = CASE WHEN partidos_ganados>0 THEN partidos_ganados-1 ELSE 0 END, puntos = CASE WHEN puntos>=3 THEN puntos-3 ELSE 0 END WHERE equipo_id = %s" % equipo2_id)
                q.exec("UPDATE clasificacion SET partidos_perdidos = CASE WHEN partidos_perdidos>0 THEN partidos_perdidos-1 ELSE 0 END WHERE equipo_id = %s" % equipo1_id)
            else:
                q.exec("UPDATE clasificacion SET partidos_empatados = CASE WHEN partidos_empatados>0 THEN partidos_empatados-1 ELSE 0 END, puntos = CASE WHEN puntos>0 THEN puntos-1 ELSE 0 END WHERE equipo_id = %s" % equipo1_id)
                q.exec("UPDATE clasificacion SET partidos_empatados = CASE WHEN partidos_empatados>0 THEN partidos_empatados-1 ELSE 0 END, puntos = CASE WHEN puntos>0 THEN puntos-1 ELSE 0 END WHERE equipo_id = %s" % equipo2_id)
        except Exception as e:
            print(f"Error en _revert_clasificacion: {e}")
    def _limpiar_formulario(self):
        spin_goles_local = self.dialog.findChild(QSpinBox, "spinGolesLocal")
        if spin_goles_local:
            spin_goles_local.setValue(0)
        spin_goles_visitante = self.dialog.findChild(QSpinBox, "spinGolesVisitante")
        if spin_goles_visitante:
            spin_goles_visitante.setValue(0)
        cmb_local = self.dialog.findChild(QComboBox, "cmbEquipoLocal")
        if cmb_local:
            cmb_local.setCurrentIndex(0)
        cmb_visitante = self.dialog.findChild(QComboBox, "cmbEquipoVisitante")
        if cmb_visitante:
            cmb_visitante.setCurrentIndex(0)
        self.partido_id = None
    def _cancelar(self):
        self._limpiar_formulario()
        self.dialog.close()
    def show(self):
        if self.dialog:
            self.dialog.show()
    def close(self):
        if self.dialog:
            self.dialog.close()
