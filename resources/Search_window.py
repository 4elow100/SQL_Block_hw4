# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Search_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(310, 340)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(310, 340))
        Form.setMaximumSize(QSize(310, 340))
        Form.setStyleSheet(u"QWidget#Form {\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.432, x2:1, y2:0.739, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(255, 85, 255, 255));\n"
"}")
        self.EmailFrame = QFrame(Form)
        self.EmailFrame.setObjectName(u"EmailFrame")
        self.EmailFrame.setGeometry(QRect(0, 160, 310, 51))
        self.EmailFrame.setStyleSheet(u"")
        self.EmailFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.EmailFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.EmailLabel = QLabel(self.EmailFrame)
        self.EmailLabel.setObjectName(u"EmailLabel")
        self.EmailLabel.setGeometry(QRect(10, 0, 290, 21))
        self.EmailLabel.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"font: 700 12pt \"Segoe UI\";")
        self.EmailLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.EmailEdit = QLineEdit(self.EmailFrame)
        self.EmailEdit.setObjectName(u"EmailEdit")
        self.EmailEdit.setGeometry(QRect(10, 20, 290, 31))
        sizePolicy.setHeightForWidth(self.EmailEdit.sizePolicy().hasHeightForWidth())
        self.EmailEdit.setSizePolicy(sizePolicy)
        self.EmailEdit.setMinimumSize(QSize(290, 31))
        self.EmailEdit.setMaximumSize(QSize(290, 31))
        self.EmailEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 100);\n"
"border-radius: 7px;\n"
"color: white;")
        self.LastNameFrame = QFrame(Form)
        self.LastNameFrame.setObjectName(u"LastNameFrame")
        self.LastNameFrame.setGeometry(QRect(0, 40, 310, 51))
        self.LastNameFrame.setStyleSheet(u"")
        self.LastNameFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LastNameFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.LastNameLabel = QLabel(self.LastNameFrame)
        self.LastNameLabel.setObjectName(u"LastNameLabel")
        self.LastNameLabel.setGeometry(QRect(10, 0, 290, 21))
        self.LastNameLabel.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"font: 700 12pt \"Segoe UI\";")
        self.LastNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LastNameEdit = QLineEdit(self.LastNameFrame)
        self.LastNameEdit.setObjectName(u"LastNameEdit")
        self.LastNameEdit.setGeometry(QRect(10, 20, 290, 31))
        sizePolicy.setHeightForWidth(self.LastNameEdit.sizePolicy().hasHeightForWidth())
        self.LastNameEdit.setSizePolicy(sizePolicy)
        self.LastNameEdit.setMinimumSize(QSize(290, 31))
        self.LastNameEdit.setMaximumSize(QSize(290, 31))
        self.LastNameEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 100);\n"
"border-radius: 7px;\n"
"color: white;")
        self.MainLabel = QLabel(Form)
        self.MainLabel.setObjectName(u"MainLabel")
        self.MainLabel.setGeometry(QRect(10, 10, 290, 21))
        self.MainLabel.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: white;")
        self.MainLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.SearchBTN = QPushButton(Form)
        self.SearchBTN.setObjectName(u"SearchBTN")
        self.SearchBTN.setGeometry(QRect(60, 290, 190, 41))
        self.SearchBTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.SearchBTN.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 255, 255, 80);\n"
"border: 1px solid rgba(255, 255, 255, 100);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font: 700 10pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 80);\n"
"}")
        self.PhoneFrame = QFrame(Form)
        self.PhoneFrame.setObjectName(u"PhoneFrame")
        self.PhoneFrame.setGeometry(QRect(0, 220, 310, 51))
        self.PhoneFrame.setStyleSheet(u"")
        self.PhoneFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PhoneFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.PhoneLabel = QLabel(self.PhoneFrame)
        self.PhoneLabel.setObjectName(u"PhoneLabel")
        self.PhoneLabel.setGeometry(QRect(10, 0, 290, 21))
        self.PhoneLabel.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"font: 700 12pt \"Segoe UI\";")
        self.PhoneLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.PhoneEdit = QLineEdit(self.PhoneFrame)
        self.PhoneEdit.setObjectName(u"PhoneEdit")
        self.PhoneEdit.setGeometry(QRect(10, 20, 290, 31))
        sizePolicy.setHeightForWidth(self.PhoneEdit.sizePolicy().hasHeightForWidth())
        self.PhoneEdit.setSizePolicy(sizePolicy)
        self.PhoneEdit.setMinimumSize(QSize(290, 31))
        self.PhoneEdit.setMaximumSize(QSize(290, 31))
        self.PhoneEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 100);\n"
"border-radius: 7px;\n"
"color: white;")
        self.NameFrame = QFrame(Form)
        self.NameFrame.setObjectName(u"NameFrame")
        self.NameFrame.setGeometry(QRect(0, 100, 310, 51))
        self.NameFrame.setStyleSheet(u"")
        self.NameFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.NameFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.NameLabel = QLabel(self.NameFrame)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setGeometry(QRect(10, 0, 290, 21))
        self.NameLabel.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"font: 700 12pt \"Segoe UI\";")
        self.NameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NameEdit = QLineEdit(self.NameFrame)
        self.NameEdit.setObjectName(u"NameEdit")
        self.NameEdit.setGeometry(QRect(10, 20, 290, 31))
        sizePolicy.setHeightForWidth(self.NameEdit.sizePolicy().hasHeightForWidth())
        self.NameEdit.setSizePolicy(sizePolicy)
        self.NameEdit.setMinimumSize(QSize(290, 31))
        self.NameEdit.setMaximumSize(QSize(290, 31))
        self.NameEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 100);\n"
"border-radius: 7px;\n"
"color: white;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.EmailLabel.setText(QCoreApplication.translate("Form", u"Email", None))
        self.LastNameLabel.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.MainLabel.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.SearchBTN.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.PhoneLabel.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.NameLabel.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
    # retranslateUi
