# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QWidget, QAbstractItemView)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 300))
        MainWindow.setMaximumSize(QSize(800, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 300))
        self.centralwidget.setMaximumSize(QSize(800, 300))
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget {\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0.432, x2:1, y2:0.739, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(255, 85, 255, 255));\n"
"}")
        self.Button_frame = QFrame(self.centralwidget)
        self.Button_frame.setObjectName(u"Button_frame")
        self.Button_frame.setGeometry(QRect(0, 0, 211, 300))
        self.Button_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Button_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.DelButton = QPushButton(self.Button_frame)
        self.DelButton.setObjectName(u"DelButton")
        self.DelButton.setGeometry(QRect(10, 260, 191, 31))
        self.DelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.DelButton.setStyleSheet(u"QPushButton {\n"
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
        self.SearchButton = QPushButton(self.Button_frame)
        self.SearchButton.setObjectName(u"SearchButton")
        self.SearchButton.setGeometry(QRect(10, 210, 191, 31))
        self.SearchButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.SearchButton.setStyleSheet(u"QPushButton {\n"
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
        self.EditButton = QPushButton(self.Button_frame)
        self.EditButton.setObjectName(u"EditButton")
        self.EditButton.setGeometry(QRect(10, 160, 191, 31))
        self.EditButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.EditButton.setStyleSheet(u"QPushButton {\n"
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
        self.Addbutton = QPushButton(self.Button_frame)
        self.Addbutton.setObjectName(u"Addbutton")
        self.Addbutton.setGeometry(QRect(10, 110, 191, 31))
        self.Addbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.Addbutton.setStyleSheet(u"QPushButton {\n"
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
        self.CreateDBButton = QPushButton(self.Button_frame)
        self.CreateDBButton.setObjectName(u"CreateDBButton")
        self.CreateDBButton.setGeometry(QRect(10, 60, 191, 31))
        self.CreateDBButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.CreateDBButton.setStyleSheet(u"QPushButton {\n"
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
        self.Table_frame = QFrame(self.centralwidget)
        self.Table_frame.setObjectName(u"Table_frame")
        self.Table_frame.setGeometry(QRect(210, 0, 591, 300))
        self.Table_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Table_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.tableView = QTableView(self.Table_frame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 60, 571, 231))
        self.tableView.setStyleSheet(u"QTableView{\n"
                                     "background-color: rgba(255, 255, 255, 50);\n"
                                     "border: 1px solid rgba(255, 255, 255, 100);\n"
                                     "border-radius: 7px;\n"
                                     "gridline-color: rgb(119, 82, 141);\n"
                                     "color: white;\n"
                                     "}\n"
                                     "QHeaderView::section {\n"
                                     "background-color: transparent;\n"
                                     "border: 1px solid rgba(255, 255, 255, 100);\n"
                                     "border-top-left-radius: 3px;\n"
                                     "border-top-right-radius: 3px;\n"
                                     "color: white;\n"
                                     "height: 25px;\n"
                                     "}\n"
                                     "QTableView::item {\n"
                                     "background-color: transparent;\n"
                                     "border: 1px solid rgba(255, 255, 255, 100);\n"
                                     "border-bottom: 1px solid rgba(255, 255, 255, 100);\n"
                                     "color:white;\n"
                                     "height: 15px;\n"
                                     "font-size: 12pt;\n"
                                     "}\n"
                                     "QTableView::item:selected {\n"
                                     "border: 1px solid rgba(255, 255, 255, 100);\n"
                                     "color: white;\n"
                                     "background-color: rgba(0, 0, 0, 50);\n"
                                     "height: 15px;\n"
                                     "font-size: 12pt;\n"
                                     "}\n"
                                     "QScrollBar:vertical {\n"
                                     "border: none;\n"
                                     "background-color: rgba(0, 0, 0, 30);\n"
                                     "width: 10px;\n"
                                     "margin: 27px 0 10px 0;\n"
                                     "border-radius: 0px;\n"
                                     "}\n"
                                     "QScrollBar::handle:vertical {\n"
                                     "background-color: rgba(0, 0, 0, 80);\n"
                                     "min-height: 30px;\n"
                                     "border-radius: 5px;\n"
                                     "}\n"
                                     "QScrollBar::handle:vertical:hover {\n"
                                     "background-color: rgba(0, 0, 0, 100);\n"
                                     "}\n"
                                     "QScrollBar::handle:vertical:pressed {\n"
                                     "background-color: rgba(0, 0, 0, 70);\n"
                                     "}\n"
                                     "QScrollBar::sub-line:vertical {\n"
                                     "border: none;\n"
                                     "background-color: rgba(0, 0, 0, 50);\n"
                                     "height: 27px;\n"
                                     "border-top-left-radius: 4px;\n"
                                     "border-top-right-radius: 4px;\n"
                                     "subcontrol-position: top;\n"
                                     "subcontrol-origin: margin;\n"
                                     "}\n"
                                     "QScrollBar::sub-line:vertical:hover {\n"
                                     "background-color: rgba(0, 0, 0, 100);\n"
                                     "}\n"
                                     "QScrollBar::sub-line:vertical:pressed {\n"
                                     "background-color: rgba(0, 0, 0, 50);\n"
                                     "}\n"
                                     "QScrollBar::add-line:vertical {\n"
                                     "border: none;\n"
                                     "background-color: rgba(0, 0, 0, 50);\n"
                                     "height: 10px;\n"
                                     "border-bottom-left-radius: 4px;\n"
                                     "border-bottom-right-radius: 4px;\n"
                                     "subcontrol-position: bottom;\n"
                                     "subcontrol-origin: margin;\n"
                                     "}\n"
                                     "QScrollBar::add-line:vertical:hover {\n"
                                     "background-color: rgba(0, 0, 0, 100);\n"
                                     "}\n"
                                     "QScrollBar::add-line:vertical:pressed {\n"
                                     "background-color: rgba(0, 0, 0, 50);\n"
                                     "}\n"
                                     "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                     "background: none;\n"
                                     "}\n"
                                     "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                     "background: none;\n"
                                     "}\n"
                                     "QScrollBar:horizontal {\n"
                                     "border: none;\n"
                                     "background-color: rgba(0, 0, 0, 30);\n"
                                     "height: 10px;\n"
                                     "margin: 0 10px 0 10px;\n"
                                     "border-radius: 0px;\n"
                                     "}\n"
                                     "QScrollBar::handle:horizontal {\n"
                                     "background-color: rgba(0, 0, 0, 80);\n"
                                     "min-width: 30px;\n"
                                     "border-radius: 5px;\n"
                                     "}\n"
                                     "QScrollBar::handle:horizontal:hover {\n"
                                     "background-color: rgba(0, 0, 0, 100);\n"
                                     "}\n"
                                     "QScrollBar::handle:horizontal:pressed {\n"
                                     "background-color: rgba(0, 0, 0, 70);\n"
                                     "}\n"
                                     "QScrollBar::sub-line:horizontal {\n"
                                     "border: none;\n"
                                     "background-color: rgba(0, 0, 0, 50);\n"
                                     "width: 10px;\n"
                                     "border-top-left-radius: 4px;\n"
                                     "border-bottom-left-radius: 4px;\n"
                                     "subcontrol-position: left;\n"
                                     "subcontrol-origin: margin;\n"
                                     "}\n"
                                     "QScrollBar::sub-line:horizontal:hover {\n"
                                     "background-color: rgba(0, 0, 0, 100);\n"
                                     "}\n"
                                     "QScrollBar::sub-line:horizontal:pressed {\n"
                                     "background-color: rgba(0, 0, 0, 50);\n"
                                     "}\n"
                                     "QScrollBar::add-line:horizontal {\n"
                                     "border: none;\n"
                                     "background-color: rgba(0, 0, 0, 50);\n"
                                     "width: 10px;\n"
                                     "border-top-right-radius: 4px;\n"
                                     "border-bottom-right-radius: 4px;\n"
                                     "subcontrol-position: right;\n"
                                     "subcontrol-origin: margin;\n"
                                     "}\n"
                                     "QScrollBar::add-line:horizontal:hover {\n"
                                     "background-color: rgba(0, 0, 0, 100);\n"
                                     "}\n"
                                     "QScrollBar::add-line:horizontal:pressed {\n"
                                     "background-color: rgba(0, 0, 0, 50);\n"
                                     "}\n"
                                     "QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
                                     "background: none;\n"
                                     "}\n"
                                     "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
                                     "background: none;\n"
                                     "}")
        self.tableView.setShowGrid(False)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setDefaultSectionSize(15)
        self.tableView.horizontalHeader().setStyleSheet(u"QHeaderView, QHeaderView::section {\n"
                                                        u"background-color: rgba(0, 0, 0, 80);"
                                                        "font-size: 13pt;\n"
                                                        "color: white;\n"
                                                        "}")
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableView.setFocusPolicy(Qt.NoFocus)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.MainLabel = QLabel(self.centralwidget)
        self.MainLabel.setObjectName(u"MainLabel")
        self.MainLabel.setGeometry(QRect(0, 0, 801, 51))
        self.MainLabel.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: white;")
        self.MainLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432", None))
        self.DelButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.SearchButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.EditButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0445 \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.Addbutton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.CreateDBButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.MainLabel.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432", None))
    # retranslateUi

