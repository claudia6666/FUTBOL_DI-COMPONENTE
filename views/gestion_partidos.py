import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
from PySide6.QtWidgets import QWidget, QMessageBox, QTreeWidgetItem, QTableWidgetItem, QVBoxLayout
from PySide6.QtSql import QSqlQuery
from models.globals import get_db_connection
from modules.reloj_digital.views.RelojWidget import DigitalClockWidget

class GestionPartidos(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_ui = os.path.join(ruta_base, 'ui', 'gestion_partidos.ui')
        loader = QUiLoader()
        ui_file = QFile(ruta_ui)
        if ui_file.open(QIODevice.ReadOnly):
            self.ui = loader.load(ui_file, self)
            ui_file.close()
            if self.ui:
                self._apply_green_theme()
                self._setup_reloj()
                self._connect_signals()
                try:
                    self._cargar_partidos()
                except Exception as e:
                    print(f"Error cargando partidos: {e}")
                return
        self.ui = QWidget()
        QMessageBox.warning(self, 'Aviso', f'No se pudo cargar {ruta_ui}')

    def _apply_green_theme(self):
        try:
            green_stylesheet = """
            QWidget {
                background-color: #016b61;
            }
            QGroupBox {
                color: white;
                border: 2px solid #93da97;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px 0 3px;
            }
            QLabel {
                color: white;
            }
            QCheckBox {
                color: white;
            }
            QRadioButton {
                color: white;
            }
            QPushButton {
                background-color: #93da97;
                color: #016b61;
                border: 2px solid #6fae7e;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #a8eaab;
            }
            QPushButton:pressed {
                background-color: #7ac981;
            }
            QComboBox {
                background-color: #0d5350;
                color: white;
                border: 2px solid #6fae7e;
                border-radius: 3px;
                padding: 4px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QSpinBox {
                background-color: #0d5350;
                color: white;
                border: 2px solid #6fae7e;
                border-radius: 3px;
                padding: 4px;
            }
            QLineEdit {
                background-color: #0d5350;
                color: white;
                border: 2px solid #6fae7e;
                border-radius: 3px;
                padding: 4px;
            }
            QTableWidget {
                background-color: #0d5350;
                color: white;
                gridline-color: #6fae7e;
            }
            QTableWidget::item {
                padding: 4px;
            }
            QTableWidget::item:selected {
                background-color: #6fae7e;
            }
            QHeaderView::section {
                background-color: #016b61;
                color: white;
                padding: 4px;
                border: 1px solid #6fae7e;
            }
            QTreeWidget {
                background-color: #0d5350;
                color: white;
            }
            """
            self.ui.setStyleSheet(green_stylesheet)
        except Exception as e:
            print(f"Error aplicando tema verde: {e}")
        except Exception as e:
            print(f"Error aplicando tema verde: {e}")

    def _setup_reloj(self):
        try:
            from PySide6.QtWidgets import QSpinBox, QLabel, QPushButton, QHBoxLayout, QComboBox, QMainWindow
            from modules.reloj_digital.widgets.ui_AppReloj import Ui_MainWindow as UiRelojMain

            self._reloj_ui_instance = None

            clock_container = self.ui.findChild(QWidget, "clockContainer")
            if not clock_container:
                return

            layout = QVBoxLayout(clock_container)
            layout.setContentsMargins(4, 4, 4, 4)

            mode_combo = QComboBox(clock_container)
            mode_combo.addItems(['Fútbol', 'Reloj'])
            layout.addWidget(mode_combo)

            self._inner_container = QWidget(clock_container)
            inner_layout = QVBoxLayout(self._inner_container)
            inner_layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(self._inner_container)

            def clear_inner():
                for i in reversed(range(self._inner_container.layout().count())):
                    w = self._inner_container.layout().itemAt(i).widget()
                    if w:
                        w.setParent(None)

            def build_futbol_view():
                clear_inner()
                try:
                    if hasattr(self.ui, 'groupGestion'):
                        self.ui.groupGestion.show()
                    if hasattr(self.ui, 'groupReloj'):
                        self.ui.groupReloj.setMaximumWidth(300)
                except Exception:
                    pass
                from PySide6.QtWidgets import QSizePolicy
                self.clock_widget = DigitalClockWidget()
                try:
                    if hasattr(self.clock_widget, 'lcd_display') and self.clock_widget.lcd_display:
                        self.clock_widget.lcd_display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                except Exception:
                    pass
                try:
                    self.clock_widget.set_mode('timer')
                    self.clock_widget.set_timer_duration(90)
                    self.clock_widget._count_up = False
                    self.clock_widget.reset_timer()
                except Exception:
                    pass
                self._inner_container.layout().addWidget(self.clock_widget)

                controls = QHBoxLayout()
                lbl = QLabel('Duración (min):', self._inner_container)
                spin = QSpinBox(self._inner_container)
                spin.setRange(1, 300)
                spin.setValue(90)
                btn_apply = QPushButton('Aplicar', self._inner_container)
                self._futbol_duration_controls = (lbl, spin, btn_apply)

                def aplicar_duracion():
                    minutos = int(spin.value())
                    try:
                        self.clock_widget.set_timer_duration(minutos)
                        self.clock_widget._count_up = False
                        self.clock_widget.reset_timer()
                        QMessageBox.information(self, 'Temporizador', f'Duración ajustada a {minutos} minutos')
                    except Exception as e:
                        QMessageBox.critical(self, 'Error', f'No se pudo ajustar la duración: {e}')

                btn_apply.clicked.connect(aplicar_duracion)
                controls.addWidget(lbl)
                controls.addWidget(spin)
                controls.addWidget(btn_apply)
                self._inner_container.layout().addItem(controls)
                if getattr(self, '_reloj_window', None):
                    try:
                        self._reloj_window.close()
                    except Exception:
                        pass
                if getattr(self, '_reloj_widget', None):
                    try:
                        self._reloj_widget.close()
                    except Exception:
                        pass
                try:
                    for w in getattr(self, '_futbol_duration_controls', ()): 
                        if w:
                            w.show()
                except Exception:
                    pass

            def build_reloj_view():
                clear_inner()
                try:
                    from PySide6.QtWidgets import QMainWindow
                    from modules.reloj_digital.widgets.ui_AppReloj import Ui_MainWindow as UiRelojMain

                    temp_main = QMainWindow()
                    ui_reloj = UiRelojMain()
                    ui_reloj.setupUi(temp_main)

                    central = getattr(ui_reloj, 'centralwidget', None)
                    if central is None:
                        from modules.reloj_digital.views.AppReloj import TestWindow
                        self._reloj_window = TestWindow()
                        if getattr(self._reloj_window, 'ui', None) and hasattr(self._reloj_window.ui, 'clockWidgetContainer'):
                            cont = self._reloj_window.ui.clockWidgetContainer
                            cont.setParent(self._inner_container)
                            self._inner_container.layout().addWidget(cont)
                        else:
                            self._reloj_window.showMaximized()
                        return

                    try:
                        if hasattr(self.ui, 'groupGestion'):
                            self.ui.groupGestion.hide()
                        if hasattr(self.ui, 'groupReloj'):
                            self.ui.groupReloj.setMaximumWidth(16777215)
                    except Exception:
                        pass

                    try:
                        for w in getattr(self, '_futbol_duration_controls', ()): 
                            if w:
                                w.hide()
                    except Exception:
                        pass

                    try:
                        if getattr(self, '_reloj_window', None):
                            try:
                                self._reloj_window.close()
                            except Exception:
                                pass

                        from modules.reloj_digital.views.AppReloj import TestWindow
                        self._reloj_window = TestWindow()
                        central = getattr(self._reloj_window.ui, 'centralwidget', None)
                        if central is None:
                            return

                        try:
                            self._reloj_window.hide()
                        except Exception:
                            pass

                        central.setParent(self._inner_container)
                        try:
                            from PySide6.QtWidgets import QSizePolicy
                            central.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                            self._inner_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                            if hasattr(self.ui, 'groupReloj'):
                                self.ui.groupReloj.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                        except Exception:
                            pass
                        self._inner_container.layout().addWidget(central)
                        self._reloj_widget = central

                        try:
                            reloj_container = central.findChild(QWidget, 'clockWidgetContainer')
                            if reloj_container:
                                try:
                                    from PySide6.QtWidgets import QSizePolicy, QSpacerItem
                                    reloj_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                                    reloj_container.setMinimumHeight(175)
                                    reloj_container.setMinimumWidth(200)
                                except Exception:
                                    pass
                                try:
                                    cw = getattr(self._reloj_window, 'clock_widget', None)
                                    if cw:
                                        try:
                                            if hasattr(cw, 'lcd_display') and cw.lcd_display:
                                                cw.lcd_display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                                                try:
                                                    cw.lcd_display.setMinimumHeight(70)
                                                    cw.lcd_display.setMinimumWidth(140)
                                                except Exception:
                                                    pass
                                                try:
                                                    cw.lcd_display.setStyleSheet('font-size:36px;')
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                        try:
                                            cw.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                                            try:
                                                cw.setMinimumHeight(175)
                                                cw.setMinimumWidth(200)
                                            except Exception:
                                                pass
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                                try:
                                    central.updateGeometry()
                                    self._inner_container.updateGeometry()
                                    if hasattr(self.ui, 'groupReloj'):
                                        self.ui.groupReloj.updateGeometry()
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    except Exception as e:
                        print(f"Error integrando TestWindow del módulo reloj: {e}")
                except Exception as e:
                    print(f"Error construyendo vista reloj: {e}")

            build_futbol_view()

            def on_mode_change(index):
                try:
                    if mode_combo.itemText(index) == 'Reloj':
                        build_reloj_view()
                    else:
                        build_futbol_view()
                except Exception as e:
                    print(f"Error cambiando modo: {e}")

            mode_combo.currentIndexChanged.connect(on_mode_change)
        except Exception as e:
            print(f"Error configurando reloj: {e}")

    def _connect_signals(self):
        try:
            self.ui.tableEventos.setColumnCount(4)
            self.ui.tableEventos.setHorizontalHeaderLabels(['Tipo', 'Equipo', 'Jugador', 'Minuto'])
            
            self.ui.btnRefrescar.clicked.connect(self._cargar_partidos)
            self.ui.btnAgregarGol.clicked.connect(self._agregar_gol)
            self.ui.btnAgregarTarjeta.clicked.connect(self._agregar_tarjeta)
            self.ui.btnFinalizarPartido.clicked.connect(self._finalizar_partido)
            self.ui.treePartidos.itemSelectionChanged.connect(self._on_partido_selected)
            self.ui.cmbEquipoGoals.currentIndexChanged.connect(self._cargar_jugadores_equipo)
        except Exception as e:
            print(f"Error conectando señales: {e}")

    def _cargar_partidos(self):
        db = get_db_connection()
        query = QSqlQuery(db)
        query.exec("SELECT p.id, COALESCE(e1.nombre,'Equipo 1'), COALESCE(e2.nombre,'Equipo 2'), p.fecha, p.hora, COALESCE(p.estado,'Programado'), COALESCE(p.goles_equipo1,0), COALESCE(p.goles_equipo2,0) FROM partidos p LEFT JOIN equipos e1 ON p.equipo1_id = e1.id LEFT JOIN equipos e2 ON p.equipo2_id = e2.id WHERE COALESCE(p.goles_equipo1,0) = 0 AND COALESCE(p.goles_equipo2,0) = 0 ORDER BY p.fecha DESC, p.hora DESC")
        tree = self.ui.treePartidos
        tree.clear()
        while query.next():
            pid = query.value(0)
            local = query.value(1)
            visita = query.value(2)
            fecha = query.value(3) or ''
            hora = query.value(4) or ''
            estado = query.value(5) or ''
            goles1 = query.value(6) or 0
            goles2 = query.value(7) or 0
            texto = f"{local} {goles1} - {goles2} {visita}"
            item = QTreeWidgetItem([texto, f"{fecha} {hora}", estado])
            item.setData(0, Qt.UserRole, pid)
            tree.addTopLevelItem(item)

    def _on_partido_selected(self):
        try:
            item = self.ui.treePartidos.currentItem()
            if not item:
                return
            partido_id = item.data(0, Qt.UserRole)
            self.current_partido_id = partido_id
            self._cargar_detalle(partido_id)
            self._cargar_equipos_para_partido(partido_id)
        except Exception as e:
            print(f"Error seleccionando partido: {e}")

    def _cargar_detalle(self, partido_id):
        db = get_db_connection()
        query = QSqlQuery(db)
        query.prepare("SELECT e1.nombre, e2.nombre, p.goles_equipo1, p.goles_equipo2, p.equipo1_id, p.equipo2_id FROM partidos p LEFT JOIN equipos e1 ON p.equipo1_id = e1.id LEFT JOIN equipos e2 ON p.equipo2_id = e2.id WHERE p.id = ?")
        query.addBindValue(partido_id)
        if query.exec() and query.next():
            local = query.value(0)
            visita = query.value(1)
            goles1 = query.value(2) or 0
            goles2 = query.value(3) or 0
            self.equipo1_id = query.value(4)
            self.equipo2_id = query.value(5)
            try:
                self.ui.lblPartido.setText(f"Partido: {local} vs {visita}")
                self.ui.lblMarcador.setText(f"{goles1} - {goles2}")
            except Exception:
                pass
        self.ui.tableEventos.setRowCount(0)
        q2 = QSqlQuery(db)
        q2.prepare("SELECT 'Gol' as tipo, e.nombre as equipo, pa.nombre as jugador, g.minuto FROM goles g JOIN participantes pa ON g.participante_id = pa.id JOIN equipos e ON pa.equipo_id = e.id WHERE g.partido_id = ? UNION ALL SELECT 'Tarjeta' as tipo, e.nombre, pa.nombre, t.minuto FROM tarjetas t JOIN participantes pa ON t.participante_id = pa.id JOIN equipos e ON pa.equipo_id = e.id WHERE t.partido_id = ? ORDER BY 4")
        q2.addBindValue(partido_id)
        q2.addBindValue(partido_id)
        if q2.exec():
            row = 0
            while q2.next():
                tipo = q2.value(0)
                equipo = q2.value(1)
                jugador = q2.value(2)
                minuto = q2.value(3)
                self.ui.tableEventos.insertRow(row)
                self.ui.tableEventos.setItem(row, 0, QTableWidgetItem(str(tipo)))
                self.ui.tableEventos.setItem(row, 1, QTableWidgetItem(str(equipo)))
                self.ui.tableEventos.setItem(row, 2, QTableWidgetItem(str(jugador)))
                self.ui.tableEventos.setItem(row, 3, QTableWidgetItem(str(minuto)))
                row += 1

    def _cargar_equipos_para_partido(self, partido_id):
        db = get_db_connection()
        query = QSqlQuery(db)
        query.prepare("SELECT equipo1_id, equipo2_id FROM partidos WHERE id = ?")
        query.addBindValue(partido_id)
        if query.exec() and query.next():
            eq1_id = query.value(0)
            eq2_id = query.value(1)
            q_eq = QSqlQuery(db)
            q_eq.prepare("SELECT nombre FROM equipos WHERE id = ?")
            equipos = []
            for eq_id in [eq1_id, eq2_id]:
                q_eq.addBindValue(eq_id)
                if q_eq.exec() and q_eq.next():
                    equipos.append((eq_id, q_eq.value(0)))
            self.ui.cmbEquipoGoals.blockSignals(True)
            self.ui.cmbEquipoGoals.clear()
            for eq_id, eq_name in equipos:
                self.ui.cmbEquipoGoals.addItem(eq_name, eq_id)
            self.ui.cmbEquipoGoals.blockSignals(False)
            self._cargar_jugadores_equipo()

    def _cargar_jugadores_equipo(self):
        eq_id = self.ui.cmbEquipoGoals.currentData()
        if not eq_id:
            return
        db = get_db_connection()
        query = QSqlQuery(db)
        query.prepare("SELECT id, nombre FROM participantes WHERE equipo_id = ? AND tipo_participante = 'Jugador' ORDER BY nombre")
        query.addBindValue(eq_id)
        self.ui.cmbJugador.blockSignals(True)
        self.ui.cmbJugador.clear()
        if query.exec():
            while query.next():
                self.ui.cmbJugador.addItem(query.value(1), query.value(0))

    def _agregar_gol(self):
        if not hasattr(self, 'current_partido_id'):
            QMessageBox.warning(self, 'Aviso', 'Por favor selecciona un partido')
            return
        jugador_id = self.ui.cmbJugador.currentData()
        minuto = self.ui.spinMinuto.value()
        if not jugador_id:
            QMessageBox.warning(self, 'Aviso', 'Por favor selecciona un jugador')
            return
        db = get_db_connection()
        query = QSqlQuery(db)
        query.prepare("INSERT INTO goles (participante_id, partido_id, minuto) VALUES (?, ?, ?)")
        query.addBindValue(jugador_id)
        query.addBindValue(self.current_partido_id)
        query.addBindValue(minuto)
        if query.exec():
            QMessageBox.information(self, 'Éxito', 'Gol registrado')
            self._cargar_detalle(self.current_partido_id)
        else:
            QMessageBox.critical(self, 'Error', f'Error: {query.lastError().text()}')

    def _agregar_tarjeta(self):
        if not hasattr(self, 'current_partido_id'):
            QMessageBox.warning(self, 'Aviso', 'Por favor selecciona un partido')
            return
        jugador_id = self.ui.cmbJugador.currentData()
        minuto = self.ui.spinMinuto.value()
        if not jugador_id:
            QMessageBox.warning(self, 'Aviso', 'Por favor selecciona un jugador')
            return
        db = get_db_connection()
        query = QSqlQuery(db)
        query.prepare("INSERT INTO tarjetas (participante_id, partido_id, minuto, tipo) VALUES (?, ?, ?, ?)")
        query.addBindValue(jugador_id)
        query.addBindValue(self.current_partido_id)
        query.addBindValue(minuto)
        query.addBindValue('Amarilla')
        if query.exec():
            QMessageBox.information(self, 'Éxito', 'Tarjeta registrada')
            self._cargar_detalle(self.current_partido_id)
        else:
            QMessageBox.critical(self, 'Error', f'Error: {query.lastError().text()}')

    def _finalizar_partido(self):
        if not hasattr(self, 'current_partido_id'):
            QMessageBox.warning(self, 'Aviso', 'Por favor selecciona un partido')
            return
        db = get_db_connection()
        query = QSqlQuery(db)
        q_goles = QSqlQuery(db)
        q_goles.prepare("SELECT COUNT(*) FROM goles g JOIN participantes p ON g.participante_id = p.id WHERE g.partido_id = ? AND p.equipo_id = ?")
        
        q_goles.addBindValue(self.current_partido_id)
        q_goles.addBindValue(self.equipo1_id)
        goles1 = 0
        if q_goles.exec() and q_goles.next():
            goles1 = q_goles.value(0)
        
        q_goles_2 = QSqlQuery(db)
        q_goles_2.prepare("SELECT COUNT(*) FROM goles g JOIN participantes p ON g.participante_id = p.id WHERE g.partido_id = ? AND p.equipo_id = ?")
        q_goles_2.addBindValue(self.current_partido_id)
        q_goles_2.addBindValue(self.equipo2_id)
        goles2 = 0
        if q_goles_2.exec() and q_goles_2.next():
            goles2 = q_goles_2.value(0)
        
        query.prepare("UPDATE partidos SET goles_equipo1 = ?, goles_equipo2 = ?, estado = 'Finalizado' WHERE id = ?")
        query.addBindValue(goles1)
        query.addBindValue(goles2)
        query.addBindValue(self.current_partido_id)
        if query.exec():
            QMessageBox.information(self, 'Éxito', f'Partido finalizado: {goles1} - {goles2}')
            self._cargar_partidos()
        else:
            QMessageBox.critical(self, 'Error', f'Error: {query.lastError().text()}')

