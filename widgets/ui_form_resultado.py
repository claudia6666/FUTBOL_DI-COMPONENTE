# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_resultado.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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

class Ui_DialogFormResultado(object):
    def setupUi(self, DialogFormResultado):
        if not DialogFormResultado.objectName():
            DialogFormResultado.setObjectName(u"DialogFormResultado")
        DialogFormResultado.resize(691, 313)
        DialogFormResultado.setStyleSheet(u"\n"
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
        self.vboxLayout = QVBoxLayout(DialogFormResultado)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.lblTitulo = QLabel(DialogFormResultado)
        self.lblTitulo.setObjectName(u"lblTitulo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitulo.sizePolicy().hasHeightForWidth())
        self.lblTitulo.setSizePolicy(sizePolicy)
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vboxLayout.addWidget(self.lblTitulo)

        self.groupResultado = QGroupBox(DialogFormResultado)
        self.groupResultado.setObjectName(u"groupResultado")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupResultado.sizePolicy().hasHeightForWidth())
        self.groupResultado.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.groupResultado.setFont(font)
        self.formLayout = QFormLayout(self.groupResultado)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupResultado)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.cmbEquipoLocal = QComboBox(self.groupResultado)
        self.cmbEquipoLocal.setObjectName(u"cmbEquipoLocal")
        self.cmbEquipoLocal.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbEquipoLocal)

        self.label1 = QLabel(self.groupResultado)
        self.label1.setObjectName(u"label1")
        self.label1.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label1)

        self.spinGolesLocal = QSpinBox(self.groupResultado)
        self.spinGolesLocal.setObjectName(u"spinGolesLocal")
        self.spinGolesLocal.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spinGolesLocal)

        self.label2 = QLabel(self.groupResultado)
        self.label2.setObjectName(u"label2")
        self.label2.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label2)

        self.cmbEquipoVisitante = QComboBox(self.groupResultado)
        self.cmbEquipoVisitante.setObjectName(u"cmbEquipoVisitante")
        self.cmbEquipoVisitante.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbEquipoVisitante)

        self.label3 = QLabel(self.groupResultado)
        self.label3.setObjectName(u"label3")
        self.label3.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label3)

        self.spinGolesVisitante = QSpinBox(self.groupResultado)
        self.spinGolesVisitante.setObjectName(u"spinGolesVisitante")
        self.spinGolesVisitante.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.spinGolesVisitante)

        self.horizontalSpacer = QSpacerItem(40, 8, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(0, QFormLayout.ItemRole.FieldRole, self.horizontalSpacer)


        self.vboxLayout.addWidget(self.groupResultado)

        self.buttonBox = QDialogButtonBox(DialogFormResultado)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.vboxLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogFormResultado)
        self.buttonBox.accepted.connect(DialogFormResultado.accept)
        self.buttonBox.rejected.connect(DialogFormResultado.reject)

        QMetaObject.connectSlotsByName(DialogFormResultado)
    # setupUi

    def retranslateUi(self, DialogFormResultado):
        DialogFormResultado.setWindowTitle(QCoreApplication.translate("DialogFormResultado", u"Resultado del Partido", None))
        self.lblTitulo.setText(QCoreApplication.translate("DialogFormResultado", u"RESULTADO DEL PARTIDO", None))
        self.groupResultado.setTitle(QCoreApplication.translate("DialogFormResultado", u"Marcador", None))
        self.label.setText(QCoreApplication.translate("DialogFormResultado", u"Equipo Local:", None))
        self.label1.setText(QCoreApplication.translate("DialogFormResultado", u"Goles Local:", None))
        self.label2.setText(QCoreApplication.translate("DialogFormResultado", u"Equipo Visitante:", None))
        self.label3.setText(QCoreApplication.translate("DialogFormResultado", u"Goles Visitante:", None))
    # retranslateUi

