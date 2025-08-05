# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainApp(object):
    def setupUi(self, MainApp):
        if not MainApp.objectName():
            MainApp.setObjectName(u"MainApp")
        MainApp.resize(800, 480)
        self.horizontalLayout = QHBoxLayout(MainApp)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftPanel = QFrame(MainApp)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.leftPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.appLogo = QFrame(self.leftPanel)
        self.appLogo.setObjectName(u"appLogo")
        self.appLogo.setFrameShape(QFrame.Shape.StyledPanel)
        self.appLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.appLogo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo = QLabel(self.appLogo)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(30, 30))
        self.logo.setMaximumSize(QSize(30, 30))
        self.logo.setPixmap(QPixmap(u":/icons/solar-linear-icons/magic-stick-3.svg"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo)

        self.appName = QLabel(self.appLogo)
        self.appName.setObjectName(u"appName")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.appName.setFont(font)

        self.horizontalLayout_2.addWidget(self.appName)


        self.verticalLayout.addWidget(self.appLogo)

        self.setUpPanel = QFrame(self.leftPanel)
        self.setUpPanel.setObjectName(u"setUpPanel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setUpPanel.sizePolicy().hasHeightForWidth())
        self.setUpPanel.setSizePolicy(sizePolicy)
        self.setUpPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.setUpPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.setUpPanel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.defaultSetup = QPushButton(self.setUpPanel)
        self.defaultSetup.setObjectName(u"defaultSetup")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.defaultSetup.sizePolicy().hasHeightForWidth())
        self.defaultSetup.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/icons/solar-linear-icons/restart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.defaultSetup.setIcon(icon)
        self.defaultSetup.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.defaultSetup)

        self.logCSV = QPushButton(self.setUpPanel)
        self.logCSV.setObjectName(u"logCSV")
        sizePolicy1.setHeightForWidth(self.logCSV.sizePolicy().hasHeightForWidth())
        self.logCSV.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/solar-linear-icons/folder-with-files.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logCSV.setIcon(icon1)
        self.logCSV.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.logCSV)


        self.verticalLayout.addWidget(self.setUpPanel)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.rightPanel = QFrame(MainApp)
        self.rightPanel.setObjectName(u"rightPanel")
        self.rightPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.rightPanel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.optionPanel = QFrame(self.rightPanel)
        self.optionPanel.setObjectName(u"optionPanel")
        self.optionPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.optionPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.optionPanel)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuPanel = QFrame(self.optionPanel)
        self.menuPanel.setObjectName(u"menuPanel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menuPanel.sizePolicy().hasHeightForWidth())
        self.menuPanel.setSizePolicy(sizePolicy2)
        self.menuPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.menuPanel)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.menuButton = QPushButton(self.menuPanel)
        self.menuButton.setObjectName(u"menuButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/solar-linear-icons/menu-dots-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuButton.setIcon(icon2)

        self.horizontalLayout_13.addWidget(self.menuButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.menuLabel = QLabel(self.menuPanel)
        self.menuLabel.setObjectName(u"menuLabel")
        self.menuLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.menuLabel)


        self.horizontalLayout_3.addWidget(self.menuPanel)

        self.mainScreen = QFrame(self.optionPanel)
        self.mainScreen.setObjectName(u"mainScreen")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainScreen.sizePolicy().hasHeightForWidth())
        self.mainScreen.setSizePolicy(sizePolicy3)
        self.mainScreen.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainScreen.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.mainScreen)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.display = QLabel(self.mainScreen)
        self.display.setObjectName(u"display")
        self.display.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.display)


        self.horizontalLayout_3.addWidget(self.mainScreen)

        self.appInterface = QFrame(self.optionPanel)
        self.appInterface.setObjectName(u"appInterface")
        self.appInterface.setFrameShape(QFrame.Shape.StyledPanel)
        self.appInterface.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.appInterface)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.minimize = QPushButton(self.appInterface)
        self.minimize.setObjectName(u"minimize")
        icon3 = QIcon()
        icon3.addFile(u":/icons/solar-linear-icons/minus-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize.setIcon(icon3)

        self.horizontalLayout_12.addWidget(self.minimize)

        self.maximize = QPushButton(self.appInterface)
        self.maximize.setObjectName(u"maximize")
        icon4 = QIcon()
        icon4.addFile(u":/icons/solar-linear-icons/circle-top-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize.setIcon(icon4)

        self.horizontalLayout_12.addWidget(self.maximize)

        self.quit = QPushButton(self.appInterface)
        self.quit.setObjectName(u"quit")
        icon5 = QIcon()
        icon5.addFile(u":/icons/solar-linear-icons/exit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.quit.setIcon(icon5)

        self.horizontalLayout_12.addWidget(self.quit)


        self.horizontalLayout_3.addWidget(self.appInterface)


        self.verticalLayout_3.addWidget(self.optionPanel)

        self.mainFrame = QFrame(self.rightPanel)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.mainFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.basicView = QWidget()
        self.basicView.setObjectName(u"basicView")
        self.verticalLayout_5 = QVBoxLayout(self.basicView)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header = QFrame(self.basicView)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.header)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.basicViewLabel = QLabel(self.header)
        self.basicViewLabel.setObjectName(u"basicViewLabel")
        self.basicViewLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.basicViewLabel, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_5.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.displayInfor = QFrame(self.basicView)
        self.displayInfor.setObjectName(u"displayInfor")
        sizePolicy.setHeightForWidth(self.displayInfor.sizePolicy().hasHeightForWidth())
        self.displayInfor.setSizePolicy(sizePolicy)
        self.displayInfor.setFrameShape(QFrame.Shape.StyledPanel)
        self.displayInfor.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.displayInfor)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.setupInfor = QFrame(self.displayInfor)
        self.setupInfor.setObjectName(u"setupInfor")
        self.setupInfor.setFrameShape(QFrame.Shape.StyledPanel)
        self.setupInfor.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.setupInfor)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_16 = QFrame(self.setupInfor)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.frame_16)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.setupInfor)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_17)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.frame_20)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignLeft)

        self.setupVoltageDisplay = QLCDNumber(self.frame_20)
        self.setupVoltageDisplay.setObjectName(u"setupVoltageDisplay")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.setupVoltageDisplay.sizePolicy().hasHeightForWidth())
        self.setupVoltageDisplay.setSizePolicy(sizePolicy4)
        self.setupVoltageDisplay.setSmallDecimalPoint(False)
        self.setupVoltageDisplay.setDigitCount(5)

        self.horizontalLayout_8.addWidget(self.setupVoltageDisplay)


        self.verticalLayout_13.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_17)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.frame_21)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignLeft)

        self.setupCurrentDisplay = QLCDNumber(self.frame_21)
        self.setupCurrentDisplay.setObjectName(u"setupCurrentDisplay")
        sizePolicy4.setHeightForWidth(self.setupCurrentDisplay.sizePolicy().hasHeightForWidth())
        self.setupCurrentDisplay.setSizePolicy(sizePolicy4)

        self.horizontalLayout_9.addWidget(self.setupCurrentDisplay)


        self.verticalLayout_13.addWidget(self.frame_21)


        self.verticalLayout_9.addWidget(self.frame_17)


        self.horizontalLayout_6.addWidget(self.setupInfor)

        self.outputInfor = QFrame(self.displayInfor)
        self.outputInfor.setObjectName(u"outputInfor")
        self.outputInfor.setFrameShape(QFrame.Shape.StyledPanel)
        self.outputInfor.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.outputInfor)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_18 = QFrame(self.outputInfor)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_18)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.frame_18)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.outputInfor)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_19)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.frame_22)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12, 0, Qt.AlignmentFlag.AlignLeft)

        self.outputVoltageDisplay = QLCDNumber(self.frame_22)
        self.outputVoltageDisplay.setObjectName(u"outputVoltageDisplay")
        sizePolicy4.setHeightForWidth(self.outputVoltageDisplay.sizePolicy().hasHeightForWidth())
        self.outputVoltageDisplay.setSizePolicy(sizePolicy4)

        self.horizontalLayout_11.addWidget(self.outputVoltageDisplay)


        self.verticalLayout_14.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.frame_23)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13, 0, Qt.AlignmentFlag.AlignLeft)

        self.outputCurrentDisplay = QLCDNumber(self.frame_23)
        self.outputCurrentDisplay.setObjectName(u"outputCurrentDisplay")
        sizePolicy4.setHeightForWidth(self.outputCurrentDisplay.sizePolicy().hasHeightForWidth())
        self.outputCurrentDisplay.setSizePolicy(sizePolicy4)

        self.horizontalLayout_10.addWidget(self.outputCurrentDisplay)


        self.verticalLayout_14.addWidget(self.frame_23)


        self.verticalLayout_10.addWidget(self.frame_19)


        self.horizontalLayout_6.addWidget(self.outputInfor)


        self.verticalLayout_5.addWidget(self.displayInfor)

        self.stackedWidget.addWidget(self.basicView)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_12 = QFrame(self.page_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.page_2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.mainFrame)

        self.basicSetup = QFrame(self.rightPanel)
        self.basicSetup.setObjectName(u"basicSetup")
        self.basicSetup.setFrameShape(QFrame.Shape.StyledPanel)
        self.basicSetup.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.basicSetup)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.setup = QFrame(self.basicSetup)
        self.setup.setObjectName(u"setup")
        self.setup.setFrameShape(QFrame.Shape.StyledPanel)
        self.setup.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.setup)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.setupVoltageLabel = QLabel(self.setup)
        self.setupVoltageLabel.setObjectName(u"setupVoltageLabel")

        self.horizontalLayout_5.addWidget(self.setupVoltageLabel)

        self.setupVoltageInput = QLineEdit(self.setup)
        self.setupVoltageInput.setObjectName(u"setupVoltageInput")

        self.horizontalLayout_5.addWidget(self.setupVoltageInput)

        self.setupCurrentLabel = QLabel(self.setup)
        self.setupCurrentLabel.setObjectName(u"setupCurrentLabel")

        self.horizontalLayout_5.addWidget(self.setupCurrentLabel)

        self.setupCurrentInput = QLineEdit(self.setup)
        self.setupCurrentInput.setObjectName(u"setupCurrentInput")

        self.horizontalLayout_5.addWidget(self.setupCurrentInput)

        self.setupButton = QPushButton(self.setup)
        self.setupButton.setObjectName(u"setupButton")

        self.horizontalLayout_5.addWidget(self.setupButton)


        self.horizontalLayout_4.addWidget(self.setup)

        self.outPutControl = QFrame(self.basicSetup)
        self.outPutControl.setObjectName(u"outPutControl")
        self.outPutControl.setFrameShape(QFrame.Shape.StyledPanel)
        self.outPutControl.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.outPutControl)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.outPutStatus = QLabel(self.outPutControl)
        self.outPutStatus.setObjectName(u"outPutStatus")

        self.horizontalLayout_7.addWidget(self.outPutStatus)

        self.outPutButton = QPushButton(self.outPutControl)
        self.outPutButton.setObjectName(u"outPutButton")

        self.horizontalLayout_7.addWidget(self.outPutButton)


        self.horizontalLayout_4.addWidget(self.outPutControl)


        self.verticalLayout_3.addWidget(self.basicSetup)


        self.horizontalLayout.addWidget(self.rightPanel)


        self.retranslateUi(MainApp)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainApp)
    # setupUi

    def retranslateUi(self, MainApp):
        MainApp.setWindowTitle(QCoreApplication.translate("MainApp", u"Form", None))
        self.logo.setText("")
        self.appName.setText(QCoreApplication.translate("MainApp", u"WPS150S", None))
        self.defaultSetup.setText(QCoreApplication.translate("MainApp", u"Default Setup", None))
        self.logCSV.setText(QCoreApplication.translate("MainApp", u"Log CSV", None))
        self.menuButton.setText("")
        self.menuLabel.setText(QCoreApplication.translate("MainApp", u"MENU", None))
        self.display.setText(QCoreApplication.translate("MainApp", u"Main Screen", None))
        self.minimize.setText("")
        self.maximize.setText("")
        self.quit.setText("")
        self.basicViewLabel.setText(QCoreApplication.translate("MainApp", u"Basic View", None))
        self.label_7.setText(QCoreApplication.translate("MainApp", u"Setup", None))
        self.label_10.setText(QCoreApplication.translate("MainApp", u"Voltage", None))
        self.label_11.setText(QCoreApplication.translate("MainApp", u"Curent", None))
        self.label_8.setText(QCoreApplication.translate("MainApp", u"Output", None))
        self.label_12.setText(QCoreApplication.translate("MainApp", u"Voltage", None))
        self.label_13.setText(QCoreApplication.translate("MainApp", u"Curent", None))
        self.label_6.setText(QCoreApplication.translate("MainApp", u"Graph View", None))
        self.setupVoltageLabel.setText(QCoreApplication.translate("MainApp", u"Voltage", None))
        self.setupCurrentLabel.setText(QCoreApplication.translate("MainApp", u"Current", None))
        self.setupButton.setText(QCoreApplication.translate("MainApp", u"Set", None))
        self.outPutStatus.setText(QCoreApplication.translate("MainApp", u"Status", None))
        self.outPutButton.setText(QCoreApplication.translate("MainApp", u"ON/OFF", None))
    # retranslateUi

