

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QSize(900, 700))
        MainWindow.setMaximumSize(QSize(2782, 2221))
        MainWindow.setStyleSheet(u"background-color: rgb(113, 177, 129);\n"
"")
        self.actionExportar = QAction(MainWindow)
        self.actionExportar.setObjectName(u"actionExportar")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionAyuda = QAction(MainWindow)
        self.actionAyuda.setObjectName(u"actionAyuda")
        font = QFont()
        font.setBold(True)
        self.actionAyuda.setFont(font)
        self.actionCreditos = QAction(MainWindow)
        self.actionCreditos.setObjectName(u"actionCreditos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitulo = QLabel(self.centralwidget)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font1 = QFont()
        font1.setPointSize(31)
        font1.setBold(True)
        self.lblTitulo.setFont(font1)
        self.lblTitulo.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.frameContenido = QFrame(self.centralwidget)
        self.frameContenido.setObjectName(u"frameContenido")
        self.frameContenido.setFrameShape(QFrame.Shape.StyledPanel)
        self.gridLayout = QGridLayout(self.frameContenido)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnEstadisticas = QPushButton(self.frameContenido)
        self.btnEstadisticas.setObjectName(u"btnEstadisticas")
        self.btnEstadisticas.setMinimumSize(QSize(200, 120))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.btnEstadisticas.setFont(font2)
        self.btnEstadisticas.setStyleSheet(u"background-color: rgb(1, 107, 97);\n"
"\n"
"border: 4px solid #93da97; \n"
"border-radius:10px; \n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"../resources/iconos/stats.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEstadisticas.setIcon(icon)
        self.btnEstadisticas.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btnEstadisticas, 1, 2, 1, 1)

        self.btnClasificacion = QPushButton(self.frameContenido)
        self.btnClasificacion.setObjectName(u"btnClasificacion")
        self.btnClasificacion.setMinimumSize(QSize(200, 120))
        self.btnClasificacion.setFont(font2)
        self.btnClasificacion.setStyleSheet(u"background-color: rgb(1, 107, 97);\n"
"\n"
"border: 4px solid #93da97; \n"
"border-radius:10px; \n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../resources/iconos/trophy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnClasificacion.setIcon(icon1)
        self.btnClasificacion.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btnClasificacion, 1, 1, 1, 1)

        self.btnCalendario = QPushButton(self.frameContenido)
        self.btnCalendario.setObjectName(u"btnCalendario")
        self.btnCalendario.setMinimumSize(QSize(200, 120))
        self.btnCalendario.setFont(font2)
        self.btnCalendario.setStyleSheet(u"background-color: rgb(1, 107, 97);\n"
"\n"
"border: 4px solid #93da97; \n"
"border-radius:10px; \n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../resources/iconos/calendar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCalendario.setIcon(icon2)
        self.btnCalendario.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btnCalendario, 0, 2, 1, 1)

        self.btnParticipantes = QPushButton(self.frameContenido)
        self.btnParticipantes.setObjectName(u"btnParticipantes")
        self.btnParticipantes.setMinimumSize(QSize(200, 120))
        self.btnParticipantes.setFont(font2)
        self.btnParticipantes.setStyleSheet(u"background-color: rgb(1, 107, 97);\n"
"\n"
"border: 4px solid #93da97; \n"
"border-radius:10px; \n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../resources/iconos/players.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnParticipantes.setIcon(icon3)
        self.btnParticipantes.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btnParticipantes, 0, 1, 1, 1)

        self.btnResultados = QPushButton(self.frameContenido)
        self.btnResultados.setObjectName(u"btnResultados")
        self.btnResultados.setMinimumSize(QSize(200, 120))
        self.btnResultados.setFont(font2)
        self.btnResultados.setStyleSheet(u"background-color: rgb(1, 107, 97);\n"
"\n"
"border: 4px solid #93da97; \n"
"border-radius:10px; \n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../resources/iconos/results.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnResultados.setIcon(icon4)
        self.btnResultados.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btnResultados, 1, 0, 1, 1)

        self.btnEquipos = QPushButton(self.frameContenido)
        self.btnEquipos.setObjectName(u"btnEquipos")
        self.btnEquipos.setMinimumSize(QSize(200, 120))
        self.btnEquipos.setFont(font2)
        self.btnEquipos.setStyleSheet(u"background-color: rgb(1, 107, 97);\n"
"\n"
"border: 4px solid #93da97; \n"
"border-radius:10px; \n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"../resources/iconos/team.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnEquipos.setIcon(icon5)
        self.btnEquipos.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.btnEquipos, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frameContenido)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../resources/img/equipo.jpg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"../resources/img/Champ.jpg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"../resources/img/entreno.jpg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        self.menuCreditos = QMenu(self.menubar)
        self.menuCreditos.setObjectName(u"menuCreditos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menubar.addAction(self.menuCreditos.menuAction())
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuCreditos.addAction(self.actionCreditos)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Torneo de F\u00fatbol - Instituto", None))
        self.actionExportar.setText(QCoreApplication.translate("MainWindow", u"Exportar a CSV", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionAyuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.actionCreditos.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9ditos", None))
        self.lblTitulo.setText(QCoreApplication.translate("MainWindow", u"TORNEO DE F\u00daTBOL ", None))
        self.btnEstadisticas.setToolTip(QCoreApplication.translate("MainWindow", u"Ver estad\u00edsticas de goles y tarjetas", None))
        self.btnEstadisticas.setText(QCoreApplication.translate("MainWindow", u"Gestión de Partidos", None))
        self.btnClasificacion.setToolTip(QCoreApplication.translate("MainWindow", u"Ver cuadro de eliminatorias y clasificaci\u00f3n", None))
        self.btnClasificacion.setText(QCoreApplication.translate("MainWindow", u"Clasificaci\u00f3n", None))
        self.btnCalendario.setToolTip(QCoreApplication.translate("MainWindow", u"Programar y gestionar partidos", None))
        self.btnCalendario.setText(QCoreApplication.translate("MainWindow", u"Calendario de Partidos", None))
        self.btnParticipantes.setToolTip(QCoreApplication.translate("MainWindow", u"Gestionar jugadores y \u00e1rbitros", None))
        self.btnParticipantes.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Participantes", None))
        self.btnResultados.setToolTip(QCoreApplication.translate("MainWindow", u"Registrar resultados, goles y tarjetas", None))
        self.btnResultados.setText(QCoreApplication.translate("MainWindow", u"Actualizar Resultados", None))
        self.btnEquipos.setToolTip(QCoreApplication.translate("MainWindow", u"Crear, editar y eliminar equipos del torneo", None))
        self.btnEquipos.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Equipos", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.menuCreditos.setTitle(QCoreApplication.translate("MainWindow", u"Cr\u00e9ditos", None))

