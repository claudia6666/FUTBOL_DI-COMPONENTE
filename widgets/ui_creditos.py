

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_DialogCreditos(object):
    def setupUi(self, DialogCreditos):
        if not DialogCreditos.objectName():
            DialogCreditos.setObjectName(u"DialogCreditos")
        DialogCreditos.resize(991, 622)
        DialogCreditos.setStyleSheet(u"background-color: rgb(113,177,129);")
        self.vboxLayout = QVBoxLayout(DialogCreditos)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.buttonBox = QDialogButtonBox(DialogCreditos)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"\n"
"QPushButton {\n"
" background-color: rgb(1,107,97);\n"
" color: white;\n"
" border-radius: 8px;\n"
" padding: 8px 20px;\n"
" font-weight: bold;\n"
"}\n"
"      ")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)

        self.vboxLayout.addWidget(self.buttonBox)

        self.label = QLabel(DialogCreditos)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.label)

        self.frame = QFrame(DialogCreditos)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"background-color: rgb(1,107,97);\n"
"border-radius: 10px;\n"
"color: white;\n"
"      ")
        self.vboxLayout1 = QVBoxLayout(self.frame)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.label1 = QLabel(self.frame)
        self.label1.setObjectName(u"label1")
        font1 = QFont()
        font1.setPointSize(14)
        self.label1.setFont(font1)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout1.addWidget(self.label1)


        self.vboxLayout.addWidget(self.frame)


        self.retranslateUi(DialogCreditos)
        self.buttonBox.rejected.connect(DialogCreditos.reject)

        QMetaObject.connectSlotsByName(DialogCreditos)

    def retranslateUi(self, DialogCreditos):
        DialogCreditos.setWindowTitle(QCoreApplication.translate("DialogCreditos", u"Cr\u00e9ditos", None))
        self.label.setText(QCoreApplication.translate("DialogCreditos", u"CR\u00c9DITOS", None))
        self.label1.setText(QCoreApplication.translate("DialogCreditos", u"\n"
"Aplicaci\u00f3n de Gesti\u00f3n de Torneo de F\u00fatbol\n"
"\n"
"Autor: Claudia Orta Pereda \n"
"Versi\u00f3n: 1.0  \n"
"Fecha de actualizaci\u00f3n: Enero de 2026  \n"
"\n"
"Proyecto desarrollado con PySide6 y SQLite.\n"
"         ", None))

