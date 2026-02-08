

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QLabel, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_DialogAyuda(object):
    def setupUi(self, DialogAyuda):
        if not DialogAyuda.objectName():
            DialogAyuda.setObjectName(u"DialogAyuda")
        DialogAyuda.resize(900, 650)
        DialogAyuda.setStyleSheet(u"background-color: rgb(113,177,129);")
        self.vboxLayout = QVBoxLayout(DialogAyuda)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.buttonBox = QDialogButtonBox(DialogAyuda)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"\n"
"QPushButton {\n"
" background-color: rgb(1,107,97);\n"
" color: white;\n"
" border-radius: 10px;\n"
" padding: 10px 26px;\n"
" font-weight: bold;\n"
" font-size: 12pt;\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(113,177,129);\n"
"}\n"
"      ")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)

        self.vboxLayout.addWidget(self.buttonBox)

        self.label = QLabel(DialogAyuda)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.label)

        self.label1 = QLabel(DialogAyuda)
        self.label1.setObjectName(u"label1")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setItalic(True)
        self.label1.setFont(font1)
        self.label1.setStyleSheet(u"color: white;")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.label1)

        self.frame = QFrame(DialogAyuda)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"background-color: rgb(1,107,97);\n"
"border-radius: 16px;\n"
"      ")
        self.vboxLayout1 = QVBoxLayout(self.frame)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color: rgb(1, 107, 97);\n"
"border-radius: 12px;\n"
"padding: 18px;\n"
"font-size: 13pt;\n"
"line-height: 1.4;\n"
"         ")
        self.textEdit.setReadOnly(True)

        self.vboxLayout1.addWidget(self.textEdit)


        self.vboxLayout.addWidget(self.frame)


        self.retranslateUi(DialogAyuda)
        self.buttonBox.rejected.connect(DialogAyuda.reject)

        QMetaObject.connectSlotsByName(DialogAyuda)

    def retranslateUi(self, DialogAyuda):
        DialogAyuda.setWindowTitle(QCoreApplication.translate("DialogAyuda", u"Ayuda", None))
        self.label.setText(QCoreApplication.translate("DialogAyuda", u"AYUDA ", None))
        self.label1.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("DialogAyuda", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">E</span><span style=\" font-size:12pt; font-weight:700;\">sta aplicaci\u00f3n permite gestionar un torneo deportivo completo de forma sencilla y ordenada, utilizando PySide6 y SQLite.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weigh"
                        "t:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">GESTI\u00d3N DE CALENDARIO</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Crear, editar y eliminar partidos</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Seleccionar equipos, \u00e1rbitro, fecha y ronda</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Visualizar todos los partidos programados</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:"
                        "0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">ACTUALIZACI\u00d3N DE RESULTADOS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Registrar goles de los partidos jugados</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Actualizar autom\u00e1ticamente la clasificaci\u00f3n</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Registrar tarjetas y goles de jugadore"
                        "s</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">JUGADORES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Listar todos los participantes del torneo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Editar o eliminar jugadores</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weigh"
                        "t:700;\">\u2022 Consultar estad\u00edsticas individuales</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">CLASIFICACI\u00d3N</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Mostrar la clasificaci\u00f3n general</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Ordenar por puntos, goles o tarjetas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Actualizaci\u00f3n autom\u00e1tica tras cada partido</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">ELIMINATORIAS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Generar cuartos, semifinales y final</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Visualizar el cuadro de emparejamientos</span></p>\n"
"<p style=\" mar"
                        "gin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Gesti\u00f3n autom\u00e1tica seg\u00fan resultados</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">CONSEJOS DE USO</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Seleccione siempre un elemento antes de editar o eliminar</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12p"
                        "t; font-weight:700;\">\u2022 Utilice los botones inferiores para realizar acciones</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u2022 Todos los datos se guardan autom\u00e1ticamente en SQLite</span></p></body></html>", None))
        self.textEdit.setProperty(u"text", QCoreApplication.translate("DialogAyuda", u"\n"
"\ud83d\udc4b BIENVENIDO\n"
"\n"
"Esta aplicaci\u00f3n permite gestionar un torneo deportivo completo\n"
"de forma sencilla y ordenada, utilizando PySide6 y SQLite.\n"
"\n"
"\n"
"\ud83d\udcc5 GESTI\u00d3N DE CALENDARIO\n"
"\u2022 Crear, editar y eliminar partidos\n"
"\u2022 Seleccionar equipos, \u00e1rbitro, fecha y ronda\n"
"\u2022 Visualizar todos los partidos programados\n"
"\n"
"\n"
"\u26bd ACTUALIZACI\u00d3N DE RESULTADOS\n"
"\u2022 Registrar goles de los partidos jugados\n"
"\u2022 Actualizar autom\u00e1ticamente la clasificaci\u00f3n\n"
"\u2022 Registrar tarjetas y goles de jugadores\n"
"\n"
"\n"
"\ud83d\udc65 JUGADORES\n"
"\u2022 Listar todos los participantes del torneo\n"
"\u2022 Editar o eliminar jugadores\n"
"\u2022 Consultar estad\u00edsticas individuales\n"
"\n"
"\n"
"\ud83c\udfc6 CLASIFICACI\u00d3N\n"
"\u2022 Mostrar la clasificaci\u00f3n general\n"
"\u2022 Ordenar por puntos, goles o tarjetas\n"
"\u2022 Actualizaci\u00f3n autom\u00e1tica tras cada partido\n"
"\n"
"\n"
"\ud83e\udd47 ELIMINAT"
                        "ORIAS\n"
"\u2022 Generar cuartos, semifinales y final\n"
"\u2022 Visualizar el cuadro de emparejamientos\n"
"\u2022 Gesti\u00f3n autom\u00e1tica seg\u00fan resultados\n"
"\n"
"\n"
"\u2139\ufe0f CONSEJOS DE USO\n"
"\u2022 Seleccione siempre un elemento antes de editar o eliminar\n"
"\u2022 Utilice los botones inferiores para realizar acciones\n"
"\u2022 Todos los datos se guardan autom\u00e1ticamente en SQLite\n"
"         ", None))

