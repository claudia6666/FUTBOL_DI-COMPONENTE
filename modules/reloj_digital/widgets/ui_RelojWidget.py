from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_DigitalClockWidget(object):
    def setupUi(self, DigitalClockWidget):
        if not DigitalClockWidget.objectName():
            DigitalClockWidget.setObjectName(u"DigitalClockWidget")
        DigitalClockWidget.resize(611, 250)
        DigitalClockWidget.setStyleSheet(u"QWidget#DigitalClockWidget {\n"
"    background-color: rgb(20, 80, 60);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLCDNumber {\n"
"    background-color: rgb(10, 60, 50);\n"
"    color: #7fff7f;\n"
"    border: 3px solid #00ff00;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #93da97;\n"
"    color: rgb(1, 107, 97);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #a8e8ac;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #7ec582;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #5a7a5c;\n"
"    color: #3a5a4c;\n"
"}")
        self.verticalLayout = QVBoxLayout(DigitalClockWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.lcdDisplay = QLCDNumber(DigitalClockWidget)
        self.lcdDisplay.setObjectName(u"lcdDisplay")
        self.lcdDisplay.setMinimumSize(QSize(0, 80))
        self.lcdDisplay.setStyleSheet(u"border-color: rgb(133, 255, 137);")
        self.lcdDisplay.setDigitCount(8)
        self.lcdDisplay.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.verticalLayout.addWidget(self.lcdDisplay)

        self.controlsLayout = QHBoxLayout()
        self.controlsLayout.setSpacing(10)
        self.controlsLayout.setObjectName(u"controlsLayout")
        self.btnStart = QPushButton(DigitalClockWidget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setMinimumSize(QSize(0, 40))
        self.btnStart.setStyleSheet(u"background-color: rgb(60, 255, 106);\n"
"color: rgb(10, 60, 50);\n"
"border-color: rgb(10, 60, 50);")

        self.controlsLayout.addWidget(self.btnStart)

        self.btnPause = QPushButton(DigitalClockWidget)
        self.btnPause.setObjectName(u"btnPause")
        self.btnPause.setEnabled(False)
        self.btnPause.setMinimumSize(QSize(0, 40))

        self.controlsLayout.addWidget(self.btnPause)

        self.btnReset = QPushButton(DigitalClockWidget)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setMinimumSize(QSize(0, 40))
        self.btnReset.setStyleSheet(u"background-color: rgb(60, 255, 106);\n"
"color: rgb(10, 60, 50);\n"
"border-color: rgb(10, 60, 50);")

        self.controlsLayout.addWidget(self.btnReset)


        self.verticalLayout.addLayout(self.controlsLayout)


        self.retranslateUi(DigitalClockWidget)

        QMetaObject.connectSlotsByName(DigitalClockWidget)

    def retranslateUi(self, DigitalClockWidget):
        DigitalClockWidget.setWindowTitle(QCoreApplication.translate("DigitalClockWidget", u"Digital Clock", None))
        self.btnStart.setText(QCoreApplication.translate("DigitalClockWidget", u"Start", None))
        self.btnPause.setText(QCoreApplication.translate("DigitalClockWidget", u"Pause", None))
        self.btnReset.setText(QCoreApplication.translate("DigitalClockWidget", u"Reset", None))

