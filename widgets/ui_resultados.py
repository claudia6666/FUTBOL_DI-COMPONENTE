

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_DialogResultados(object):
    def setupUi(self, DialogResultados):
        if not DialogResultados.objectName():
            DialogResultados.setObjectName(u"DialogResultados")
        DialogResultados.resize(1000, 700)
        DialogResultados.setMinimumSize(QSize(900, 600))
        DialogResultados.setStyleSheet(u"background-color: rgb(113, 177, 129);")
        self.verticalLayout = QVBoxLayout(DialogResultados)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonBox = QDialogButtonBox(DialogResultados)
        self.buttonBox.setObjectName(u"buttonBox")
        font = QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(1, 107, 97);\n"
"color: white;\n"
"border-radius: 8px;\n"
"padding: 8px 20px;\n"
"font-weight: bold;\n"
"min-width: 100px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(113, 177, 129);\n"
"}")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)

        self.verticalLayout.addWidget(self.buttonBox)

        self.lblTitulo = QLabel(DialogResultados)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font1 = QFont()
        font1.setPointSize(28)
        font1.setBold(True)
        self.lblTitulo.setFont(font1)
        self.lblTitulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.tabWidgetResultados = QTabWidget(DialogResultados)
        self.tabWidgetResultados.setObjectName(u"tabWidgetResultados")
        self.tabWidgetResultados.setStyleSheet(u"QTabWidget::pane {\n"
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
        self.tabPartidos = QWidget()
        self.tabPartidos.setObjectName(u"tabPartidos")
        self.verticalLayoutPartidos = QVBoxLayout(self.tabPartidos)
        self.verticalLayoutPartidos.setObjectName(u"verticalLayoutPartidos")
        self.treePartidos = QTreeWidget(self.tabPartidos)
        fontPartidos = QFont()
        fontPartidos.setPointSize(8)
        fontPartidos.setBold(False)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem.setFont(4, fontPartidos);
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem.setFont(3, fontPartidos);
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setFont(2, fontPartidos);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setFont(1, fontPartidos);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem.setFont(0, fontPartidos);
        self.treePartidos.setHeaderItem(__qtreewidgetitem)
        self.treePartidos.setObjectName(u"treePartidos")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(False)
        self.treePartidos.setFont(font3)
        self.treePartidos.setStyleSheet(u"\n"
"QTreeWidget {background-color:#93da97; border-radius:5px; color:black;}\n"
"QTreeWidget::item {color:black;}\n"
"QTreeWidget::item:selected {background-color: rgb(1,107,97); color:white;}\n"
"QHeaderView::section {background-color: rgb(1,107,97); color:white; font-weight:bold; padding:5px;}\n"
"          ")
        self.treePartidos.setAllColumnsShowFocus(False)
        self.treePartidos.header().setCascadingSectionResizes(False)
        self.treePartidos.header().setDefaultSectionSize(182)

        self.verticalLayoutPartidos.addWidget(self.treePartidos)

        self.horizontalLayoutBotonesPartidos = QHBoxLayout()
        self.horizontalLayoutBotonesPartidos.setObjectName(u"horizontalLayoutBotonesPartidos")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)

        self.btnEditarPartido = QPushButton(self.tabPartidos)
        self.btnEditarPartido.setObjectName(u"btnEditarPartido")
        self.btnEditarPartido.setFont(font4)
        self.btnEditarPartido.setStyleSheet(u"background-color: rgb(1,107,97); color:white; border-radius:8px; padding:8px;")

        self.horizontalLayoutBotonesPartidos.addWidget(self.btnEditarPartido)

        self.btnEliminarPartido = QPushButton(self.tabPartidos)
        self.btnEliminarPartido.setObjectName(u"btnEliminarPartido")
        self.btnEliminarPartido.setFont(font4)
        self.btnEliminarPartido.setStyleSheet(u"background-color: rgb(1,107,97); color:white; border-radius:8px; padding:8px;")

        self.horizontalLayoutBotonesPartidos.addWidget(self.btnEliminarPartido)


        self.verticalLayoutPartidos.addLayout(self.horizontalLayoutBotonesPartidos)

        self.tabWidgetResultados.addTab(self.tabPartidos, "")
        self.tabJugadores = QWidget()
        self.tabJugadores.setObjectName(u"tabJugadores")
        self.verticalLayoutJugadores = QVBoxLayout(self.tabJugadores)
        self.verticalLayoutJugadores.setObjectName(u"verticalLayoutJugadores")
        self.tableJugadores = QTableWidget(self.tabJugadores)
        fontTableJugadores = QFont()
        fontTableJugadores.setPointSize(8)
        fontTableJugadores.setBold(False)
        if (self.tableJugadores.columnCount() < 6):
            self.tableJugadores.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(fontTableJugadores);
        self.tableJugadores.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(fontTableJugadores);
        self.tableJugadores.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(fontTableJugadores);
        self.tableJugadores.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(fontTableJugadores);
        self.tableJugadores.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(fontTableJugadores);
        self.tableJugadores.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(fontTableJugadores);
        self.tableJugadores.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableJugadores.setObjectName(u"tableJugadores")
        self.tableJugadores.setFont(fontTableJugadores)
        self.tableJugadores.setStyleSheet(u"\n"
"QTableWidget {background-color:#93da97; border-radius:5px; color:black;}\n"
"QTableWidget::item {color:black;}\n"
"QTableWidget::item:selected {background-color: rgb(1,107,97); color:white;}\n"
"QHeaderView::section {background-color: rgb(1,107,97); color:white; font-weight:bold; padding:5px;}\n"
"          ")
        self.tableJugadores.horizontalHeader().setDefaultSectionSize(150)
        self.tableJugadores.horizontalHeader().setStretchLastSection(True)

        self.verticalLayoutJugadores.addWidget(self.tableJugadores)

        self.horizontalLayoutBotonesJugadores = QHBoxLayout()
        self.horizontalLayoutBotonesJugadores.setObjectName(u"horizontalLayoutBotonesJugadores")
        self.btnRegistrarGolesTarjetas = QPushButton(self.tabJugadores)
        self.btnRegistrarGolesTarjetas.setObjectName(u"btnRegistrarGolesTarjetas")
        self.btnRegistrarGolesTarjetas.setFont(font4)
        self.btnRegistrarGolesTarjetas.setStyleSheet(u"background-color: rgb(1,107,97); color:white; border-radius:8px; padding:8px;")

        self.horizontalLayoutBotonesJugadores.addWidget(self.btnRegistrarGolesTarjetas)

        self.btnEditarJugador = QPushButton(self.tabJugadores)
        self.btnEditarJugador.setObjectName(u"btnEditarJugador")
        self.btnEditarJugador.setFont(font4)
        self.btnEditarJugador.setStyleSheet(u"background-color: rgb(1,107,97); color:white; border-radius:8px; padding:8px;")

        self.horizontalLayoutBotonesJugadores.addWidget(self.btnEditarJugador)

        self.btnEliminarJugador = QPushButton(self.tabJugadores)
        self.btnEliminarJugador.setObjectName(u"btnEliminarJugador")
        self.btnEliminarJugador.setFont(font4)
        self.btnEliminarJugador.setStyleSheet(u"background-color: rgb(1,107,97); color:white; border-radius:8px; padding:8px;")

        self.horizontalLayoutBotonesJugadores.addWidget(self.btnEliminarJugador)


        self.verticalLayoutJugadores.addLayout(self.horizontalLayoutBotonesJugadores)

        self.tabWidgetResultados.addTab(self.tabJugadores, "")
        self.tabClasificacion = QWidget()
        self.tabClasificacion.setObjectName(u"tabClasificacion")
        self.verticalLayoutClasificacion = QVBoxLayout(self.tabClasificacion)
        self.verticalLayoutClasificacion.setObjectName(u"verticalLayoutClasificacion")
        self.treeClasificacion = QTreeWidget(self.tabClasificacion)
        fontClasifResultados = QFont()
        fontClasifResultados.setPointSize(8)
        fontClasifResultados.setBold(False)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(3, fontClasifResultados);
        __qtreewidgetitem1.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(2, fontClasifResultados);
        __qtreewidgetitem1.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(1, fontClasifResultados);
        __qtreewidgetitem1.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem1.setFont(0, fontClasifResultados);
        self.treeClasificacion.setHeaderItem(__qtreewidgetitem1)
        self.treeClasificacion.setObjectName(u"treeClasificacion")
        self.treeClasificacion.setFont(fontClasifResultados)
        self.treeClasificacion.setStyleSheet(u"\n"
"QTreeWidget {background-color:#93da97; border-radius:5px; color:black;}\n"
"QTreeWidget::item {color:black;}\n"
"QTreeWidget::item:selected {background-color: rgb(1,107,97); color:white;}\n"
"QHeaderView::section {background-color: rgb(1,107,97); color:white; font-weight:bold; padding:5px;}\n"
"          ")
        self.treeClasificacion.header().setDefaultSectionSize(226)

        self.verticalLayoutClasificacion.addWidget(self.treeClasificacion)

        self.tabWidgetResultados.addTab(self.tabClasificacion, "")

        self.verticalLayout.addWidget(self.tabWidgetResultados)


        self.retranslateUi(DialogResultados)

        self.tabWidgetResultados.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(DialogResultados)

    def retranslateUi(self, DialogResultados):
        DialogResultados.setWindowTitle(QCoreApplication.translate("DialogResultados", u"Actualizaci\u00f3n de Resultados", None))
        self.lblTitulo.setText(QCoreApplication.translate("DialogResultados", u"ACTUALIZACI\u00d3N DE RESULTADOS", None))
        ___qtreewidgetitem = self.treePartidos.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("DialogResultados", u"Eliminatoria", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("DialogResultados", u"\u00c1rbitro", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("DialogResultados", u"Goles Equipo 2", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("DialogResultados", u"Goles Equipo 1", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DialogResultados", u"Partido", None));
        self.btnEditarPartido.setText(QCoreApplication.translate("DialogResultados", u"Editar Resultado", None))
        self.btnEliminarPartido.setText(QCoreApplication.translate("DialogResultados", u"Eliminar", None))
        self.tabWidgetResultados.setTabText(self.tabWidgetResultados.indexOf(self.tabPartidos), QCoreApplication.translate("DialogResultados", u"Partidos", None))
        ___qtablewidgetitem = self.tableJugadores.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DialogResultados", u"ID", None));
        ___qtablewidgetitem1 = self.tableJugadores.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DialogResultados", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableJugadores.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DialogResultados", u"Equipo", None));
        ___qtablewidgetitem3 = self.tableJugadores.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DialogResultados", u"Goles", None));
        ___qtablewidgetitem4 = self.tableJugadores.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DialogResultados", u"T. Amarillas", None));
        ___qtablewidgetitem5 = self.tableJugadores.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DialogResultados", u"T. Rojas", None));
        self.btnRegistrarGolesTarjetas.setText(QCoreApplication.translate("DialogResultados", u"Registrar Goles/Tarjetas", None))
        self.btnEditarJugador.setText(QCoreApplication.translate("DialogResultados", u"Editar", None))
        self.btnEliminarJugador.setText(QCoreApplication.translate("DialogResultados", u"Eliminar", None))
        self.tabWidgetResultados.setTabText(self.tabWidgetResultados.indexOf(self.tabJugadores), QCoreApplication.translate("DialogResultados", u"Jugadores", None))
        ___qtreewidgetitem1 = self.treeClasificacion.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("DialogResultados", u"T. Rojas", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("DialogResultados", u"T. Amarillas", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("DialogResultados", u"Goles", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("DialogResultados", u"Equipo/Jugador", None));
        self.tabWidgetResultados.setTabText(self.tabWidgetResultados.indexOf(self.tabClasificacion), QCoreApplication.translate("DialogResultados", u"Clasificaci\u00f3n", None))

