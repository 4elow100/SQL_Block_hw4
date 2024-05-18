# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Message_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 140)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(300, 140))
        Dialog.setMaximumSize(QSize(300, 140))
        Dialog.setStyleSheet(u"QDialog{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.432, x2:1, y2:0.739, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(255, 85, 255, 255));\n"
"}")
        self.MainLabel = QLabel(Dialog)
        self.MainLabel.setObjectName(u"MainLabel")
        self.MainLabel.setGeometry(QRect(9, 10, 281, 70))
        self.MainLabel.setStyleSheet(u"color: white;")
        self.MainLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.OkBTN = QPushButton(Dialog)
        self.OkBTN.setObjectName(u"OkBTN")
        self.OkBTN.setGeometry(QRect(90, 90, 121, 41))
        self.OkBTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.OkBTN.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.MainLabel.setText("")
        self.OkBTN.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

