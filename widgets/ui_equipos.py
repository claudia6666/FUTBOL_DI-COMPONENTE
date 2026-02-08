

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_DialogEquipos(object):
    def setupUi(self, DialogEquipos):
        if not DialogEquipos.objectName():
            DialogEquipos.setObjectName(u"DialogEquipos")
        DialogEquipos.resize(1000, 700)
        DialogEquipos.setMinimumSize(QSize(900, 600))
        DialogEquipos.setStyleSheet(u"background-color: rgb(113, 177, 129);")
        self.verticalLayout = QVBoxLayout(DialogEquipos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonBox = QDialogButtonBox(DialogEquipos)
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

        self.lblTitulo = QLabel(DialogEquipos)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font1 = QFont()
        font1.setPointSize(32)
        font1.setBold(True)
        self.lblTitulo.setFont(font1)
        self.lblTitulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.frameContenido = QFrame(DialogEquipos)
        self.frameContenido.setObjectName(u"frameContenido")
        self.frameContenido.setStyleSheet(u"background-color: rgb(113, 177, 129);")
        self.frameContenido.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout_main = QHBoxLayout(self.frameContenido)
        self.horizontalLayout_main.setObjectName(u"horizontalLayout_main")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.lblListaEquipos = QLabel(self.frameContenido)
        self.lblListaEquipos.setObjectName(u"lblListaEquipos")
        self.lblListaEquipos.setSizeIncrement(QSize(10, 0))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.lblListaEquipos.setFont(font2)
        self.lblListaEquipos.setStyleSheet(u" background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px 20px;\n"
"    font-weight: bold;\n"
"    min-width: 100px;")
        self.lblListaEquipos.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lblListaEquipos)

        self.tableEquipos = QTableWidget(self.frameContenido)
        if (self.tableEquipos.columnCount() < 5):
            self.tableEquipos.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableEquipos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableEquipos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableEquipos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableEquipos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableEquipos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableEquipos.setObjectName(u"tableEquipos")
        self.tableEquipos.setStyleSheet(u"QTableWidget {\n"
"    background-color: #93da97;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #93da97;\n"
"    color: rgb(1, 107, 97);\n"
"}\n"
"QHeaderView::section {\n"
"	\n"
"	background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"    padding: 8px;\n"
"    border: 2px solid #93da97 ;;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"")
        self.tableEquipos.setAlternatingRowColors(True)
        self.tableEquipos.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableEquipos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableEquipos.setSortingEnabled(True)
        self.tableEquipos.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableEquipos)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnNuevoEquipo = QPushButton(self.frameContenido)
        self.btnNuevoEquipo.setObjectName(u"btnNuevoEquipo")
        self.btnNuevoEquipo.setMinimumSize(QSize(0, 45))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.btnNuevoEquipo.setFont(font3)
        self.btnNuevoEquipo.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.btnNuevoEquipo)

        self.btnEditarEquipo = QPushButton(self.frameContenido)
        self.btnEditarEquipo.setObjectName(u"btnEditarEquipo")
        self.btnEditarEquipo.setMinimumSize(QSize(0, 45))
        self.btnEditarEquipo.setFont(font3)
        self.btnEditarEquipo.setStyleSheet(u"QPushButton {\n"
" \n"
"	background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"   \n"
"    padding: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #93da97;\n"
"    color: rgb(1, 107, 97);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1, 107, 97);\n"
"}")

        self.horizontalLayout.addWidget(self.btnEditarEquipo)

        self.btnEliminarEquipo = QPushButton(self.frameContenido)
        self.btnEliminarEquipo.setObjectName(u"btnEliminarEquipo")
        self.btnEliminarEquipo.setMinimumSize(QSize(0, 45))
        self.btnEliminarEquipo.setFont(font3)
        self.btnEliminarEquipo.setStyleSheet(u"QPushButton {\n"
" background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"      padding: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #93da97;\n"
"    color: rgb(1, 107, 97);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(1, 107, 97);\n"
"}")

        self.horizontalLayout.addWidget(self.btnEliminarEquipo)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_main.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.lblJugadoresEquipo = QLabel(self.frameContenido)
        self.lblJugadoresEquipo.setObjectName(u"lblJugadoresEquipo")
        self.lblJugadoresEquipo.setMaximumSize(QSize(16777215, 16777215))
        self.lblJugadoresEquipo.setFont(font2)
        self.lblJugadoresEquipo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
" background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px 20px;\n"
"    font-weight: bold;\n"
"    min-width: 100px;")
        self.lblJugadoresEquipo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblJugadoresEquipo)

        self.lblEquipoSeleccionado = QLabel(self.frameContenido)
        self.lblEquipoSeleccionado.setObjectName(u"lblEquipoSeleccionado")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(True)
        self.lblEquipoSeleccionado.setFont(font4)
        self.lblEquipoSeleccionado.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding: 4px;\n"
" background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px 20px;\n"
"    font-weight: bold;\n"
"    min-width: 100px;")
        self.lblEquipoSeleccionado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblEquipoSeleccionado.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lblEquipoSeleccionado)

        self.listJugadores = QListWidget(self.frameContenido)
        self.listJugadores.setObjectName(u"listJugadores")
        self.listJugadores.setStyleSheet(u"background-color: rgb(147, 218, 151);")
        self.listJugadores.setAlternatingRowColors(True)
        self.listJugadores.setSpacing(3)

        self.verticalLayout_3.addWidget(self.listJugadores)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAgregarJugador = QPushButton(self.frameContenido)
        self.btnAgregarJugador.setObjectName(u"btnAgregarJugador")
        self.btnAgregarJugador.setMinimumSize(QSize(0, 45))
        self.btnAgregarJugador.setFont(font3)
        self.btnAgregarJugador.setStyleSheet(u"background-color: rgb(1, 107, 97);")

        self.horizontalLayout_2.addWidget(self.btnAgregarJugador)

        self.btnQuitarJugador = QPushButton(self.frameContenido)
        self.btnQuitarJugador.setObjectName(u"btnQuitarJugador")
        self.btnQuitarJugador.setMinimumSize(QSize(0, 45))
        self.btnQuitarJugador.setFont(font3)
        self.btnQuitarJugador.setStyleSheet(u"background-color: rgb(1, 107, 97);")

        self.horizontalLayout_2.addWidget(self.btnQuitarJugador)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_main.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.frameContenido)


        self.retranslateUi(DialogEquipos)
        self.buttonBox.rejected.connect(DialogEquipos.reject)

        QMetaObject.connectSlotsByName(DialogEquipos)

    def retranslateUi(self, DialogEquipos):
        DialogEquipos.setWindowTitle(QCoreApplication.translate("DialogEquipos", u"Gesti\u00f3n de Equipos", None))
        self.lblTitulo.setText(QCoreApplication.translate("DialogEquipos", u"GESTI\u00d3N DE EQUIPOS", None))
        self.lblListaEquipos.setText(QCoreApplication.translate("DialogEquipos", u"Lista de Equipos", None))
        ___qtablewidgetitem = self.tableEquipos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogEquipos", u"ID", None));
        ___qtablewidgetitem1 = self.tableEquipos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogEquipos", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableEquipos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DialogEquipos", u"Curso", None));
        ___qtablewidgetitem3 = self.tableEquipos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DialogEquipos", u"Color", None));
        ___qtablewidgetitem4 = self.tableEquipos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DialogEquipos", u"Emblema", None));
        self.btnNuevoEquipo.setToolTip(QCoreApplication.translate("DialogEquipos", u"Crear un nuevo equipo", None))
        self.btnNuevoEquipo.setText(QCoreApplication.translate("DialogEquipos", u"Nuevo Equipo", None))
        self.btnEditarEquipo.setToolTip(QCoreApplication.translate("DialogEquipos", u"Editar equipo seleccionado", None))
        self.btnEditarEquipo.setText(QCoreApplication.translate("DialogEquipos", u"Editar", None))
        self.btnEliminarEquipo.setToolTip(QCoreApplication.translate("DialogEquipos", u"Eliminar equipo seleccionado", None))
        self.btnEliminarEquipo.setText(QCoreApplication.translate("DialogEquipos", u"Eliminar", None))
        self.lblJugadoresEquipo.setText(QCoreApplication.translate("DialogEquipos", u"Jugadores del Equipo", None))
        self.lblEquipoSeleccionado.setText(QCoreApplication.translate("DialogEquipos", u"Selecciona un equipo para ver sus jugadores", None))
        self.btnAgregarJugador.setToolTip(QCoreApplication.translate("DialogEquipos", u"Agregar jugador al equipo seleccionado", None))
        self.btnAgregarJugador.setText(QCoreApplication.translate("DialogEquipos", u"Agregar Jugador", None))
        self.btnQuitarJugador.setToolTip(QCoreApplication.translate("DialogEquipos", u"Quitar jugador del equipo", None))
        self.btnQuitarJugador.setText(QCoreApplication.translate("DialogEquipos", u"Quitar Jugador", None))

