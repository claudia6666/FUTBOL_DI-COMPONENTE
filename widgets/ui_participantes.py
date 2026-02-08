

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDialog, QDialogButtonBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_DialogParticipantes(object):
    def setupUi(self, DialogParticipantes):
        if not DialogParticipantes.objectName():
            DialogParticipantes.setObjectName(u"DialogParticipantes")
        DialogParticipantes.resize(1000, 700)
        DialogParticipantes.setMinimumSize(QSize(900, 600))
        DialogParticipantes.setStyleSheet(u"background-color: rgb(113, 177, 129);")
        self.verticalLayout = QVBoxLayout(DialogParticipantes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonBox = QDialogButtonBox(DialogParticipantes)
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

        self.lblTitulo = QLabel(DialogParticipantes)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font1 = QFont()
        font1.setPointSize(31)
        font1.setBold(True)
        self.lblTitulo.setFont(font1)
        self.lblTitulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.frameContenido = QFrame(DialogParticipantes)
        self.frameContenido.setObjectName(u"frameContenido")
        self.frameContenido.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_contenido = QVBoxLayout(self.frameContenido)
        self.verticalLayout_contenido.setObjectName(u"verticalLayout_contenido")
        self.tabWidget = QTabWidget(self.frameContenido)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"	\n"
"background-color: rgb(1, 107, 97);\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"QTabBar::tab {\n"
"\n"
"background-color: rgb(147, 218, 151);\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    margin-right: 5px;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"}\n"
"QTabBar::tab:selected {\n"
"   	background-color: rgb(1, 107, 97);\n"
"}\n"
"QTabBar::tab:hover {\n"
"   	background-color: rgb(1, 107, 97);\n"
"}")
        self.tabJugadores = QWidget()
        self.tabJugadores.setObjectName(u"tabJugadores")
        self.verticalLayout_2 = QVBoxLayout(self.tabJugadores)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblBuscar = QLabel(self.tabJugadores)
        self.lblBuscar.setObjectName(u"lblBuscar")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.lblBuscar.setFont(font2)
        self.lblBuscar.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.lblBuscar)

        self.txtBuscarJugador = QLineEdit(self.tabJugadores)
        self.txtBuscarJugador.setObjectName(u"txtBuscarJugador")
        self.txtBuscarJugador.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 10pt;\n"
"}\n"
"QLineEdit:focus {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid #93da97;\n"
"}")

        self.horizontalLayout.addWidget(self.txtBuscarJugador)

        self.lblFiltroEquipo = QLabel(self.tabJugadores)
        self.lblFiltroEquipo.setObjectName(u"lblFiltroEquipo")
        self.lblFiltroEquipo.setFont(font2)
        self.lblFiltroEquipo.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.lblFiltroEquipo)

        self.cmbFiltroEquipo = QComboBox(self.tabJugadores)
        self.cmbFiltroEquipo.addItem("")
        self.cmbFiltroEquipo.setObjectName(u"cmbFiltroEquipo")
        self.cmbFiltroEquipo.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout.addWidget(self.cmbFiltroEquipo)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tableJugadores = QTableWidget(self.tabJugadores)
        if (self.tableJugadores.columnCount() < 9):
            self.tableJugadores.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableJugadores.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableJugadores.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableJugadores.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableJugadores.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableJugadores.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableJugadores.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableJugadores.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableJugadores.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableJugadores.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableJugadores.setObjectName(u"tableJugadores")
        self.tableJugadores.setStyleSheet(u"QTableWidget {\n"
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
        self.tableJugadores.setAlternatingRowColors(True)
        self.tableJugadores.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableJugadores.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableJugadores.setSortingEnabled(True)
        self.tableJugadores.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableJugadores)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnNuevoJugador = QPushButton(self.tabJugadores)
        self.btnNuevoJugador.setObjectName(u"btnNuevoJugador")
        self.btnNuevoJugador.setMinimumSize(QSize(0, 45))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.btnNuevoJugador.setFont(font3)
        self.btnNuevoJugador.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btnNuevoJugador)

        self.btnEditarJugador = QPushButton(self.tabJugadores)
        self.btnEditarJugador.setObjectName(u"btnEditarJugador")
        self.btnEditarJugador.setMinimumSize(QSize(0, 45))
        self.btnEditarJugador.setFont(font3)
        self.btnEditarJugador.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btnEditarJugador)

        self.btnEliminarJugador = QPushButton(self.tabJugadores)
        self.btnEliminarJugador.setObjectName(u"btnEliminarJugador")
        self.btnEliminarJugador.setMinimumSize(QSize(0, 45))
        self.btnEliminarJugador.setFont(font3)
        self.btnEliminarJugador.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btnEliminarJugador)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnExportarJugadores = QPushButton(self.tabJugadores)
        self.btnExportarJugadores.setObjectName(u"btnExportarJugadores")
        self.btnExportarJugadores.setMinimumSize(QSize(0, 45))
        self.btnExportarJugadores.setFont(font3)
        self.btnExportarJugadores.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(1, 107, 97);\n"
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

        self.horizontalLayout_2.addWidget(self.btnExportarJugadores)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tabJugadores, "")
        self.tabArbitros = QWidget()
        self.tabArbitros.setObjectName(u"tabArbitros")
        self.verticalLayout_3 = QVBoxLayout(self.tabArbitros)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_buscar = QHBoxLayout()
        self.horizontalLayout_buscar.setObjectName(u"horizontalLayout_buscar")
        self.lblBuscarArbitro = QLabel(self.tabArbitros)
        self.lblBuscarArbitro.setObjectName(u"lblBuscarArbitro")
        self.lblBuscarArbitro.setFont(font2)
        self.lblBuscarArbitro.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_buscar.addWidget(self.lblBuscarArbitro)

        self.txtBuscarArbitro = QLineEdit(self.tabArbitros)
        self.txtBuscarArbitro.setObjectName(u"txtBuscarArbitro")
        self.txtBuscarArbitro.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 10pt;\n"
"}\n"
"QLineEdit:focus {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid #93da97;\n"
"}")

        self.horizontalLayout_buscar.addWidget(self.txtBuscarArbitro)


        self.verticalLayout_3.addLayout(self.horizontalLayout_buscar)

        self.tableArbitros = QTableWidget(self.tabArbitros)
        if (self.tableArbitros.columnCount() < 5):
            self.tableArbitros.setColumnCount(5)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableArbitros.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableArbitros.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableArbitros.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableArbitros.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableArbitros.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        self.tableArbitros.setObjectName(u"tableArbitros")
        self.tableArbitros.setStyleSheet(u"QTableWidget {\n"
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
        self.tableArbitros.setAlternatingRowColors(True)
        self.tableArbitros.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableArbitros.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableArbitros.setSortingEnabled(True)
        self.tableArbitros.horizontalHeader().setDefaultSectionSize(158)
        self.tableArbitros.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.tableArbitros)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnNuevoArbitro = QPushButton(self.tabArbitros)
        self.btnNuevoArbitro.setObjectName(u"btnNuevoArbitro")
        self.btnNuevoArbitro.setMinimumSize(QSize(0, 45))
        self.btnNuevoArbitro.setFont(font3)
        self.btnNuevoArbitro.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.btnNuevoArbitro)

        self.btnEditarArbitro = QPushButton(self.tabArbitros)
        self.btnEditarArbitro.setObjectName(u"btnEditarArbitro")
        self.btnEditarArbitro.setMinimumSize(QSize(0, 45))
        self.btnEditarArbitro.setFont(font3)
        self.btnEditarArbitro.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.btnEditarArbitro)

        self.btnEliminarArbitro = QPushButton(self.tabArbitros)
        self.btnEliminarArbitro.setObjectName(u"btnEliminarArbitro")
        self.btnEliminarArbitro.setMinimumSize(QSize(0, 45))
        self.btnEliminarArbitro.setFont(font3)
        self.btnEliminarArbitro.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.btnEliminarArbitro)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btnAsignarPartido = QPushButton(self.tabArbitros)
        self.btnAsignarPartido.setObjectName(u"btnAsignarPartido")
        self.btnAsignarPartido.setMinimumSize(QSize(0, 45))
        self.btnAsignarPartido.setFont(font3)
        self.btnAsignarPartido.setStyleSheet(u"QPushButton {\n"
"  \n"
"	background-color: rgb(1, 107, 97);\n"
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

        self.horizontalLayout_3.addWidget(self.btnAsignarPartido)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tabArbitros, "")

        self.verticalLayout_contenido.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frameContenido)


        self.retranslateUi(DialogParticipantes)
        self.buttonBox.rejected.connect(DialogParticipantes.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DialogParticipantes)

    def retranslateUi(self, DialogParticipantes):
        DialogParticipantes.setWindowTitle(QCoreApplication.translate("DialogParticipantes", u"Gesti\u00f3n de Participantes", None))
        self.lblTitulo.setText(QCoreApplication.translate("DialogParticipantes", u"GESTI\u00d3N DE PARTICIPANTES", None))
        self.lblBuscar.setText(QCoreApplication.translate("DialogParticipantes", u"Buscar:", None))
        self.txtBuscarJugador.setPlaceholderText(QCoreApplication.translate("DialogParticipantes", u"Buscar por nombre...", None))
        self.lblFiltroEquipo.setText(QCoreApplication.translate("DialogParticipantes", u"Equipo:", None))
        self.cmbFiltroEquipo.setItemText(0, QCoreApplication.translate("DialogParticipantes", u"Todos los equipos", None))

        self.cmbFiltroEquipo.setToolTip(QCoreApplication.translate("DialogParticipantes", u"Filtrar por equipo", None))
        ___qtablewidgetitem = self.tableJugadores.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogParticipantes", u"ID", None));
        ___qtablewidgetitem1 = self.tableJugadores.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogParticipantes", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableJugadores.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DialogParticipantes", u"Fecha Nac.", None));
        ___qtablewidgetitem3 = self.tableJugadores.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DialogParticipantes", u"Curso", None));
        ___qtablewidgetitem4 = self.tableJugadores.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DialogParticipantes", u"Equipo", None));
        ___qtablewidgetitem5 = self.tableJugadores.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DialogParticipantes", u"Posici\u00f3n", None));
        ___qtablewidgetitem6 = self.tableJugadores.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DialogParticipantes", u"Goles", None));
        ___qtablewidgetitem7 = self.tableJugadores.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DialogParticipantes", u"T. Amarillas", None));
        ___qtablewidgetitem8 = self.tableJugadores.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DialogParticipantes", u"T. Rojas", None));
        self.btnNuevoJugador.setToolTip(QCoreApplication.translate("DialogParticipantes", u"Registrar nuevo jugador", None))
        self.btnNuevoJugador.setText(QCoreApplication.translate("DialogParticipantes", u"Nuevo Jugador", None))
        self.btnEditarJugador.setToolTip(QCoreApplication.translate("DialogParticipantes", u"Editar jugador seleccionado", None))
        self.btnEditarJugador.setText(QCoreApplication.translate("DialogParticipantes", u"Editar", None))
        self.btnEliminarJugador.setToolTip(QCoreApplication.translate("DialogParticipantes", u"Eliminar jugador seleccionado", None))
        self.btnEliminarJugador.setText(QCoreApplication.translate("DialogParticipantes", u"Eliminar", None))
        self.btnExportarJugadores.setToolTip(QCoreApplication.translate("DialogParticipantes", u"Exportar lista de jugadores a CSV", None))
        self.btnExportarJugadores.setText(QCoreApplication.translate("DialogParticipantes", u"Exportar CSV", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabJugadores), QCoreApplication.translate("DialogParticipantes", u"Jugadores", None))
        self.lblBuscarArbitro.setText(QCoreApplication.translate("DialogParticipantes", u"Buscar:", None))
        self.txtBuscarArbitro.setPlaceholderText(QCoreApplication.translate("DialogParticipantes", u"Buscar \u00e1rbitro por nombre...", None))
        ___qtablewidgetitem9 = self.tableArbitros.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DialogParticipantes", u"ID", None));
        ___qtablewidgetitem10 = self.tableArbitros.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DialogParticipantes", u"Nombre", None));
        ___qtablewidgetitem11 = self.tableArbitros.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DialogParticipantes", u"Fecha Nac.", None));
        ___qtablewidgetitem12 = self.tableArbitros.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DialogParticipantes", u"Curso", None));
        ___qtablewidgetitem13 = self.tableArbitros.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DialogParticipantes", u"Partidos Arbitrados", None));
        self.btnNuevoArbitro.setToolTip(QCoreApplication.translate("DialogParticipantes", u"Registrar nuevo \u00e1rbitro", None))
        self.btnNuevoArbitro.setText(QCoreApplication.translate("DialogParticipantes", u"Nuevo \u00c1rbitro", None))
        self.btnEditarArbitro.setToolTip(QCoreApplication.translate("DialogParticipantes", u"Editar \u00e1rbitro seleccionado", None))
        self.btnEditarArbitro.setText(QCoreApplication.translate("DialogParticipantes", u"Editar", None))
        self.btnEliminarArbitro.setToolTip(QCoreApplication.translate("DialogParticipantes", u"Eliminar \u00e1rbitro seleccionado", None))
        self.btnEliminarArbitro.setText(QCoreApplication.translate("DialogParticipantes", u"Eliminar", None))
        self.btnAsignarPartido.setToolTip(QCoreApplication.translate("DialogParticipantes", u"Asignar \u00e1rbitro a un partido", None))
        self.btnAsignarPartido.setText(QCoreApplication.translate("DialogParticipantes", u"Asignar a Partido", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabArbitros), QCoreApplication.translate("DialogParticipantes", u"\u00c1rbitros", None))

