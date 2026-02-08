

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_DialogFormEquipo(object):
    def setupUi(self, DialogFormEquipo):
        if not DialogFormEquipo.objectName():
            DialogFormEquipo.setObjectName(u"DialogFormEquipo")
        DialogFormEquipo.resize(599, 465)
        DialogFormEquipo.setStyleSheet(u"\n"
"   QDialog {\n"
"       background-color: rgb(113, 177, 129);\n"
"   }\n"
"   QLabel#lblTitulo {\n"
"       font-size: 22pt;\n"
"       font-weight: bold;\n"
"       color: white;\n"
"       background-color: rgb(1, 107, 97);\n"
"       border-radius: 8px;\n"
"       padding: 10px;\n"
"   }\n"
"   QPushButton {\n"
"       background-color: rgb(1, 107, 97);\n"
"       color: white;\n"
"       border-radius: 8px;\n"
"       padding: 8px;\n"
"       font-weight: bold;\n"
"   }\n"
"   QPushButton:hover {\n"
"       background-color: #93da97;\n"
"       color: rgb(1, 107, 97);\n"
"   }\n"
"   QPushButton:pressed {\n"
"       background-color: rgb(1, 107, 97);\n"
"   }\n"
"   QLineEdit, QComboBox {\n"
"       border: 2px solid rgb(1,107,97);\n"
"       border-radius: 5px;\n"
"       padding: 4px;\n"
"       background-color: white;\n"
"   }\n"
"   QLabel#lblVistaPrevia {\n"
"       border: 2px solid rgb(1,107,97);\n"
"       border-radius: 8px;\n"
"       background-color: white;\n"
"   }\n"
"   ")
        self.verticalLayout = QVBoxLayout(DialogFormEquipo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitulo = QLabel(DialogFormEquipo)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.groupBox = QGroupBox(DialogFormEquipo)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.lblNombre = QLabel(self.groupBox)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txtNombre = QLineEdit(self.groupBox)
        self.txtNombre.setObjectName(u"txtNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.lblCurso = QLabel(self.groupBox)
        self.lblCurso.setObjectName(u"lblCurso")
        self.lblCurso.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblCurso)

        self.cmbCurso = QComboBox(self.groupBox)
        self.cmbCurso.setObjectName(u"cmbCurso")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbCurso)

        self.lblColor = QLabel(self.groupBox)
        self.lblColor.setObjectName(u"lblColor")
        self.lblColor.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblColor)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txtColor = QLineEdit(self.groupBox)
        self.txtColor.setObjectName(u"txtColor")
        self.txtColor.setReadOnly(True)

        self.horizontalLayout.addWidget(self.txtColor)

        self.btnSeleccionarColor = QPushButton(self.groupBox)
        self.btnSeleccionarColor.setObjectName(u"btnSeleccionarColor")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btnSeleccionarColor.setFont(font1)

        self.horizontalLayout.addWidget(self.btnSeleccionarColor)


        self.formLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(DialogFormEquipo)
        self.buttonBox.setObjectName(u"buttonBox")
        font2 = QFont()
        font2.setPointSize(11)
        self.buttonBox.setFont(font2)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogFormEquipo)
        self.buttonBox.accepted.connect(DialogFormEquipo.accept)
        self.buttonBox.rejected.connect(DialogFormEquipo.reject)

        QMetaObject.connectSlotsByName(DialogFormEquipo)

    def retranslateUi(self, DialogFormEquipo):
        DialogFormEquipo.setWindowTitle(QCoreApplication.translate("DialogFormEquipo", u"Formulario de Equipo", None))
        self.lblTitulo.setText(QCoreApplication.translate("DialogFormEquipo", u"DATOS DEL EQUIPO", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogFormEquipo", u"Informaci\u00f3n del Equipo", None))
        self.lblNombre.setText(QCoreApplication.translate("DialogFormEquipo", u"Nombre del Equipo:", None))
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("DialogFormEquipo", u"Ej: Los Tigres", None))
        self.lblCurso.setText(QCoreApplication.translate("DialogFormEquipo", u"Curso:", None))
        self.lblColor.setText(QCoreApplication.translate("DialogFormEquipo", u"Color de Camiseta:", None))
        self.txtColor.setPlaceholderText(QCoreApplication.translate("DialogFormEquipo", u"Seleccionar color", None))
        self.btnSeleccionarColor.setText(QCoreApplication.translate("DialogFormEquipo", u"Seleccionar", None))

