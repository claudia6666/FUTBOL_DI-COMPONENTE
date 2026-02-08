

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateTimeEdit,
    QDialog, QDialogButtonBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_DialogCalendario(object):
    def setupUi(self, DialogCalendario):
        if not DialogCalendario.objectName():
            DialogCalendario.setObjectName(u"DialogCalendario")
        DialogCalendario.resize(1000, 700)
        DialogCalendario.setMinimumSize(QSize(900, 600))
        DialogCalendario.setStyleSheet(u"background-color: rgb(113, 177, 129);")
        self.verticalLayout = QVBoxLayout(DialogCalendario)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonBox = QDialogButtonBox(DialogCalendario)
        self.buttonBox.setObjectName(u"buttonBox")
        font = QFont()
        font.setPointSize(15)
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

        self.lblTitulo = QLabel(DialogCalendario)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font1 = QFont()
        font1.setPointSize(28)
        font1.setBold(True)
        self.lblTitulo.setFont(font1)
        self.lblTitulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.frameContenido = QFrame(DialogCalendario)
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
"    background-color: rgb(113, 177, 129);\n"
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
"    background-color: #93da97;\n"
"    color: rgb(1, 107, 97);\n"
"}")
        self.tabPartidos = QWidget()
        self.tabPartidos.setObjectName(u"tabPartidos")
        self.verticalLayoutPartidos = QVBoxLayout(self.tabPartidos)
        self.verticalLayoutPartidos.setObjectName(u"verticalLayoutPartidos")
        self.horizontalLayoutFiltros = QHBoxLayout()
        self.horizontalLayoutFiltros.setObjectName(u"horizontalLayoutFiltros")
        self.lblEquipo1 = QLabel(self.tabPartidos)
        self.lblEquipo1.setObjectName(u"lblEquipo1")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.lblEquipo1.setFont(font2)
        self.lblEquipo1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblEquipo1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayoutFiltros.addWidget(self.lblEquipo1)

        self.cmbEquipo1 = QComboBox(self.tabPartidos)
        self.cmbEquipo1.setObjectName(u"cmbEquipo1")
        self.cmbEquipo1.setStyleSheet(u"QComboBox {background-color:white; border-radius:5px; padding:5px; color:black;}")

        self.horizontalLayoutFiltros.addWidget(self.cmbEquipo1)

        self.lblEquipo2 = QLabel(self.tabPartidos)
        self.lblEquipo2.setObjectName(u"lblEquipo2")
        self.lblEquipo2.setFont(font2)
        self.lblEquipo2.setStyleSheet(u"color: white;")
        self.lblEquipo2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayoutFiltros.addWidget(self.lblEquipo2)

        self.cmbEquipo2 = QComboBox(self.tabPartidos)
        self.cmbEquipo2.setObjectName(u"cmbEquipo2")
        self.cmbEquipo2.setStyleSheet(u"QComboBox {background-color:white; border-radius:5px; padding:5px; color:black;}")

        self.horizontalLayoutFiltros.addWidget(self.cmbEquipo2)

        self.lblArbitro = QLabel(self.tabPartidos)
        self.lblArbitro.setObjectName(u"lblArbitro")
        self.lblArbitro.setFont(font2)
        self.lblArbitro.setStyleSheet(u"color:white\n"
";")
        self.lblArbitro.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayoutFiltros.addWidget(self.lblArbitro)

        self.cmbArbitro = QComboBox(self.tabPartidos)
        self.cmbArbitro.setObjectName(u"cmbArbitro")
        self.cmbArbitro.setStyleSheet(u"QComboBox {background-color:white; border-radius:5px; padding:5px; color:black;}\n"
"")

        self.horizontalLayoutFiltros.addWidget(self.cmbArbitro)

        self.lblFecha = QLabel(self.tabPartidos)
        self.lblFecha.setObjectName(u"lblFecha")
        self.lblFecha.setFont(font2)
        self.lblFecha.setStyleSheet(u"color:white\n"
";")

        self.horizontalLayoutFiltros.addWidget(self.lblFecha)

        self.dtFechaHora = QDateTimeEdit(self.tabPartidos)
        self.dtFechaHora.setObjectName(u"dtFechaHora")
        self.dtFechaHora.setStyleSheet(u"QDateTimeEdit {background-color:white; border-radius:5px; padding:5px; color:black;}")

        self.horizontalLayoutFiltros.addWidget(self.dtFechaHora)

        self.lblEliminatoria = QLabel(self.tabPartidos)
        self.lblEliminatoria.setObjectName(u"lblEliminatoria")
        self.lblEliminatoria.setFont(font2)
        self.lblEliminatoria.setStyleSheet(u"color:white\n"
";")

        self.horizontalLayoutFiltros.addWidget(self.lblEliminatoria)

        self.cmbEliminatoria = QComboBox(self.tabPartidos)
        self.cmbEliminatoria.addItem("")
        self.cmbEliminatoria.addItem("")
        self.cmbEliminatoria.addItem("")
        self.cmbEliminatoria.addItem("")
        self.cmbEliminatoria.addItem("")
        self.cmbEliminatoria.setObjectName(u"cmbEliminatoria")
        self.cmbEliminatoria.setFont(font2)
        self.cmbEliminatoria.setStyleSheet(u"QComboBox {background-color:white; border-radius:5px; padding:5px; color:black;}\n"
"")

        self.horizontalLayoutFiltros.addWidget(self.cmbEliminatoria)


        self.verticalLayoutPartidos.addLayout(self.horizontalLayoutFiltros)

        self.treePartidos = QTreeWidget(self.tabPartidos)
        font3 = QFont()
        font3.setPointSize(11)
        font3.setStyleStrategy(QFont.PreferAntialias)
        font4 = QFont()
        font4.setPointSize(11)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setFont(2, font4);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setFont(1, font4);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem.setFont(0, font3);
        self.treePartidos.setHeaderItem(__qtreewidgetitem)
        self.treePartidos.setObjectName(u"treePartidos")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.treePartidos.setFont(font5)
        self.treePartidos.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.treePartidos.setStyleSheet(u"QTreeWidget {background-color:#93da97; border-radius:5px;} QTreeWidget::item:selected {background-color: rgb(1,107,97); color:white;} QHeaderView::section {background-color: rgb(1,107,97); color:white; font-weight:bold; padding:5px;}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(1, 107, 97);\n"
"    color: black;\n"
"    padding: 8px;\n"
"    border: 2px solid #93da97;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter; /* CENTRA el texto */\n"
"}\n"
"\n"
" qproperty-alignment: AlignCenter; /* CENTRA el texto */")
        self.treePartidos.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.treePartidos.setAlternatingRowColors(True)
        self.treePartidos.header().setDefaultSectionSize(315)

        self.verticalLayoutPartidos.addWidget(self.treePartidos)

        self.horizontalLayoutBotones = QHBoxLayout()
        self.horizontalLayoutBotones.setObjectName(u"horizontalLayoutBotones")
        self.btnNuevoPartido = QPushButton(self.tabPartidos)
        self.btnNuevoPartido.setObjectName(u"btnNuevoPartido")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.btnNuevoPartido.setFont(font6)
        self.btnNuevoPartido.setStyleSheet(u"background-color: rgb(1, 107, 97);")

        self.horizontalLayoutBotones.addWidget(self.btnNuevoPartido)

        self.btnEditarPartido = QPushButton(self.tabPartidos)
        self.btnEditarPartido.setObjectName(u"btnEditarPartido")
        self.btnEditarPartido.setFont(font6)
        self.btnEditarPartido.setStyleSheet(u"background-color: rgb(1, 107, 97);")

        self.horizontalLayoutBotones.addWidget(self.btnEditarPartido)

        self.btnEliminarPartido = QPushButton(self.tabPartidos)
        self.btnEliminarPartido.setObjectName(u"btnEliminarPartido")
        self.btnEliminarPartido.setFont(font6)
        self.btnEliminarPartido.setStyleSheet(u"background-color: rgb(1, 107, 97);")

        self.horizontalLayoutBotones.addWidget(self.btnEliminarPartido)


        self.verticalLayoutPartidos.addLayout(self.horizontalLayoutBotones)

        self.tabWidget.addTab(self.tabPartidos, "")

        self.verticalLayout_contenido.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frameContenido)


        self.retranslateUi(DialogCalendario)
        self.buttonBox.rejected.connect(DialogCalendario.reject)

        QMetaObject.connectSlotsByName(DialogCalendario)

    def retranslateUi(self, DialogCalendario):
        DialogCalendario.setWindowTitle(QCoreApplication.translate("DialogCalendario", u"Gesti\u00f3n del Calendario", None))
        self.lblTitulo.setText(QCoreApplication.translate("DialogCalendario", u"GESTI\u00d3N DEL CALENDARIO", None))
        self.lblEquipo1.setText(QCoreApplication.translate("DialogCalendario", u"Equipo 1:", None))
        self.lblEquipo2.setText(QCoreApplication.translate("DialogCalendario", u"Equipo 2:", None))
        self.lblArbitro.setText(QCoreApplication.translate("DialogCalendario", u"\u00c1rbitro:", None))
        self.lblFecha.setText(QCoreApplication.translate("DialogCalendario", u"Fecha y Hora:", None))
        self.lblEliminatoria.setText(QCoreApplication.translate("DialogCalendario", u"Eliminatoria:", None))
        self.cmbEliminatoria.setItemText(0, QCoreApplication.translate("DialogCalendario", u"Todos", None))
        self.cmbEliminatoria.setItemText(1, QCoreApplication.translate("DialogCalendario", u"Octavos", None))
        self.cmbEliminatoria.setItemText(2, QCoreApplication.translate("DialogCalendario", u"Cuartos", None))
        self.cmbEliminatoria.setItemText(3, QCoreApplication.translate("DialogCalendario", u"Semifinal", None))
        self.cmbEliminatoria.setItemText(4, QCoreApplication.translate("DialogCalendario", u"Final", None))

        ___qtreewidgetitem = self.treePartidos.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("DialogCalendario", u"\u00c1rbitro", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("DialogCalendario", u"Fecha y Hora", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DialogCalendario", u"Partido", None));
        self.btnNuevoPartido.setText(QCoreApplication.translate("DialogCalendario", u"Nuevo Partido", None))
        self.btnEditarPartido.setText(QCoreApplication.translate("DialogCalendario", u"Editar", None))
        self.btnEliminarPartido.setText(QCoreApplication.translate("DialogCalendario", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPartidos), QCoreApplication.translate("DialogCalendario", u"Partidos", None))

