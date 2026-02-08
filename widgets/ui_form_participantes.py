

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)
class Ui_DialogFormParticipante(object):
    def setupUi(self, DialogFormParticipante):
        if not DialogFormParticipante.objectName():
            DialogFormParticipante.setObjectName(u"DialogFormParticipante")
        DialogFormParticipante.resize(560, 650)
        DialogFormParticipante.setMinimumSize(QSize(480, 560))
        DialogFormParticipante.setStyleSheet(u"\n"
"QDialog {\n"
"    background-color: rgb(113, 177, 129);\n"
"}\n"
"\n"
"QLabel#lblTitulo {\n"
"    font-size: 20pt;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(1, 107, 97);\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #93da97;\n"
"    color: rgb(1, 107, 97);\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QSpinBox, QDateEdit {\n"
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
"    margin-top: 18px;\n"
"    padding-top: 18px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-posi"
                        "tion: top center;\n"
"    padding: 5px 12px;\n"
"    background-color: rgb(1,107,97);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QLabel, QRadioButton {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"   ")
        self.verticalLayout = QVBoxLayout(DialogFormParticipante)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.lblTitulo = QLabel(DialogFormParticipante)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setAlignment(Qt.AlignCenter)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitulo.sizePolicy().hasHeightForWidth())
        self.lblTitulo.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.groupDatosPersonales = QGroupBox(DialogFormParticipante)
        self.groupDatosPersonales.setObjectName(u"groupDatosPersonales")
        self.formLayout = QFormLayout(self.groupDatosPersonales)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.label = QLabel(self.groupDatosPersonales)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.txtNombre = QLineEdit(self.groupDatosPersonales)
        self.txtNombre.setObjectName(u"txtNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.label1 = QLabel(self.groupDatosPersonales)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label1)

        self.dateFechaNac = QDateEdit(self.groupDatosPersonales)
        self.dateFechaNac.setObjectName(u"dateFechaNac")
        self.dateFechaNac.setCalendarPopup(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateFechaNac)

        self.label2 = QLabel(self.groupDatosPersonales)
        self.label2.setObjectName(u"label2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label2)

        self.cmbCurso = QComboBox(self.groupDatosPersonales)
        self.cmbCurso.setObjectName(u"cmbCurso")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbCurso)


        self.verticalLayout.addWidget(self.groupDatosPersonales)

        self.groupRol = QGroupBox(DialogFormParticipante)
        self.groupRol.setObjectName(u"groupRol")
        self.vboxLayout = QVBoxLayout(self.groupRol)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.rbJugador = QRadioButton(self.groupRol)
        self.rbJugador.setObjectName(u"rbJugador")

        self.vboxLayout.addWidget(self.rbJugador)

        self.rbArbitro = QRadioButton(self.groupRol)
        self.rbArbitro.setObjectName(u"rbArbitro")

        self.vboxLayout.addWidget(self.rbArbitro)


        self.verticalLayout.addWidget(self.groupRol)

        self.groupDatosJugador = QGroupBox(DialogFormParticipante)
        self.groupDatosJugador.setObjectName(u"groupDatosJugador")
        self.groupDatosJugador.setEnabled(False)
        self.formLayout1 = QFormLayout(self.groupDatosJugador)
        self.formLayout1.setObjectName(u"formLayout1")
        self.formLayout1.setHorizontalSpacing(10)
        self.formLayout1.setVerticalSpacing(10)
        self.label3 = QLabel(self.groupDatosJugador)
        self.label3.setObjectName(u"label3")

        self.formLayout1.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label3)

        self.cmbEquipo = QComboBox(self.groupDatosJugador)
        self.cmbEquipo.setObjectName(u"cmbEquipo")

        self.formLayout1.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cmbEquipo)

        self.label4 = QLabel(self.groupDatosJugador)
        self.label4.setObjectName(u"label4")

        self.formLayout1.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label4)

        self.cmbPosicion = QComboBox(self.groupDatosJugador)
        self.cmbPosicion.setObjectName(u"cmbPosicion")

        self.formLayout1.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbPosicion)

        self.label5 = QLabel(self.groupDatosJugador)
        self.label5.setObjectName(u"label5")

        self.formLayout1.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label5)

        self.spinGoles = QSpinBox(self.groupDatosJugador)
        self.spinGoles.setObjectName(u"spinGoles")
        self.spinGoles.setMaximum(200)

        self.formLayout1.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spinGoles)

        self.label6 = QLabel(self.groupDatosJugador)
        self.label6.setObjectName(u"label6")

        self.formLayout1.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label6)

        self.spinTarjetasAmarillas = QSpinBox(self.groupDatosJugador)
        self.spinTarjetasAmarillas.setObjectName(u"spinTarjetasAmarillas")
        self.spinTarjetasAmarillas.setMaximum(50)

        self.formLayout1.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spinTarjetasAmarillas)

        self.label7 = QLabel(self.groupDatosJugador)
        self.label7.setObjectName(u"label7")

        self.formLayout1.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label7)

        self.spinTarjetasRojas = QSpinBox(self.groupDatosJugador)
        self.spinTarjetasRojas.setObjectName(u"spinTarjetasRojas")
        self.spinTarjetasRojas.setMaximum(50)

        self.formLayout1.setWidget(4, QFormLayout.ItemRole.FieldRole, self.spinTarjetasRojas)


        self.verticalLayout.addWidget(self.groupDatosJugador)

        self.buttonBox = QDialogButtonBox(DialogFormParticipante)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogFormParticipante)
        self.rbJugador.toggled.connect(self.groupDatosJugador.setEnabled)

        QMetaObject.connectSlotsByName(DialogFormParticipante)

    def retranslateUi(self, DialogFormParticipante):
        DialogFormParticipante.setWindowTitle(QCoreApplication.translate("DialogFormParticipante", u"Formulario de Participante", None))
        self.lblTitulo.setText(QCoreApplication.translate("DialogFormParticipante", u"DATOS DEL PARTICIPANTE", None))
        self.groupDatosPersonales.setTitle(QCoreApplication.translate("DialogFormParticipante", u"Datos Personales", None))
        self.label.setText(QCoreApplication.translate("DialogFormParticipante", u"Nombre Completo:", None))
        self.label1.setText(QCoreApplication.translate("DialogFormParticipante", u"Fecha de Nacimiento:", None))
        self.dateFechaNac.setDisplayFormat(QCoreApplication.translate("DialogFormParticipante", u"dd/MM/yyyy", None))
        self.label2.setText(QCoreApplication.translate("DialogFormParticipante", u"Curso:", None))
        self.groupRol.setTitle(QCoreApplication.translate("DialogFormParticipante", u"Rol", None))
        self.rbJugador.setText(QCoreApplication.translate("DialogFormParticipante", u"Jugador", None))
        self.rbArbitro.setText(QCoreApplication.translate("DialogFormParticipante", u"\u00c1rbitro", None))
        self.groupDatosJugador.setTitle(QCoreApplication.translate("DialogFormParticipante", u"Datos de Jugador", None))
        self.label3.setText(QCoreApplication.translate("DialogFormParticipante", u"Equipo:", None))
        self.label4.setText(QCoreApplication.translate("DialogFormParticipante", u"Posici\u00f3n:", None))
        self.label5.setText(QCoreApplication.translate("DialogFormParticipante", u"Goles:", None))
        self.label6.setText(QCoreApplication.translate("DialogFormParticipante", u"Tarjetas Amarillas:", None))
        self.label7.setText(QCoreApplication.translate("DialogFormParticipante", u"Tarjetas Rojas:", None))

