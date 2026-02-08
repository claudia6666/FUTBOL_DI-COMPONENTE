

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDialog, QDialogButtonBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_DialogEliminatorias(object):
    def setupUi(self, DialogEliminatorias):
        if not DialogEliminatorias.objectName():
            DialogEliminatorias.setObjectName(u"DialogEliminatorias")
        DialogEliminatorias.resize(1200, 800)
        DialogEliminatorias.setMinimumSize(QSize(1100, 700))
        DialogEliminatorias.setStyleSheet(u"background-color: rgb(113, 177, 129);")
        self.verticalLayout = QVBoxLayout(DialogEliminatorias)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonBox = QDialogButtonBox(DialogEliminatorias)
        self.buttonBox.setObjectName(u"buttonBox")
        font = QFont()
        font.setPointSize(13)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px 20px;\n"
"    font-weight: bold;\n"
"    min-width: 100px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(113, 177, 129);\n"
"}")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)

        self.verticalLayout.addWidget(self.buttonBox)

        self.lblTitulo = QLabel(DialogEliminatorias)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font1 = QFont()
        font1.setPointSize(31)
        font1.setBold(True)
        self.lblTitulo.setFont(font1)
        self.lblTitulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.frameContenido = QFrame(DialogEliminatorias)
        self.frameContenido.setObjectName(u"frameContenido")
        self.frameContenido.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_contenido = QVBoxLayout(self.frameContenido)
        self.verticalLayout_contenido.setObjectName(u"verticalLayout_contenido")
        self.tabWidget = QTabWidget(self.frameContenido)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    background-color: rgb(1, 107, 97);\n"
"    border-radius: 10px;\n"
"}\n"
"QTabBar::tab {\n"
"    background-color: rgb(147, 218, 151);\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    margin-right: 5px;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background-color: rgb(1, 107, 97);\n"
"}\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(1, 107, 97);\n"
"}")
        self.tabClasificacion = QWidget()
        self.tabClasificacion.setObjectName(u"tabClasificacion")
        self.verticalLayout_2 = QVBoxLayout(self.tabClasificacion)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_filtros = QHBoxLayout()
        self.horizontalLayout_filtros.setObjectName(u"horizontalLayout_filtros")
        self.lblFiltroGrupo = QLabel(self.tabClasificacion)
        self.lblFiltroGrupo.setObjectName(u"lblFiltroGrupo")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.lblFiltroGrupo.setFont(font2)
        self.lblFiltroGrupo.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_filtros.addWidget(self.lblFiltroGrupo)

        self.cmbFiltroGrupo = QComboBox(self.tabClasificacion)
        self.cmbFiltroGrupo.addItem("")
        self.cmbFiltroGrupo.addItem("")
        self.cmbFiltroGrupo.addItem("")
        self.cmbFiltroGrupo.addItem("")
        self.cmbFiltroGrupo.addItem("")
        self.cmbFiltroGrupo.setObjectName(u"cmbFiltroGrupo")
        self.cmbFiltroGrupo.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 10pt;\n"
"    min-width: 150px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid #93da97;\n"
"}\n"
"QComboBox:focus {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid #93da97;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    color: black;\n"
"    selection-background-color: #93da97;\n"
"    selection-color: rgb(1, 107, 97);\n"
"}")

        self.horizontalLayout_filtros.addWidget(self.cmbFiltroGrupo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_filtros.addItem(self.horizontalSpacer)

        self.lblClasificados = QLabel(self.tabClasificacion)
        self.lblClasificados.setObjectName(u"lblClasificados")
        self.lblClasificados.setFont(font2)
        self.lblClasificados.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(1, 107, 97);\n"
"padding: 8px 15px;\n"
"border-radius: 5px;")

        self.horizontalLayout_filtros.addWidget(self.lblClasificados)


        self.verticalLayout_2.addLayout(self.horizontalLayout_filtros)

        self.tableClasificacion = QTableWidget(self.tabClasificacion)
        if (self.tableClasificacion.columnCount() < 12):
            self.tableClasificacion.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableClasificacion.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableClasificacion.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableClasificacion.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableClasificacion.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableClasificacion.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableClasificacion.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableClasificacion.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableClasificacion.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableClasificacion.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableClasificacion.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableClasificacion.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableClasificacion.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableClasificacion.setObjectName(u"tableClasificacion")
        self.tableClasificacion.setStyleSheet(u"QTableWidget {\n"
"    background-color: #93da97;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"QTableWidget::item {\n"
"    color: black;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(113, 177, 129);\n"
"    color: white;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"    padding: 8px;\n"
"    border: 2px solid #93da97;\n"
"    font-weight: bold;\n"
"}")
        self.tableClasificacion.setAlternatingRowColors(True)
        self.tableClasificacion.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableClasificacion.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableClasificacion.setSortingEnabled(True)
        self.tableClasificacion.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableClasificacion)

        self.horizontalLayout_botones_clasificacion = QHBoxLayout()
        self.horizontalLayout_botones_clasificacion.setObjectName(u"horizontalLayout_botones_clasificacion")
        self.btnActualizarClasificacion = QPushButton(self.tabClasificacion)
        self.btnActualizarClasificacion.setObjectName(u"btnActualizarClasificacion")
        self.btnActualizarClasificacion.setMinimumSize(QSize(0, 45))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.btnActualizarClasificacion.setFont(font3)
        self.btnActualizarClasificacion.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #93da97;\n"
"    color: rgb(1, 107, 97);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1, 107, 97);\n"
"}")

        self.horizontalLayout_botones_clasificacion.addWidget(self.btnActualizarClasificacion)

        self.btnGenerarEliminatorias = QPushButton(self.tabClasificacion)
        self.btnGenerarEliminatorias.setObjectName(u"btnGenerarEliminatorias")
        self.btnGenerarEliminatorias.setMinimumSize(QSize(0, 45))
        self.btnGenerarEliminatorias.setFont(font3)
        self.btnGenerarEliminatorias.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #93da97;\n"
"    color: rgb(1, 107, 97);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1, 107, 97);\n"
"}")

        self.horizontalLayout_botones_clasificacion.addWidget(self.btnGenerarEliminatorias)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_botones_clasificacion.addItem(self.horizontalSpacer_2)

        self.btnExportarClasificacion = QPushButton(self.tabClasificacion)
        self.btnExportarClasificacion.setObjectName(u"btnExportarClasificacion")
        self.btnExportarClasificacion.setMinimumSize(QSize(0, 45))
        self.btnExportarClasificacion.setFont(font3)
        self.btnExportarClasificacion.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #93da97;\n"
"    color: rgb(1, 107, 97);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1, 107, 97);\n"
"}")

        self.horizontalLayout_botones_clasificacion.addWidget(self.btnExportarClasificacion)


        self.verticalLayout_2.addLayout(self.horizontalLayout_botones_clasificacion)

        self.tabWidget.addTab(self.tabClasificacion, "")
        self.tabEliminatorias = QWidget()
        self.tabEliminatorias.setObjectName(u"tabEliminatorias")
        self.verticalLayout_3 = QVBoxLayout(self.tabEliminatorias)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_control = QHBoxLayout()
        self.horizontalLayout_control.setObjectName(u"horizontalLayout_control")
        self.lblFaseActual = QLabel(self.tabEliminatorias)
        self.lblFaseActual.setObjectName(u"lblFaseActual")
        self.lblFaseActual.setFont(font2)
        self.lblFaseActual.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_control.addWidget(self.lblFaseActual)

        self.cmbFaseActual = QComboBox(self.tabEliminatorias)
        self.cmbFaseActual.addItem("")
        self.cmbFaseActual.addItem("")
        self.cmbFaseActual.addItem("")
        self.cmbFaseActual.addItem("")
        self.cmbFaseActual.setObjectName(u"cmbFaseActual")
        self.cmbFaseActual.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 10pt;\n"
"    min-width: 180px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid #93da97;\n"
"}\n"
"QComboBox:focus {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid #93da97;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    color: black;\n"
"    selection-background-color: #93da97;\n"
"    selection-color: rgb(1, 107, 97);\n"
"}")

        self.horizontalLayout_control.addWidget(self.cmbFaseActual)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_control.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_control)

        self.scrollAreaCuadro = QScrollArea(self.tabEliminatorias)
        self.scrollAreaCuadro.setObjectName(u"scrollAreaCuadro")
        self.scrollAreaCuadro.setStyleSheet(u"QScrollArea {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background-color: rgb(147, 218, 151);\n"
"    width: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(1, 107, 97);\n"
"    border-radius: 6px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(113, 177, 129);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background-color: rgb(147, 218, 151);\n"
"    height: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(1, 107, 97);\n"
"    border-radius: 6px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: rgb(113, 177, 129);\n"
"}")
        self.scrollAreaCuadro.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1130, 540))
        self.verticalLayout_cuadro = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_cuadro.setObjectName(u"verticalLayout_cuadro")
        self.frameCuadro = QFrame(self.scrollAreaWidgetContents)
        self.frameCuadro.setObjectName(u"frameCuadro")
        self.frameCuadro.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"}")
        self.frameCuadro.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameCuadro.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_frame_cuadro = QVBoxLayout(self.frameCuadro)
        self.verticalLayout_frame_cuadro.setObjectName(u"verticalLayout_frame_cuadro")
        self.lblInfoCuadro = QLabel(self.frameCuadro)
        self.lblInfoCuadro.setObjectName(u"lblInfoCuadro")
        font4 = QFont()
        font4.setPointSize(12)
        self.lblInfoCuadro.setFont(font4)
        self.lblInfoCuadro.setStyleSheet(u"color: rgb(1, 107, 97);\n"
"padding: 20px;")
        self.lblInfoCuadro.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblInfoCuadro.setWordWrap(True)

        self.verticalLayout_frame_cuadro.addWidget(self.lblInfoCuadro)


        self.verticalLayout_cuadro.addWidget(self.frameCuadro)

        self.scrollAreaCuadro.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollAreaCuadro)

        self.tabWidget.addTab(self.tabEliminatorias, "")

        self.verticalLayout_contenido.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frameContenido)


        self.retranslateUi(DialogEliminatorias)
        self.buttonBox.rejected.connect(DialogEliminatorias.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DialogEliminatorias)

    def retranslateUi(self, DialogEliminatorias):
        DialogEliminatorias.setWindowTitle(QCoreApplication.translate("DialogEliminatorias", u"Gesti\u00f3n de Eliminatorias", None))
        self.lblTitulo.setText(QCoreApplication.translate("DialogEliminatorias", u"CLASIFICACI\u00d3N Y ELIMINATORIAS", None))
        self.lblFiltroGrupo.setText(QCoreApplication.translate("DialogEliminatorias", u"Grupo:", None))
        self.cmbFiltroGrupo.setItemText(0, QCoreApplication.translate("DialogEliminatorias", u"Todos los grupos", None))
        self.cmbFiltroGrupo.setItemText(1, QCoreApplication.translate("DialogEliminatorias", u"Grupo A", None))
        self.cmbFiltroGrupo.setItemText(2, QCoreApplication.translate("DialogEliminatorias", u"Grupo B", None))
        self.cmbFiltroGrupo.setItemText(3, QCoreApplication.translate("DialogEliminatorias", u"Grupo C", None))
        self.cmbFiltroGrupo.setItemText(4, QCoreApplication.translate("DialogEliminatorias", u"Grupo D", None))

        self.lblClasificados.setText(QCoreApplication.translate("DialogEliminatorias", u"Clasificados a Eliminatorias: 0", None))
        ___qtablewidgetitem = self.tableClasificacion.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogEliminatorias", u"Pos", None));
        ___qtablewidgetitem1 = self.tableClasificacion.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogEliminatorias", u"Equipo", None));
        ___qtablewidgetitem2 = self.tableClasificacion.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DialogEliminatorias", u"Grupo", None));
        ___qtablewidgetitem3 = self.tableClasificacion.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DialogEliminatorias", u"PJ", None));
        ___qtablewidgetitem4 = self.tableClasificacion.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DialogEliminatorias", u"PG", None));
        ___qtablewidgetitem5 = self.tableClasificacion.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DialogEliminatorias", u"PE", None));
        ___qtablewidgetitem6 = self.tableClasificacion.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DialogEliminatorias", u"PP", None));
        ___qtablewidgetitem7 = self.tableClasificacion.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DialogEliminatorias", u"GF", None));
        ___qtablewidgetitem8 = self.tableClasificacion.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DialogEliminatorias", u"GC", None));
        ___qtablewidgetitem9 = self.tableClasificacion.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DialogEliminatorias", u"DG", None));
        ___qtablewidgetitem10 = self.tableClasificacion.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DialogEliminatorias", u"Pts", None));
        ___qtablewidgetitem11 = self.tableClasificacion.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DialogEliminatorias", u"Estado", None));
        self.btnActualizarClasificacion.setToolTip(QCoreApplication.translate("DialogEliminatorias", u"Actualizar tabla de clasificaci\u00f3n con \u00faltimos resultados", None))
        self.btnActualizarClasificacion.setText(QCoreApplication.translate("DialogEliminatorias", u"Actualizar Clasificaci\u00f3n", None))
        self.btnGenerarEliminatorias.setToolTip(QCoreApplication.translate("DialogEliminatorias", u"Generar cuadro de eliminatorias con equipos clasificados", None))
        self.btnGenerarEliminatorias.setText(QCoreApplication.translate("DialogEliminatorias", u"Generar Eliminatorias", None))
        self.btnExportarClasificacion.setToolTip(QCoreApplication.translate("DialogEliminatorias", u"Exportar tabla de clasificaci\u00f3n a CSV", None))
        self.btnExportarClasificacion.setText(QCoreApplication.translate("DialogEliminatorias", u"Exportar CSV", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabClasificacion), QCoreApplication.translate("DialogEliminatorias", u"Tabla de Clasificaci\u00f3n", None))
        self.lblFaseActual.setText(QCoreApplication.translate("DialogEliminatorias", u"Fase Actual:", None))
        self.cmbFaseActual.setItemText(0, QCoreApplication.translate("DialogEliminatorias", u"Cuartos de Final", None))
        self.cmbFaseActual.setItemText(1, QCoreApplication.translate("DialogEliminatorias", u"Semifinales", None))
        self.cmbFaseActual.setItemText(2, QCoreApplication.translate("DialogEliminatorias", u"Final", None))
        self.cmbFaseActual.setItemText(3, QCoreApplication.translate("DialogEliminatorias", u"Tercer Lugar", None))

        self.lblInfoCuadro.setText(QCoreApplication.translate("DialogEliminatorias", u"Genera las eliminatorias desde la pesta\u00f1a de Clasificaci\u00f3n para visualizar el cuadro aqu\u00ed.\n"
"\n"
"Los equipos clasificados se emparejar\u00e1n autom\u00e1ticamente seg\u00fan su posici\u00f3n en la tabla.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEliminatorias), QCoreApplication.translate("DialogEliminatorias", u"Cuadro de Eliminatorias", None))

