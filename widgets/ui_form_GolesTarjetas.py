

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_DialogFormGolesTarjetas(object):
    def setupUi(self, DialogFormGolesTarjetas):
        if not DialogFormGolesTarjetas.objectName():
            DialogFormGolesTarjetas.setObjectName(u"DialogFormGolesTarjetas")
        DialogFormGolesTarjetas.resize(534, 397)
        DialogFormGolesTarjetas.setStyleSheet(u"\n"
"QDialog { background-color: rgb(113,177,129); }\n"
"\n"
"QLabel#lblTitulo {\n"
" font-size: 22pt;\n"
" font-weight: bold;\n"
" color: white;\n"
" background-color: rgb(1,107,97);\n"
" border-radius: 8px;\n"
" padding: 10px;\n"
"}\n"
"\n"
"QGroupBox {\n"
" color: white;\n"
" font-weight: bold;\n"
" border: 2px solid rgb(1,107,97);\n"
" border-radius: 8px;\n"
" margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
" subcontrol-origin: margin;\n"
" subcontrol-position: top center;\n"
" padding: 4px 10px;\n"
" background-color: rgb(1,107,97);\n"
" border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox, QComboBox {\n"
" background-color: white;\n"
" border: 2px solid rgb(1,107,97);\n"
" border-radius: 5px;\n"
" padding: 4px;\n"
"}\n"
"\n"
"QPushButton {\n"
" background-color: rgb(1,107,97);\n"
" color: white;\n"
" border-radius: 8px;\n"
" padding: 8px;\n"
" font-weight: bold;\n"
"}\n"
"   ")
        self.vboxLayout = QVBoxLayout(DialogFormGolesTarjetas)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.lblTitulo = QLabel(DialogFormGolesTarjetas)
        self.lblTitulo.setObjectName(u"lblTitulo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitulo.sizePolicy().hasHeightForWidth())
        self.lblTitulo.setSizePolicy(sizePolicy)
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.lblTitulo)

        self.groupBox = QGroupBox(DialogFormGolesTarjetas)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.cmbJugador = QComboBox(self.groupBox)
        self.cmbJugador.setObjectName(u"cmbJugador")
        self.cmbJugador.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbJugador)

        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")
        self.label1.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label1)

        self.spinGoles = QSpinBox(self.groupBox)
        self.spinGoles.setObjectName(u"spinGoles")
        self.spinGoles.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spinGoles)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")
        self.label2.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label2)

        self.spinAmarillas = QSpinBox(self.groupBox)
        self.spinAmarillas.setObjectName(u"spinAmarillas")
        self.spinAmarillas.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spinAmarillas)

        self.label3 = QLabel(self.groupBox)
        self.label3.setObjectName(u"label3")
        self.label3.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label3)

        self.spinRojas = QSpinBox(self.groupBox)
        self.spinRojas.setObjectName(u"spinRojas")
        self.spinRojas.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.spinRojas)

        self.horizontalSpacer = QSpacerItem(40, 8, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(0, QFormLayout.ItemRole.FieldRole, self.horizontalSpacer)


        self.vboxLayout.addWidget(self.groupBox)

        self.buttonBox = QDialogButtonBox(DialogFormGolesTarjetas)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.vboxLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogFormGolesTarjetas)
        self.buttonBox.accepted.connect(DialogFormGolesTarjetas.accept)
        self.buttonBox.rejected.connect(DialogFormGolesTarjetas.reject)

        QMetaObject.connectSlotsByName(DialogFormGolesTarjetas)

    def retranslateUi(self, DialogFormGolesTarjetas):
        DialogFormGolesTarjetas.setWindowTitle(QCoreApplication.translate("DialogFormGolesTarjetas", u"Goles y Tarjetas", None))
        self.lblTitulo.setText(QCoreApplication.translate("DialogFormGolesTarjetas", u"GOLES Y TARJETAS", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogFormGolesTarjetas", u"Datos del Jugador", None))
        self.label.setText(QCoreApplication.translate("DialogFormGolesTarjetas", u"Jugador:", None))
        self.label1.setText(QCoreApplication.translate("DialogFormGolesTarjetas", u"Goles:", None))
        self.label2.setText(QCoreApplication.translate("DialogFormGolesTarjetas", u"Tarjetas Amarillas:", None))
        self.label3.setText(QCoreApplication.translate("DialogFormGolesTarjetas", u"Tarjetas Rojas:", None))

