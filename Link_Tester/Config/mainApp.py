# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestApp.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Application(object):
    def setupUi(self, Application):
        if not Application.objectName():
            Application.setObjectName(u"Application")
        Application.resize(800, 480)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InputTablet))
        Application.setWindowIcon(icon)
        self.overall_stack = QVBoxLayout(Application)
        self.overall_stack.setObjectName(u"overall_stack")
        self.top_stack = QHBoxLayout()
        self.top_stack.setObjectName(u"top_stack")
        self.setting_stack = QVBoxLayout()
        self.setting_stack.setObjectName(u"setting_stack")
        self.testModes = QComboBox(Application)
        self.testModes.addItem("")
        self.testModes.addItem("")
        self.testModes.setObjectName(u"testModes")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testModes.sizePolicy().hasHeightForWidth())
        self.testModes.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.testModes.setFont(font)
        self.testModes.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #444;\n"
"    border-radius: 5px;\n"
"    padding: 6px;\n"
"    font-size: 16px;\n"
"    background-color: #fafafa;\n"
"}\n"
"")

        self.setting_stack.addWidget(self.testModes)

        self.readSeriesNumber = QLineEdit(Application)
        self.readSeriesNumber.setObjectName(u"readSeriesNumber")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.readSeriesNumber.sizePolicy().hasHeightForWidth())
        self.readSeriesNumber.setSizePolicy(sizePolicy1)
        font1 = QFont()
        self.readSeriesNumber.setFont(font1)
        self.readSeriesNumber.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #444;\n"
"    border-radius: 5px;\n"
"    padding: 6px;\n"
"    font-size: 16px;\n"
"    background-color: #fafafa;\n"
"}\n"
"")

        self.setting_stack.addWidget(self.readSeriesNumber)

        self.setting_stack.setStretch(0, 1)
        self.setting_stack.setStretch(1, 1)

        self.top_stack.addLayout(self.setting_stack)

        self.setting_button_stack = QVBoxLayout()
        self.setting_button_stack.setObjectName(u"setting_button_stack")
        self.selectButton = QPushButton(Application)
        self.selectButton.setObjectName(u"selectButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.selectButton.sizePolicy().hasHeightForWidth())
        self.selectButton.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setBold(True)
        self.selectButton.setFont(font2)
        self.selectButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #555;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d0d0d0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"}\n"
"")

        self.setting_button_stack.addWidget(self.selectButton)

        self.resetButton = QPushButton(Application)
        self.resetButton.setObjectName(u"resetButton")
        sizePolicy2.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy2)
        self.resetButton.setFont(font2)
        self.resetButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #555;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d0d0d0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"}\n"
"")

        self.setting_button_stack.addWidget(self.resetButton)

        self.setting_button_stack.setStretch(0, 1)
        self.setting_button_stack.setStretch(1, 1)

        self.top_stack.addLayout(self.setting_button_stack)

        self.top_stack.setStretch(0, 8)
        self.top_stack.setStretch(1, 2)

        self.overall_stack.addLayout(self.top_stack)

        self.middle_stack = QHBoxLayout()
        self.middle_stack.setObjectName(u"middle_stack")
        self.textDisplay = QTextEdit(Application)
        self.textDisplay.setObjectName(u"textDisplay")

        self.middle_stack.addWidget(self.textDisplay)

        self.operator_stack = QVBoxLayout()
        self.operator_stack.setObjectName(u"operator_stack")
        self.button_num1 = QPushButton(Application)
        self.button_num1.setObjectName(u"button_num1")
        sizePolicy2.setHeightForWidth(self.button_num1.sizePolicy().hasHeightForWidth())
        self.button_num1.setSizePolicy(sizePolicy2)
        self.button_num1.setFont(font2)
        self.button_num1.setStyleSheet(u"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #555;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2e7d32 ;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"}\n"
"")

        self.operator_stack.addWidget(self.button_num1)

        self.button_num2 = QPushButton(Application)
        self.button_num2.setObjectName(u"button_num2")
        sizePolicy2.setHeightForWidth(self.button_num2.sizePolicy().hasHeightForWidth())
        self.button_num2.setSizePolicy(sizePolicy2)
        self.button_num2.setFont(font2)
        self.button_num2.setStyleSheet(u"QPushButton {\n"
"    background-color: #e0e0e0;\n"
"    border: 2px solid #555;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c62828 ;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c0c0c0;\n"
"}\n"
"")

        self.operator_stack.addWidget(self.button_num2)

        self.operator_stack.setStretch(0, 1)
        self.operator_stack.setStretch(1, 1)

        self.middle_stack.addLayout(self.operator_stack)

        self.middle_stack.setStretch(0, 8)
        self.middle_stack.setStretch(1, 2)

        self.overall_stack.addLayout(self.middle_stack)

        self.bottom_stack = QHBoxLayout()
        self.bottom_stack.setObjectName(u"bottom_stack")
        self.progressBar = QProgressBar(Application)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy3)
        self.progressBar.setBaseSize(QSize(0, 0))
        self.progressBar.setFont(font2)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #555;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: #e0e0e0;\n"
"    min-height: 30px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #0277bd;  /* Blue */\n"
"    width: 10px;\n"
"}\n"
"")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.bottom_stack.addWidget(self.progressBar)

        self.appVersion = QLineEdit(Application)
        self.appVersion.setObjectName(u"appVersion")
        self.appVersion.setFont(font)
        self.appVersion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.appVersion.setDragEnabled(False)
        self.appVersion.setReadOnly(True)

        self.bottom_stack.addWidget(self.appVersion)

        self.bottom_stack.setStretch(0, 8)
        self.bottom_stack.setStretch(1, 2)

        self.overall_stack.addLayout(self.bottom_stack)

        self.overall_stack.setStretch(0, 2)
        self.overall_stack.setStretch(1, 8)
        self.overall_stack.setStretch(2, 1)

        self.retranslateUi(Application)

        QMetaObject.connectSlotsByName(Application)
    # setupUi

    def retranslateUi(self, Application):
        Application.setWindowTitle(QCoreApplication.translate("Application", u"WUNU-LINK PCBA TEST APP", None))
        self.testModes.setItemText(0, QCoreApplication.translate("Application", u"                                               LINK MODE", None))
        self.testModes.setItemText(1, QCoreApplication.translate("Application", u"                                                L-Z MODE", None))

        self.readSeriesNumber.setPlaceholderText(QCoreApplication.translate("Application", u"                                                Input Board Serial Number", None))
        self.selectButton.setText(QCoreApplication.translate("Application", u"SELECT MODE", None))
        self.resetButton.setText(QCoreApplication.translate("Application", u"RESET", None))
        self.button_num1.setText(QCoreApplication.translate("Application", u"YES", None))
        self.button_num2.setText(QCoreApplication.translate("Application", u"NO", None))
        self.appVersion.setText(QCoreApplication.translate("Application", u"V0.1.0", None))
    # retranslateUi

