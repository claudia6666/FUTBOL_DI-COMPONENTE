from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 1000)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: rgb(20, 80, 60);\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #00ff00;\n"
"    border: 2px solid #00aa00;\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #00ff00;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #00ff00;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: #00ff00;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #00ff00;\n"
"    color: rgb(0, 80, 40);\n"
"    border: 2px solid #00aa00;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #33ff33;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #00cc00;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: rgb(10, 60, 50);\n"
"    color: #00ff00;\n"
"    border: 2px solid #00aa00;\n"
"    border-radius: 3px;\n"
"    padding: 4"
                        "px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: rgb(10, 60, 50);\n"
"    color: #00ff00;\n"
"    border: 2px solid #00aa00;\n"
"    border-radius: 3px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(10, 60, 50);\n"
"    color: #00ff00;\n"
"    border: 2px solid #00aa00;\n"
"    border-radius: 3px;\n"
"    padding: 4px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.groupLanguage = QGroupBox(self.centralwidget)
        self.groupLanguage.setObjectName(u"groupLanguage")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.groupLanguage.setFont(font)
        self.groupLanguage.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(60, 255, 106);\n"
"")
        self.horizontalLayout = QHBoxLayout(self.groupLanguage)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelLanguage = QLabel(self.groupLanguage)
        self.labelLanguage.setObjectName(u"labelLanguage")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        self.labelLanguage.setFont(font1)
        self.labelLanguage.hide()

        self.horizontalLayout.addWidget(self.labelLanguage)

        self.comboLanguage = QComboBox(self.groupLanguage)
        self.comboLanguage.addItem("")
        self.comboLanguage.addItem("")
        self.comboLanguage.setObjectName(u"comboLanguage")
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        self.comboLanguage.setFont(font2)
        self.comboLanguage.setStyleSheet(u"border-color: rgb(10, 60, 50);\n"
"color: rgb(255, 255, 255);")

        try:
            self.comboLanguage.setMaximumWidth(150)
            self.comboLanguage.setMinimumWidth(150)
            self.comboLanguage.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        except Exception:
            pass

        self.horizontalLayout.addWidget(self.comboLanguage)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.groupLanguage)

        self.clockWidgetContainer = QWidget(self.centralwidget)
        self.clockWidgetContainer.setObjectName(u"clockWidgetContainer")
        self.clockWidgetContainer.setMinimumSize(QSize(0, 200))
        self.clockWidgetContainer.setMaximumHeight(250)
        self.verticalLayout.addWidget(self.clockWidgetContainer)

        self.groupConfig = QGroupBox(self.centralwidget)
        self.groupConfig.setObjectName(u"groupConfig")
        self.groupConfig.setFont(font)
        self.groupConfig.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.groupConfig.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(60, 255, 106);")
        self.verticalLayout_3 = QVBoxLayout(self.groupConfig)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setContentsMargins(8, 8, 8, 8)
        self.layoutMode = QHBoxLayout()
        self.layoutMode.setObjectName(u"layoutMode")
        self.layoutMode.setSpacing(5)
        self.layoutMode.setContentsMargins(0, 0, 0, 0)
        self.labelMode = QLabel(self.groupConfig)
        self.labelMode.setObjectName(u"labelMode")
        self.labelMode.setFont(font1)

        self.layoutMode.addWidget(self.labelMode)

        self.radioClock = QRadioButton(self.groupConfig)
        self.radioClock.setObjectName(u"radioClock")
        font3 = QFont()
        font3.setPointSize(10)
        self.radioClock.setFont(font3)
        self.radioClock.setChecked(True)

        self.layoutMode.addWidget(self.radioClock)

        self.radioTimer = QRadioButton(self.groupConfig)
        self.radioTimer.setObjectName(u"radioTimer")
        self.radioTimer.setFont(font3)

        self.layoutMode.addWidget(self.radioTimer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutMode.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.layoutMode)

        self.check24h = QCheckBox(self.groupConfig)
        self.check24h.setObjectName(u"check24h")
        self.check24h.setFont(font1)
        self.check24h.setChecked(True)

        self.verticalLayout_3.addWidget(self.check24h)

        self.layoutAlarm = QHBoxLayout()
        self.layoutAlarm.setObjectName(u"layoutAlarm")
        self.layoutAlarm.setSpacing(5)
        self.layoutAlarm.setContentsMargins(0, 0, 0, 0)
        self.checkAlarm = QCheckBox(self.groupConfig)
        self.checkAlarm.setObjectName(u"checkAlarm")
        self.checkAlarm.setFont(font1)

        self.layoutAlarm.addWidget(self.checkAlarm)

        self.spinAlarmHour = QSpinBox(self.groupConfig)
        self.spinAlarmHour.setObjectName(u"spinAlarmHour")
        self.spinAlarmHour.setStyleSheet(u"border-color: rgb(10, 60, 50);")
        self.spinAlarmHour.setMaximum(23)
        self.spinAlarmHour.setValue(12)

        self.layoutAlarm.addWidget(self.spinAlarmHour)

        self.label = QLabel(self.groupConfig)
        self.label.setObjectName(u"label")

        self.layoutAlarm.addWidget(self.label)

        self.spinAlarmMinute = QSpinBox(self.groupConfig)
        self.spinAlarmMinute.setObjectName(u"spinAlarmMinute")
        self.spinAlarmMinute.setStyleSheet(u"border-color: rgb(10, 60, 50);")
        self.spinAlarmMinute.setMaximum(59)

        self.layoutAlarm.addWidget(self.spinAlarmMinute)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutAlarm.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.layoutAlarm)

        self.layoutMessage = QHBoxLayout()
        self.layoutMessage.setObjectName(u"layoutMessage")
        self.layoutMessage.setSpacing(5)
        self.layoutMessage.setContentsMargins(0, 0, 0, 0)
        self.labelMessage = QLabel(self.groupConfig)
        self.labelMessage.setObjectName(u"labelMessage")
        self.labelMessage.setFont(font1)

        self.layoutMessage.addWidget(self.labelMessage)

        self.editAlarmMessage = QLineEdit(self.groupConfig)
        self.editAlarmMessage.setObjectName(u"editAlarmMessage")
        self.editAlarmMessage.setStyleSheet(u"border-color: rgb(10, 60, 50);")

        self.layoutMessage.addWidget(self.editAlarmMessage)


        self.verticalLayout_3.addLayout(self.layoutMessage)

        self.layoutTimer = QHBoxLayout()
        self.layoutTimer.setObjectName(u"layoutTimer")
        self.layoutTimer.setSpacing(5)
        self.layoutTimer.setContentsMargins(0, 0, 0, 0)
        self.labelDuration = QLabel(self.groupConfig)
        self.labelDuration.setObjectName(u"labelDuration")
        self.labelDuration.setFont(font1)

        self.layoutTimer.addWidget(self.labelDuration)

        self.spinTimerDuration = QSpinBox(self.groupConfig)
        self.spinTimerDuration.setObjectName(u"spinTimerDuration")
        self.spinTimerDuration.setStyleSheet(u"border-color: rgb(10, 60, 50);")
        self.spinTimerDuration.setMinimum(1)
        self.spinTimerDuration.setMaximum(999)
        self.spinTimerDuration.setValue(90)

        self.layoutTimer.addWidget(self.spinTimerDuration)

        self.checkCountUp = QCheckBox(self.groupConfig)
        self.checkCountUp.setObjectName(u"checkCountUp")
        self.checkCountUp.setFont(font1)
        self.checkCountUp.setChecked(True)

        self.layoutTimer.addWidget(self.checkCountUp)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutTimer.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.layoutTimer)


        self.verticalLayout.addWidget(self.groupConfig)

        self.groupEvents = QGroupBox(self.centralwidget)
        self.groupEvents.setObjectName(u"groupEvents")
        self.groupEvents.setFont(font)
        self.groupEvents.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(60, 255, 106);")
        self.verticalLayout_4 = QVBoxLayout(self.groupEvents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelEvents = QLabel(self.groupEvents)
        self.labelEvents.setObjectName(u"labelEvents")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelEvents.sizePolicy().hasHeightForWidth())
        self.labelEvents.setSizePolicy(sizePolicy)
        self.labelEvents.setMinimumSize(QSize(0, 60))
        self.labelEvents.setFont(font2)
        self.labelEvents.setStyleSheet(u"QLabel {\n"
"    background-color: #f0f0f0;\n"
"    padding: 10px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.labelEvents.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelEvents.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.labelEvents)


        self.verticalLayout.addWidget(self.groupEvents)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Digital Clock Widget - Test Application", None))
        self.groupLanguage.setTitle(QCoreApplication.translate("MainWindow", u"Language / Idioma", None))
        self.labelLanguage.setText(QCoreApplication.translate("MainWindow", u"Select language:", None))
        self.comboLanguage.setItemText(0, QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.comboLanguage.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))

        self.groupConfig.setTitle(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.labelMode.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.radioClock.setText(QCoreApplication.translate("MainWindow", u"Clock", None))
        self.radioTimer.setText(QCoreApplication.translate("MainWindow", u"Timer/Stopwatch", None))
        self.check24h.setText(QCoreApplication.translate("MainWindow", u"24-hour format", None))
        self.checkAlarm.setText(QCoreApplication.translate("MainWindow", u"Enable alarm at", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.labelMessage.setText(QCoreApplication.translate("MainWindow", u"Alarm message:", None))
        self.editAlarmMessage.setText(QCoreApplication.translate("MainWindow", u"Time's up!", None))
        self.labelDuration.setText(QCoreApplication.translate("MainWindow", u"Timer duration (minutes):", None))
        self.checkCountUp.setText(QCoreApplication.translate("MainWindow", u"Count up (stopwatch)", None))
        self.groupEvents.setTitle(QCoreApplication.translate("MainWindow", u"Events Log", None))
        self.labelEvents.setText(QCoreApplication.translate("MainWindow", u"Waiting for events...", None))

