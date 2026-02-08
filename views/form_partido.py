import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
from PySide6.QtWidgets import QPushButton, QComboBox, QSpinBox, QDateEdit, QTimeEdit, QMessageBox
from PySide6.QtSql import QSqlQuery
from models.globals import get_db_connection
try:
    from modules.reloj_digital.views.AppReloj import TestWindow
except Exception:
    TestWindow = None
class FormPartido:
    def __init__(self, parent=None):
        ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_ui = os.path.join(ruta_base, "ui", "form_partido.ui")
        if os.path.exists(ruta_ui):
            try:
                loader = QUiLoader()
                ui_file = QFile(ruta_ui)
                if ui_file.open(QIODevice.ReadOnly):
                    self.dialog = loader.load(ui_file, None)
                    ui_file.close()
                    if self.dialog:
                        self._conectar_botones_guardado()
                        try:
                            if TestWindow is not None:
                                btn_reloj = QPushButton("Reloj")
                                btn_reloj.setObjectName("btnReloj")
                                btn_reloj.clicked.connect(self._open_reloj)
                                main_layout = self.dialog.layout()
                                if main_layout:
                                    main_layout.addWidget(btn_reloj)
                        except Exception:
                            pass
                        try:
                            self._cargar_arbitros()
                            self._cargar_partidos_programados()
                        except Exception as e:
                            print(f"FormPartido: error cargando datos iniciales: {e}")
                        print(f"FormPartido: .ui cargado desde {ruta_ui}")
                        return
            except Exception as e:
                print(f"Error al cargar {ruta_ui}: {e}")
        from PySide6.QtWidgets import QDialog
        self.dialog = QDialog(parent)
        self.dialog.setWindowTitle("Formulario de Partido")
        self.dialog.setGeometry(100, 100, 600, 500)
        print("FormPartido: fallback usado")
    def _conectar_botones_guardado(self):
        try:
            buttons = self.dialog.findChildren(QPushButton)
            for btn in buttons:
                if "Save" in btn.text() or "Guardar" in btn.text():
                    btn.clicked.connect(self._guardar_partido)
                elif "Cancel" in btn.text() or "Cancelar" in btn.text():
                    btn.clicked.connect(self._cancelar)
        except Exception as e:
            print(f"Error al conectar botones de guardado: {e}")
    def _guardar_partido(self):
        try:
            db = get_db_connection()
            cmb_equipo1 = self.dialog.findChild(QComboBox, "cmbEquipoLocal")
            cmb_equipo2 = self.dialog.findChild(QComboBox, "cmbEquipoVisitante")
            cmb_arbitro = self.dialog.findChild(QComboBox, "cmbArbitro")
            cmb_eliminatoria = self.dialog.findChild(QComboBox, "cmbEliminatoria")
            date_fecha = self.dialog.findChild(QDateEdit, "dateFecha")
            time_hora = self.dialog.findChild(QTimeEdit, "timeHora")
            if cmb_equipo1 and cmb_equipo2 and cmb_equipo1.currentData() == cmb_equipo2.currentData():
                QMessageBox.warning(self.dialog, "Validación", "Los equipos deben ser diferentes")
                return
            equipo1_id = cmb_equipo1.currentData() if cmb_equipo1 else None
            equipo2_id = cmb_equipo2.currentData() if cmb_equipo2 else None
            arbitro_id = cmb_arbitro.currentData() if cmb_arbitro else None
            ronda = cmb_eliminatoria.currentText() if cmb_eliminatoria else ""
            cmb_partidos = self.dialog.findChild(QComboBox, "cmbPartidoSeleccion")
            partido_id = cmb_partidos.currentData() if cmb_partidos else None
            if partido_id:
                query = QSqlQuery(db)
                query.prepare("""
                    UPDATE partidos
                    SET equipo1_id = ?, equipo2_id = ?, arbitro_id = ?, fecha = ?, hora = ?, ronda = ?, estado = 'Programado'
                    WHERE id = ?
                """)
                query.addBindValue(equipo1_id)
                query.addBindValue(equipo2_id)
                query.addBindValue(arbitro_id)
                query.addBindValue(date_fecha.date().toString("yyyy-MM-dd") if date_fecha else "")
                query.addBindValue(time_hora.time().toString("HH:mm") if time_hora else "")
                query.addBindValue(ronda)
                query.addBindValue(partido_id)
            else:
                query = QSqlQuery(db)
                query.prepare("""
                    INSERT INTO partidos (equipo1_id, equipo2_id, arbitro_id, goles_equipo1, goles_equipo2, fecha, hora, ronda, estado)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'Programado')
                """)
                query.addBindValue(equipo1_id)
                query.addBindValue(equipo2_id)
                query.addBindValue(arbitro_id)
                query.addBindValue(0)
                query.addBindValue(0)
                query.addBindValue(date_fecha.date().toString("yyyy-MM-dd") if date_fecha else "")
                query.addBindValue(time_hora.time().toString("HH:mm") if time_hora else "")
                query.addBindValue(ronda)
            if query.exec():
                QMessageBox.information(self.dialog, "Éxito", "Partido guardado correctamente")
                self._limpiar_formulario()
                self.dialog.close()
            else:
                QMessageBox.critical(self.dialog, "Error", f"Error al guardar: {query.lastError().text()}")
        except Exception as e:
            QMessageBox.critical(self.dialog, "Error", f"Error inesperado: {str(e)}")
    def _cargar_arbitros(self):
        try:
            cmb = self.dialog.findChild(QComboBox, "cmbArbitro")
            if not cmb:
                return
            db = get_db_connection()
            query = QSqlQuery(db)
            query.exec("SELECT id, nombre FROM participantes WHERE tipo_participante = 'Arbitro' ORDER BY nombre")
            cmb.clear()
            cmb.addItem("- Sin asignar -", None)
            while query.next():
                cmb.addItem(query.value(1), query.value(0))
        except Exception as e:
            print(f"Error cargando árbitros: {e}")
    def _cargar_partidos_programados(self):
        try:
            db = get_db_connection()
            query = QSqlQuery(db)
            query.exec("""
                SELECT p.id, e1.nombre, e2.nombre, p.fecha, p.hora, p.equipo1_id, p.equipo2_id, p.arbitro_id
                FROM partidos p
                JOIN equipos e1 ON p.equipo1_id = e1.id
                JOIN equipos e2 ON p.equipo2_id = e2.id
                WHERE p.estado = 'Programado'
                ORDER BY p.fecha, p.hora
            """)
            partidos = []
            while query.next():
                pid = query.value(0)
                local = query.value(1)
                visita = query.value(2)
                fecha = query.value(3)
                hora = query.value(4)
                eq1 = query.value(5)
                eq2 = query.value(6)
                arb = query.value(7)
                label = f"{pid} - {local} vs {visita} ({fecha}) {hora if hora else ''}"
                partidos.append((pid, label, eq1, eq2, arb))
            cmb_partidos = self.dialog.findChild(QComboBox, "cmbPartidoSeleccion")
            if not cmb_partidos:
                from PySide6.QtWidgets import QHBoxLayout, QWidget
                cmb_partidos = QComboBox(self.dialog)
                cmb_partidos.setObjectName("cmbPartidoSeleccion")
                cmb_partidos.setMinimumWidth(400)
                main_layout = self.dialog.layout()
                if main_layout:
                    container = QWidget(self.dialog)
                    h = QHBoxLayout(container)
                    h.addWidget(cmb_partidos)
                    main_layout.insertWidget(1, container)
            cmb_partidos.clear()
            cmb_partidos.addItem("- Selecciona un partido programado -", None)
            for pid, label, eq1, eq2, arb in partidos:
                cmb_partidos.addItem(label, pid)
            q_equipos = QSqlQuery(db)
            q_equipos.exec("SELECT id, nombre FROM equipos ORDER BY nombre")
            cmb_local = self.dialog.findChild(QComboBox, "cmbEquipoLocal")
            cmb_visit = self.dialog.findChild(QComboBox, "cmbEquipoVisitante")
            if cmb_local:
                cmb_local.clear()
                cmb_local.addItem("- Selecciona -", None)
                while q_equipos.next():
                    cmb_local.addItem(q_equipos.value(1), q_equipos.value(0))
            q_equipos.exec("SELECT id, nombre FROM equipos ORDER BY nombre")
            if cmb_visit:
                cmb_visit.clear()
                cmb_visit.addItem("- Selecciona -", None)
                while q_equipos.next():
                    cmb_visit.addItem(q_equipos.value(1), q_equipos.value(0))
            try:
                cmb_partidos.currentIndexChanged.disconnect(self._on_partido_seleccionado)
            except Exception:
                pass
            cmb_partidos.currentIndexChanged.connect(self._on_partido_seleccionado)
        except Exception as e:
            print(f"Error cargando partidos programados: {e}")
    def _on_partido_seleccionado(self, index):
        try:
            cmb_partidos = self.dialog.findChild(QComboBox, "cmbPartidoSeleccion")
            if not cmb_partidos:
                return
            partido_id = cmb_partidos.currentData()
            if not partido_id:
                return
            db = get_db_connection()
            query = QSqlQuery(db)
            query.prepare("SELECT equipo1_id, equipo2_id, fecha, hora, arbitro_id FROM partidos WHERE id = ?")
            query.addBindValue(partido_id)
            if not query.exec() or not query.next():
                return
            eq1 = query.value(0)
            eq2 = query.value(1)
            fecha = query.value(2)
            hora = query.value(3)
            arb = query.value(4)
            cmb_local = self.dialog.findChild(QComboBox, "cmbEquipoLocal")
            cmb_visit = self.dialog.findChild(QComboBox, "cmbEquipoVisitante")
            if cmb_local:
                for i in range(cmb_local.count()):
                    if cmb_local.itemData(i) == eq1:
                        cmb_local.setCurrentIndex(i)
                        break
            if cmb_visit:
                for i in range(cmb_visit.count()):
                    if cmb_visit.itemData(i) == eq2:
                        cmb_visit.setCurrentIndex(i)
                        break
            date_fecha = self.dialog.findChild(QDateEdit, "dateFecha")
            time_hora = self.dialog.findChild(QTimeEdit, "timeHora")
            if date_fecha and fecha:
                from PySide6.QtCore import QDate
                try:
                    parts = str(fecha).split("-")
                    date_fecha.setDate(QDate(int(parts[0]), int(parts[1]), int(parts[2])))
                except Exception:
                    pass
            if time_hora and hora:
                from PySide6.QtCore import QTime
                try:
                    hhmm = str(hora).split(":")
                    time_hora.setTime(QTime(int(hhmm[0]), int(hhmm[1])))
                except Exception:
                    pass
            cmb_arb = self.dialog.findChild(QComboBox, "cmbArbitro")
            if cmb_arb and arb:
                for i in range(cmb_arb.count()):
                    if cmb_arb.itemData(i) == arb:
                        cmb_arb.setCurrentIndex(i)
                        break
        except Exception as e:
            print(f"Error al seleccionar partido: {e}")
    def show_for_assign(self, arbitro_id=None):
        if self.dialog:
            try:
                self._cargar_arbitros()
                self._cargar_partidos_programados()
            except Exception:
                pass
            if arbitro_id is not None:
                cmb = self.dialog.findChild(QComboBox, "cmbArbitro")
                if cmb:
                    for i in range(cmb.count()):
                        if cmb.itemData(i) == arbitro_id:
                            cmb.setCurrentIndex(i)
                            break
            self.dialog.setWindowTitle("Asignar árbitro a partido")
            self.dialog.show()
    def _cancelar(self):
        self.dialog.close()

    def _open_reloj(self):
        try:
            if TestWindow is None:
                QMessageBox.warning(self.dialog, "Reloj no disponible", "El módulo del reloj no está disponible.")
                return
            self.reloj_window = TestWindow()
            try:
                self.reloj_window.setWindowModality(Qt.ApplicationModal)
            except Exception:
                pass
            self.reloj_window.show()
            self.reloj_window.raise_()
            self.reloj_window.activateWindow()
        except Exception as e:
            print(f"Error abriendo el reloj: {e}")
    def _limpiar_formulario(self):
        cmb_local = self.dialog.findChild(QComboBox, "cmbEquipoLocal")
        if cmb_local and cmb_local.count() > 0:
            cmb_local.setCurrentIndex(0)
        cmb_visitante = self.dialog.findChild(QComboBox, "cmbEquipoVisitante")
        if cmb_visitante and cmb_visitante.count() > 0:
            cmb_visitante.setCurrentIndex(0)
        cmb_arbitro = self.dialog.findChild(QComboBox, "cmbArbitro")
        if cmb_arbitro and cmb_arbitro.count() > 0:
            cmb_arbitro.setCurrentIndex(0)
        date_fecha = self.dialog.findChild(QDateEdit, "dateFecha")
        if date_fecha:
            from PySide6.QtCore import QDate
            date_fecha.setDate(QDate.currentDate())
        time_hora = self.dialog.findChild(QTimeEdit, "timeHora")
        if time_hora:
            from PySide6.QtCore import QTime
            time_hora.setTime(QTime(16, 0))
    def show(self):
        if self.dialog:
            try:
                self._cargar_arbitros()
                self._cargar_partidos_programados()
            except Exception:
                pass
            self._limpiar_formulario()
            self.dialog.setWindowTitle("Formulario de Partido")
            self.dialog.show()
    def show_for_edit(self):
        if self.dialog:
            self.dialog.setWindowTitle("EDITAR PARTIDO")
            self.dialog.show()
    def close(self):
        if self.dialog:
            self.dialog.close()
