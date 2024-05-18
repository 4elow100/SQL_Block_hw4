# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Edit_phone.ui'
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

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(310, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QSize(310, 150))
        Frame.setMaximumSize(QSize(310, 150))
        Frame.setStyleSheet(u"QFrame#Frame{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.432, x2:1, y2:0.739, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(255, 85, 255, 255));\n"
"}")
        self.MainLabel = QLabel(Frame)
        self.MainLabel.setObjectName(u"MainLabel")
        self.MainLabel.setGeometry(QRect(10, 10, 290, 21))
        self.MainLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: white;")
        self.MainLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.SaveBTN = QPushButton(Frame)
        self.SaveBTN.setObjectName(u"SaveBTN")
        self.SaveBTN.setGeometry(QRect(60, 100, 190, 41))
        self.SaveBTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.SaveBTN.setStyleSheet(u"QPushButton {\n"
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
        self.PhoneLabel = QLabel(Frame)
        self.PhoneLabel.setObjectName(u"PhoneLabel")
        self.PhoneLabel.setGeometry(QRect(10, 40, 290, 21))
        self.PhoneLabel.setStyleSheet(u"background-color: transparent;\n"
"color: white;\n"
"font: 700 12pt \"Segoe UI\";")
        self.PhoneLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.PhoneEdit = QLineEdit(Frame)
        self.PhoneEdit.setObjectName(u"PhoneEdit")
        self.PhoneEdit.setGeometry(QRect(10, 60, 290, 31))
        sizePolicy.setHeightForWidth(self.PhoneEdit.sizePolicy().hasHeightForWidth())
        self.PhoneEdit.setSizePolicy(sizePolicy)
        self.PhoneEdit.setMinimumSize(QSize(290, 31))
        self.PhoneEdit.setMaximumSize(QSize(290, 31))
        self.PhoneEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 100);\n"
"border-radius: 7px;\n"
"color: white;")

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043d\u043e\u043c\u0435\u0440\u0430 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.MainLabel.setText(QCoreApplication.translate("Frame", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043d\u043e\u043c\u0435\u0440\u0430 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.SaveBTN.setText(QCoreApplication.translate("Frame", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.PhoneLabel.setText(QCoreApplication.translate("Frame", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
    # retranslateUi

