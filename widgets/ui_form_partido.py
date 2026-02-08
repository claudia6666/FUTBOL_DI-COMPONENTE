

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QTextEdit, QTimeEdit, QVBoxLayout, QWidget)

class Ui_DialogFormPartido(object):
    def setupUi(self, DialogFormPartido):
        if not DialogFormPartido.objectName():
            DialogFormPartido.setObjectName(u"DialogFormPartido")
        DialogFormPartido.resize(860, 549)
        DialogFormPartido.setStyleSheet(u"\n"
"QDialog {\n"
"    background-color: rgb(113, 177, 129);\n"
"}\n"
"\n"
"QLabel#lblTitulo {\n"
"    font-size: 22pt;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(1, 107, 97);\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #93da97;\n"
"    color: rgb(1, 107, 97);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1, 107, 97);\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QSpinBox, QDateEdit, QTimeEdit, QTextEdit {\n"
"    border: 2px solid rgb(1,107,97);\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"    background-color: white;\n"
"    color: black;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: 2px solid rgb(1,107,97);\n"
"    border-radius: 8px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroup"
                        "Box::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 4px 10px;\n"
"    background-color: rgb(1,107,97);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Labels dentro de los GroupBoxes */\n"
"QGroupBox QLabel {\n"
"    background-color: rgb(1,107,97);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    padding: 2px 4px;\n"
"    border-radius: 4px;\n"
"}\n"
"   ")
        self.verticalLayout = QVBoxLayout(DialogFormPartido)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitulo = QLabel(DialogFormPartido)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.groupEquipos = QGroupBox(DialogFormPartido)
        self.groupEquipos.setObjectName(u"groupEquipos")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupEquipos.sizePolicy().hasHeightForWidth())
        self.groupEquipos.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.groupEquipos.setFont(font)
        self.formLayout = QFormLayout(self.groupEquipos)
        self.formLayout.setObjectName(u"formLayout")
        self.lblEquipoLocal = QLabel(self.groupEquipos)
        self.lblEquipoLocal.setObjectName(u"lblEquipoLocal")
        self.lblEquipoLocal.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblEquipoLocal)

        self.cmbEquipoLocal = QComboBox(self.groupEquipos)
        self.cmbEquipoLocal.setObjectName(u"cmbEquipoLocal")
        font1 = QFont()
        font1.setPointSize(10)
        self.cmbEquipoLocal.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbEquipoLocal)

        self.lblEquipoVisitante = QLabel(self.groupEquipos)
        self.lblEquipoVisitante.setObjectName(u"lblEquipoVisitante")
        self.lblEquipoVisitante.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblEquipoVisitante)

        self.cmbEquipoVisitante = QComboBox(self.groupEquipos)
        self.cmbEquipoVisitante.setObjectName(u"cmbEquipoVisitante")
        self.cmbEquipoVisitante.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbEquipoVisitante)

        self.horizontalSpacer = QSpacerItem(40, 8, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(0, QFormLayout.ItemRole.FieldRole, self.horizontalSpacer)


        self.verticalLayout.addWidget(self.groupEquipos)

        self.groupDetalles = QGroupBox(DialogFormPartido)
        self.groupDetalles.setObjectName(u"groupDetalles")
        sizePolicy.setHeightForWidth(self.groupDetalles.sizePolicy().hasHeightForWidth())
        self.groupDetalles.setSizePolicy(sizePolicy)
        self.groupDetalles.setFont(font)
        self.formLayout_2 = QFormLayout(self.groupDetalles)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblFecha = QLabel(self.groupDetalles)
        self.lblFecha.setObjectName(u"lblFecha")
        self.lblFecha.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblFecha)

        self.dateFecha = QDateEdit(self.groupDetalles)
        self.dateFecha.setObjectName(u"dateFecha")
        self.dateFecha.setFont(font1)
        self.dateFecha.setCalendarPopup(True)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateFecha)

        self.lblHora = QLabel(self.groupDetalles)
        self.lblHora.setObjectName(u"lblHora")
        self.lblHora.setFont(font)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblHora)

        self.timeHora = QTimeEdit(self.groupDetalles)
        self.timeHora.setObjectName(u"timeHora")
        self.timeHora.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.timeHora)

        self.lblArbitro = QLabel(self.groupDetalles)
        self.lblArbitro.setObjectName(u"lblArbitro")
        self.lblArbitro.setFont(font)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblArbitro)

        self.cmbArbitro = QComboBox(self.groupDetalles)
        self.cmbArbitro.setObjectName(u"cmbArbitro")
        self.cmbArbitro.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbArbitro)

        self.lblLugar = QLabel(self.groupDetalles)
        self.lblLugar.setObjectName(u"lblLugar")
        self.lblLugar.setFont(font)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblLugar)

        self.txtLugar = QLineEdit(self.groupDetalles)
        self.txtLugar.setObjectName(u"txtLugar")
        self.txtLugar.setFont(font1)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtLugar)

        self.horizontalSpacer_2 = QSpacerItem(40, 8, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout_2.setItem(0, QFormLayout.ItemRole.FieldRole, self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.groupDetalles)

        self.groupObservaciones = QGroupBox(DialogFormPartido)
        self.groupObservaciones.setObjectName(u"groupObservaciones")
        self.groupObservaciones.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupObservaciones)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 8, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_3)

        self.txtObservaciones = QTextEdit(self.groupObservaciones)
        self.txtObservaciones.setObjectName(u"txtObservaciones")

        self.verticalLayout_2.addWidget(self.txtObservaciones)


        self.verticalLayout.addWidget(self.groupObservaciones)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(DialogFormPartido)
        self.buttonBox.setObjectName(u"buttonBox")
        font2 = QFont()
        font2.setPointSize(11)
        self.buttonBox.setFont(font2)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogFormPartido)
        self.buttonBox.accepted.connect(DialogFormPartido.accept)
        self.buttonBox.rejected.connect(DialogFormPartido.reject)

        QMetaObject.connectSlotsByName(DialogFormPartido)

    def retranslateUi(self, DialogFormPartido):
        DialogFormPartido.setWindowTitle(QCoreApplication.translate("DialogFormPartido", u"Programar Partido", None))
        self.lblTitulo.setText(QCoreApplication.translate("DialogFormPartido", u"PROGRAMAR PARTIDO", None))
        self.groupEquipos.setTitle(QCoreApplication.translate("DialogFormPartido", u"Equipos", None))
        self.lblEquipoLocal.setText(QCoreApplication.translate("DialogFormPartido", u"Equipo Local:", None))
        self.lblEquipoVisitante.setText(QCoreApplication.translate("DialogFormPartido", u"Equipo Visitante:", None))
        self.groupDetalles.setTitle(QCoreApplication.translate("DialogFormPartido", u"Detalles del Partido", None))
        self.lblFecha.setText(QCoreApplication.translate("DialogFormPartido", u"Fecha:", None))
        self.dateFecha.setDisplayFormat(QCoreApplication.translate("DialogFormPartido", u"dd/MM/yyyy", None))
        self.lblHora.setText(QCoreApplication.translate("DialogFormPartido", u"Hora:", None))
        self.lblArbitro.setText(QCoreApplication.translate("DialogFormPartido", u"\u00c1rbitro:", None))
        self.lblLugar.setText(QCoreApplication.translate("DialogFormPartido", u"Lugar:", None))
        self.groupObservaciones.setTitle(QCoreApplication.translate("DialogFormPartido", u"Observaciones", None))

