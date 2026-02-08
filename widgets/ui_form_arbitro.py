

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_DialogFormArbitro(object):
    def setupUi(self, DialogFormArbitro):
        if not DialogFormArbitro.objectName():
            DialogFormArbitro.setObjectName(u"DialogFormArbitro")
        DialogFormArbitro.resize(500, 300)
        DialogFormArbitro.setStyleSheet(u"background-color: rgb(113, 177, 129);")
        self.verticalLayout = QVBoxLayout(DialogFormArbitro)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitulo = QLabel(DialogFormArbitro)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.groupBoxDatos = QGroupBox(DialogFormArbitro)
        self.groupBoxDatos.setObjectName(u"groupBoxDatos")
        self.groupBoxDatos.setStyleSheet(u"QGroupBox {\n"
"    color: white;\n"
"    border: 2px solid rgb(1, 107, 97);\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.formLayout = QFormLayout(self.groupBoxDatos)
        self.formLayout.setSpacing(15)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(15, 15, 15, 15)
        self.lblNombre = QLabel(self.groupBoxDatos)
        self.lblNombre.setObjectName(u"lblNombre")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.lblNombre.setFont(font1)
        self.lblNombre.setStyleSheet(u"color: white;")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txtNombre = QLineEdit(self.groupBoxDatos)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 10pt;\n"
"}\n"
"QLineEdit:focus {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid #93da97;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.lblFechaNac = QLabel(self.groupBoxDatos)
        self.lblFechaNac.setObjectName(u"lblFechaNac")
        self.lblFechaNac.setFont(font1)
        self.lblFechaNac.setStyleSheet(u"color: white;")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblFechaNac)

        self.dateFechaNac = QDateEdit(self.groupBoxDatos)
        self.dateFechaNac.setObjectName(u"dateFechaNac")
        self.dateFechaNac.setStyleSheet(u"QDateEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 10pt;\n"
"}\n"
"QDateEdit:focus {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid #93da97;\n"
"}")
        self.dateFechaNac.setCalendarPopupEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateFechaNac)

        self.lblCurso = QLabel(self.groupBoxDatos)
        self.lblCurso.setObjectName(u"lblCurso")
        self.lblCurso.setFont(font1)
        self.lblCurso.setStyleSheet(u"color: white;")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblCurso)

        self.cmbCurso = QComboBox(self.groupBoxDatos)
        self.cmbCurso.addItem("")
        self.cmbCurso.addItem("")
        self.cmbCurso.addItem("")
        self.cmbCurso.addItem("")
        self.cmbCurso.addItem("")
        self.cmbCurso.setObjectName(u"cmbCurso")
        self.cmbCurso.setStyleSheet(u"QComboBox {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-size: 10pt;\n"
"}\n"
"QComboBox:focus {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 2px solid #93da97;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    color: black;\n"
"    selection-background-color: #93da97;\n"
"    selection-color: rgb(1, 107, 97);\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbCurso)


        self.verticalLayout.addWidget(self.groupBoxDatos)

        self.buttonBox = QDialogButtonBox(DialogFormArbitro)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(1, 107, 97);\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px 20px;\n"
"    font-weight: bold;\n"
"    min-width: 80px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #93da97;\n"
"    color: rgb(1, 107, 97);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1, 107, 97);\n"
"}")

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogFormArbitro)
        self.buttonBox.accepted.connect(DialogFormArbitro.accept)
        self.buttonBox.rejected.connect(DialogFormArbitro.reject)

        QMetaObject.connectSlotsByName(DialogFormArbitro)

    def retranslateUi(self, DialogFormArbitro):
        DialogFormArbitro.setWindowTitle(QCoreApplication.translate("DialogFormArbitro", u"Formulario de \u00c1rbitro", None))
        self.lblTitulo.setText(QCoreApplication.translate("DialogFormArbitro", u"Registro de \u00c1rbitro", None))
        self.groupBoxDatos.setTitle(QCoreApplication.translate("DialogFormArbitro", u"Datos del \u00c1rbitro", None))
        self.lblNombre.setText(QCoreApplication.translate("DialogFormArbitro", u"Nombre:", None))
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("DialogFormArbitro", u"Nombre completo", None))
        self.lblFechaNac.setText(QCoreApplication.translate("DialogFormArbitro", u"Fecha de Nacimiento:", None))
        self.lblCurso.setText(QCoreApplication.translate("DialogFormArbitro", u"Curso:", None))
        self.cmbCurso.setItemText(0, QCoreApplication.translate("DialogFormArbitro", u"-- Seleccionar --", None))
        self.cmbCurso.setItemText(1, QCoreApplication.translate("DialogFormArbitro", u"1\u00ba DAM", None))
        self.cmbCurso.setItemText(2, QCoreApplication.translate("DialogFormArbitro", u"2\u00ba DAM", None))
        self.cmbCurso.setItemText(3, QCoreApplication.translate("DialogFormArbitro", u"1\u00ba ASIR", None))
        self.cmbCurso.setItemText(4, QCoreApplication.translate("DialogFormArbitro", u"2\u00ba ASIR", None))


