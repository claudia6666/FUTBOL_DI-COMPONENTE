from PySide6.QtWidgets import QDialog, QTableWidgetItem, QTreeWidgetItem, QMessageBox
from PySide6.QtSql import QSqlQuery
from PySide6.QtCore import Qt
from widgets.ui_resultados import Ui_DialogResultados
from views.form_resultado import FormResultado
from views.form_goles_tarjetas import FormGolesTarjetas
from views.form_participante import FormParticipante
from models.globals import get_db_connection
class Resultados(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogResultados()
        self.ui.setupUi(self)
        self.form_resultado_window = FormResultado()
        self.form_goles_tarjetas_window = FormGolesTarjetas()
        self.ui.buttonBox.rejected.connect(self.close)
        self.ui.btnEditarPartido.clicked.connect(self.editar_resultado)
        self.ui.btnEliminarPartido.clicked.connect(self.eliminar_resultado)
        self.ui.btnRegistrarGolesTarjetas.clicked.connect(self._abrir_formulario_goles_tarjetas)
        self.ui.btnEditarJugador.clicked.connect(self.editar_jugador)
        self.ui.btnEliminarJugador.clicked.connect(self.eliminar_jugador)
        self._cargar_resultados()
        self._cargar_jugadores()
        self._cargar_clasificacion()
        try:
            table = getattr(self.ui, 'tableJugadores', None)
            if table:
                table.setSortingEnabled(True)
                header = table.horizontalHeader()
                header.sectionClicked.connect(self._on_header_clicked)
        except Exception:
            pass
        try:
            btn_editar = getattr(self.ui, 'btnEditarJugador', None)
            if btn_editar:
                btn_editar.hide()
        except Exception:
            pass
        try:
            tab_widget = getattr(self.ui, 'tabWidgetResultados', None)
            tab_clasificacion = getattr(self.ui, 'tabClasificacion', None)
            if tab_widget and tab_clasificacion:
                index = tab_widget.indexOf(tab_clasificacion)
                if index >= 0:
                    tab_widget.removeTab(index)
        except Exception:
            pass
    def _abrir_formulario_resultado(self):
        tree = self.ui.treePartidos
        selected_items = tree.selectedItems() if tree is not None else []
        try:
            self.form_resultado_window.dialog.finished.disconnect()
        except Exception:
            pass
        self.form_resultado_window.dialog.finished.connect(self._refresh_all)
        if selected_items:
            partido_id = selected_items[0].data(0, Qt.UserRole)
            self.form_resultado_window.cargar_partido(partido_id)
            self.form_resultado_window.show()
            return
        clas = getattr(self.ui, 'treeClasificacion', None)
        if clas:
            sel_clas = clas.selectedItems()
            if sel_clas:
                equipo_id = sel_clas[0].data(0, Qt.UserRole)
                self.form_resultado_window.cargar_para_nuevo(equipo_local_id=equipo_id)
                self.form_resultado_window.show()
                return
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.warning(self, "Validación", "Debe seleccionar un partido o un equipo")
    def _abrir_formulario_goles_tarjetas(self):
        try:
            self.form_goles_tarjetas_window.dialog.finished.disconnect()
        except:
            pass
        self.form_goles_tarjetas_window.dialog.finished.connect(self._refresh_all)
        self.form_goles_tarjetas_window.show()
    def _cargar_resultados(self):
        try:
            from PySide6.QtGui import QColor
            db = get_db_connection()
            tree = getattr(self.ui, 'treePartidos', None)
            if tree is None:
                return
            tree.clear()
            tree.setColumnCount(5)
            tree.setHeaderLabels(["Partido", "Goles E1", "Goles E2", "Árbitro", "Eliminatoria"])            
            query = QSqlQuery(db)
            query.exec("""
                SELECT p.id,
                       COALESCE(e1.nombre, '') || ' vs ' || COALESCE(e2.nombre, '') AS partido,
                       p.goles_equipo1,
                       p.goles_equipo2,
                       COALESCE(pa.nombre, 'Sin árbitro') AS arbitro,
                       p.ronda
                FROM partidos p
                LEFT JOIN equipos e1 ON p.equipo1_id = e1.id
                LEFT JOIN equipos e2 ON p.equipo2_id = e2.id
                LEFT JOIN participantes pa ON p.arbitro_id = pa.id
                ORDER BY p.fecha DESC
            """)
            while query.next():
                partido_id = query.value(0)
                partido_nombre = query.value(1) or ''
                goles1 = query.value(2)
                goles2 = query.value(3)
                arbitro = query.value(4) or 'Sin árbitro'
                ronda = query.value(5) or ''
                item = QTreeWidgetItem([str(partido_nombre),
                                        str(goles1) if goles1 is not None else '',
                                        str(goles2) if goles2 is not None else '',
                                        str(arbitro),
                                        str(ronda)])
                item.setData(0, Qt.UserRole, partido_id)
                item.setTextAlignment(1, Qt.AlignCenter)
                item.setTextAlignment(2, Qt.AlignCenter)
                tree.addTopLevelItem(item)
        except Exception as e:
            print(f"Error al cargar resultados: {e}")
    def _cargar_jugadores(self):
        try:
            db = get_db_connection()
            table = getattr(self.ui, 'tableJugadores', None)
            if table is None:
                return
            table.setRowCount(0)
            query = QSqlQuery(db)
            query.exec("""
                SELECT pa.id,
                       pa.nombre,
                       COALESCE(e.nombre, 'Sin equipo') AS equipo,
                       COALESCE((SELECT COUNT(*) FROM goles g2 WHERE g2.participante_id = pa.id), 0) AS goles,
                       COALESCE(SUM(CASE WHEN t.tipo = 'Amarilla' THEN 1 ELSE 0 END), 0) AS tarjetas_amarillas,
                       COALESCE(SUM(CASE WHEN t.tipo = 'Roja' THEN 1 ELSE 0 END), 0) AS tarjetas_rojas
                FROM participantes pa
                LEFT JOIN equipos e ON pa.equipo_id = e.id
                LEFT JOIN tarjetas t ON pa.id = t.participante_id
                WHERE pa.tipo_participante = 'Jugador'
                GROUP BY pa.id, pa.nombre, e.nombre
                ORDER BY pa.nombre ASC
            """)
            row = 0
            while query.next():
                tabla_id = query.value(0)
                nombre = query.value(1) or ''
                equipo = query.value(2) or 'Sin equipo'
                goles = query.value(3) or 0
                tarjetas_amarillas = query.value(4) or 0
                tarjetas_rojas = query.value(5) or 0
                table.insertRow(row)
                item_id = QTableWidgetItem(str(tabla_id))
                item_id.setData(Qt.EditRole, int(tabla_id))
                item_nombre = QTableWidgetItem(str(nombre))
                item_nombre.setData(Qt.EditRole, str(nombre))
                item_equipo = QTableWidgetItem(str(equipo))
                item_equipo.setData(Qt.EditRole, str(equipo))
                item_goles = QTableWidgetItem(str(goles))
                item_goles.setData(Qt.EditRole, int(goles))
                item_ta = QTableWidgetItem(str(tarjetas_amarillas))
                item_ta.setData(Qt.EditRole, int(tarjetas_amarillas))
                item_tr = QTableWidgetItem(str(tarjetas_rojas))
                item_tr.setData(Qt.EditRole, int(tarjetas_rojas))
                items = [item_id, item_nombre, item_equipo, item_goles, item_ta, item_tr]
                for col, item in enumerate(items):
                    item.setData(Qt.UserRole, tabla_id)
                    item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row, col, item)
                row += 1
        except Exception as e:
            print(f"Error al cargar jugadores: {e}")
    def _cargar_clasificacion(self):
        try:
            db = get_db_connection()
            tree = getattr(self.ui, 'treeClasificacion', None)
            if tree is None:
                return
            tree.clear()
            tree.setColumnCount(9)
            tree.setHeaderLabels(["Equipo", "PJ", "PG", "PE", "PP", "GF", "GC", "DIF", "Puntos"])            
            q = QSqlQuery(db)
            q.exec("""
                SELECT c.equipo_id, COALESCE(e.nombre,'') AS equipo, c.partidos_jugados, c.partidos_ganados,
                       c.partidos_empatados, c.partidos_perdidos, c.goles_favor, c.goles_contra, c.diferencia_goles, c.puntos
                FROM clasificacion c
                LEFT JOIN equipos e ON c.equipo_id = e.id
                ORDER BY c.puntos DESC, c.diferencia_goles DESC, c.goles_favor DESC
            """)
            while q.next():
                equipo_id = q.value(0)
                nombre = q.value(1) or ''
                pj = q.value(2) or 0
                pg = q.value(3) or 0
                pe = q.value(4) or 0
                pp = q.value(5) or 0
                gf = q.value(6) or 0
                gc = q.value(7) or 0
                dif = q.value(8) or 0
                pts = q.value(9) or 0
                item = QTreeWidgetItem([str(nombre), str(pj), str(pg), str(pe), str(pp), str(gf), str(gc), str(dif), str(pts)])
                item.setData(0, Qt.UserRole, equipo_id)
                for i in range(1, 9):
                    item.setTextAlignment(i, Qt.AlignCenter)
                tree.addTopLevelItem(item)
        except Exception as e:
            print(f"Error al cargar clasificación: {e}")
    def _refresh_all(self):
        try:
            self._cargar_resultados()
            self._cargar_jugadores()
            self._cargar_clasificacion()
        except Exception as e:
            print(f"Error refrescando datos: {e}")
    def _on_header_clicked(self, index):
        try:
            table = getattr(self.ui, 'tableJugadores', None)
            if not table:
                return
            current_order = table.horizontalHeader().sortIndicatorOrder()
            from PySide6.QtCore import Qt as _Qt
            new_order = _Qt.DescendingOrder if current_order == _Qt.AscendingOrder else _Qt.AscendingOrder
            table.sortItems(index, new_order)
        except Exception as e:
            print(f"Error ordenando tabla: {e}")
    def editar_resultado(self):
        table = getattr(self.ui, 'treePartidos', None)
        if table is None:
            return
        items = table.selectedItems()
        if not items:
            QMessageBox.warning(self, "Validación", "Debe seleccionar un partido")
            return
        partido_id = items[0].data(0, Qt.UserRole)
        try:
            try:
                self.form_resultado_window.dialog.finished.disconnect()
            except Exception:
                pass
            self.form_resultado_window.dialog.finished.connect(self._refresh_all)
            self.form_resultado_window.cargar_partido(partido_id)
            self.form_resultado_window.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el formulario: {e}")
    def eliminar_resultado(self):
        tree = getattr(self.ui, 'treePartidos', None)
        if tree is None:
            return
        items = tree.selectedItems()
        if not items:
            QMessageBox.warning(self, "Validación", "Debe seleccionar un partido")
            return
        partido_id = items[0].data(0, Qt.UserRole)
        db = None
        try:
            from models.globals import get_db_connection
            db = get_db_connection()
            q = QSqlQuery(db)
            q.prepare("SELECT equipo1_id, equipo2_id, goles_equipo1, goles_equipo2, estado FROM partidos WHERE id = ?")
            q.addBindValue(partido_id)
            if q.exec() and q.next():
                eq1 = q.value(0)
                eq2 = q.value(1)
                g1 = q.value(2) or 0
                g2 = q.value(3) or 0
                estado = q.value(4)
                if estado == 'Finalizado':
                    from views.form_resultado import FormResultado as _FR
                    fr = _FR()
                    try:
                        fr._revert_clasificacion(db, eq1, eq2, g1, g2)
                    except Exception:
                        pass
            q2 = QSqlQuery(db)
            q2.prepare("DELETE FROM partidos WHERE id = ?")
            q2.addBindValue(partido_id)
            if q2.exec():
                QMessageBox.information(self, "Eliminado", "Partido eliminado correctamente")
                self._refresh_all()
            else:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar: {q2.lastError().text()}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al eliminar partido: {e}")
    def editar_jugador(self):
        table = getattr(self.ui, 'tableJugadores', None)
        if table is None:
            return
        selected = table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Validación", "Debe seleccionar un jugador")
            return
        row = selected[0].row()
        item_id = table.item(row, 0)
        if item_id is None:
            QMessageBox.warning(self, "Error", "No se pudo obtener el ID del jugador")
            return
        participante_id = item_id.data(Qt.UserRole) or int(item_id.text())
        form = FormParticipante()
        try:
            form.cargar_para_editar(participante_id)
            form.dialog.finished.connect(self._cargar_jugadores)
            form.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir formulario: {e}")
    def eliminar_jugador(self):
        table = getattr(self.ui, 'tableJugadores', None)
        if table is None:
            return
        selected = table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Validación", "Debe seleccionar un jugador")
            return
        row = selected[0].row()
        item_id = table.item(row, 0)
        participante_id = item_id.data(Qt.UserRole) or int(item_id.text())
        from models.globals import get_db_connection
        db = get_db_connection()
        q = QSqlQuery(db)
        q.prepare("DELETE FROM participantes WHERE id = ?")
        q.addBindValue(participante_id)
        if q.exec():
            QMessageBox.information(self, "Eliminado", "Participante eliminado")
            self._cargar_jugadores()
            self._refresh_all()
        else:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar: {q.lastError().text()}")
