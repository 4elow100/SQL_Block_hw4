import sys
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QMainWindow
from resources import Main_Window, Edit_window, Add_phone, Edit_phone, Search_window, Add_client, Message_window
from resources.DataBase import DataBase


class TabelData(QAbstractTableModel):
    def __init__(self, data, headers, parent=None):
        super().__init__()
        self._data = data
        self._headers = headers
        self._parent = parent

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        elif role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        if role == Qt.BackgroundRole:
            return QColor('transparent')
        if role == Qt.FontRole:
            return QtGui.QFont('Segoe UI', 9)
        if role == Qt.ToolTipRole:
            font = QtGui.QFontMetrics(QtGui.QFont('Segoe UI', 9))
            text_width = font.horizontalAdvance(self._data[index.row()][index.column()])
            column_width = self._parent.columnWidth(index.column()) - 9
            if text_width > column_width:
                return self._data[index.row()][index.column()]

    def headerData(self, section, orientation: Qt.Orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return None

    def rowCount(self, parent: QModelIndex = ...):
        return len(self._data)

    def columnCount(self, parent: QModelIndex = ...):
        return len(self._headers)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Main_Window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.CreateDBButton.clicked.connect(self.create_db)
        self.ui.Addbutton.clicked.connect(self.add_client)
        self.ui.EditButton.clicked.connect(self.edit_client)
        self.ui.SearchButton.clicked.connect(self.search_client)
        self.ui.DelButton.clicked.connect(self.del_client)
        try:
            self.db = DataBase()
        except:
            self.show_message('Ошибка в создании Базы Данных!')

    def update_table(self, data_select):
        data = []
        for client in data_select:
            client_data = []
            phone_list = []
            for data_list in client[0]:
                for item in data_list:
                    client_data.append(item)
            if client[1]:
                for phone in client[1]:
                    phone_list.append(phone[0])
            else:
                phone_list.append('')
            client_data.append(', '.join(phone_list))
            data.append(client_data)
        headers = ['id', 'Фамилия', 'Имя', 'Email', 'Номер телефона']
        self.model = TabelData(data, headers, self.ui.tableView)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.setColumnWidth(1, 120)
        self.ui.tableView.setColumnWidth(2, 100)
        self.ui.tableView.setColumnWidth(3, 170)
        self.ui.tableView.setColumnWidth(4, 179)

    def update_phone_table(self, client_id):
        phones_data = self.db.show_phone(client_id)
        phones_list = []
        if phones_data:
            for phone in phones_data:
                phones_list.append(list(phone))
        header = ['id', 'Phone number']
        self.phone_model = TabelData(phones_list, header, self.ui_edit_client.PhoneTable)
        self.ui_edit_client.PhoneTable.setModel(self.phone_model)
        self.ui_edit_client.PhoneTable.setColumnHidden(0, True)
        self.ui_edit_client.PhoneTable.setColumnWidth(1, 380)

    def close_window(self, parent, data):
        self.update_table(data)
        parent.close()

    def create_db(self):
        self.db.create_db()
        data = self.db.show_data()
        self.update_table(data)

    def add_client(self):
        self.add_client_window = QtWidgets.QWidget()
        self.ui_add_client = Add_client.Ui_Form()
        self.ui_add_client.setupUi(self.add_client_window)
        self.ui_add_client.PhoneFrame.setToolTip('Если у вас несколько номеров, то перечислите их через запятую')
        self.add_client_window.show()
        first_name = self.ui_add_client.NameEdit
        last_name = self.ui_add_client.LastNameEdit
        email = self.ui_add_client.EmailEdit
        phone = self.ui_add_client.PhoneEdit
        self.ui_add_client.AddClientBTN.clicked.connect(
            lambda: self.processing_add_client(first_name.text(), last_name.text(), email.text(), phone.text()))

    def processing_add_client(self, first_name, last_name, email, phone):
        phone_exists = False
        phone_list = []
        first = first_name.strip()
        last = last_name.strip()
        em = email.strip()
        ph = phone.strip()
        if ph:
            phone_list = ph.split(',')
            phone_exists = True
        if not first or not last or not em:
            self.show_message('Заполните поля: Фамилия, Имя, Email!')
        else:
            try:
                self.db.add_client(first, last, em, phone_list, phone_exists)
                self.close_window(self.add_client_window, self.db.show_data())
            except:
                self.show_message('Данный пользователь уже существует!')

    def save_changes_data(self, client_id):
        first_name = self.ui_edit_client.NameEdit.text()
        last_name = self.ui_edit_client.LastNameEdit.text()
        email = self.ui_edit_client.EmailEdit.text()
        self.db.edit_data_client(client_id, first_name, last_name, email)
        self.update_table(self.db.show_data())
        self.edit_client_window.close()

    def edit_client(self):
        try:
            row = self.ui.tableView.selectionModel().selectedRows()
            client_id = self.model.data(self.model.index(row[0].row(), 0))
            self.edit_client_window = QtWidgets.QWidget()
            self.ui_edit_client = Edit_window.Ui_Form()
            self.ui_edit_client.setupUi(self.edit_client_window)
            self.ui_edit_client.LastNameEdit.setText(self.model.data(self.model.index(row[0].row(), 1)))
            self.ui_edit_client.NameEdit.setText(self.model.data(self.model.index(row[0].row(), 2)))
            self.ui_edit_client.EmailEdit.setText(self.model.data(self.model.index(row[0].row(), 3)))
            self.update_phone_table(client_id)
            self.edit_client_window.show()
            self.ui_edit_client.AddPhoneBTN.clicked.connect(lambda: self.add_phone(client_id))
            self.ui_edit_client.EditPhoneBTN.clicked.connect(lambda: self.edit_phone(client_id))
            self.ui_edit_client.DelPhoneBTN.clicked.connect(lambda: self.del_phone(client_id))
            self.ui_edit_client.SaveChangesBTN.clicked.connect(lambda: self.save_changes_data(client_id))
        except:
            mes = 'Выделите необходимого клиента\nв таблице с данными!'
            self.show_message(mes)

    def _searching(self):
        client_ids = self.db.search_client(self.ui_search_client.NameEdit.text(),
                                           self.ui_search_client.LastNameEdit.text(),
                                           self.ui_search_client.EmailEdit.text(),
                                           self.ui_search_client.PhoneEdit.text())
        if client_ids:
            for row in range(self.model.rowCount()):
                if self.model.data(self.model.index(row, 0)) == str(client_ids[0][0]):
                    self.ui.tableView.selectRow(row)
            self.search_client_window.close()
        else:
            self.show_message('Клиент не найден!')

    def search_client(self):
        self.search_client_window = QtWidgets.QWidget()
        self.ui_search_client = Search_window.Ui_Form()
        self.ui_search_client.setupUi(self.search_client_window)
        self.search_client_window.show()
        self.ui_search_client.SearchBTN.clicked.connect(self._searching)

    def del_client(self):
        try:
            row = self.ui.tableView.selectionModel().selectedRows()
            client_id = self.model.data(self.model.index(row[0].row(), 0))
            self.db.delete_client(client_id)
            self.update_table(self.db.show_data())
            mes = 'Client Deleted'
            self.show_message(mes)
        except:
            mes = 'Выделите необходимого клиента\nв таблице с данными!'
            self.show_message(mes)

    def show_message(self, message):
        self.message_window = QtWidgets.QDialog()
        self.ui_message = Message_window.Ui_Dialog()
        self.ui_message.setupUi(self.message_window)
        self.ui_message.MainLabel.setText(message)
        self.message_window.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.message_window.show()
        self.ui_message.OkBTN.clicked.connect(self.message_window.close)

    def add_phone(self, client_id):
        self.add_phone_window = QtWidgets.QFrame()
        self.ui_add_phone = Add_phone.Ui_Frame()
        self.ui_add_phone.setupUi(self.add_phone_window)
        self.add_phone_window.show()
        self.ui_add_phone.SaveBTN.clicked.connect(
            lambda: (self.db.add_phone(client_id, self.ui_add_phone.PhoneEdit.text()),
                     self.update_phone_table(client_id),
                     self.add_phone_window.close()))

    def edit_phone(self, client_id):
        try:
            index = self.ui_edit_client.PhoneTable.selectionModel().selectedRows()[0].row()
            curr_phone = self.phone_model.data(self.model.index(index, 1))
            self.edit_phone_window = QtWidgets.QFrame()
            self.ui_edit_phone = Edit_phone.Ui_Frame()
            self.ui_edit_phone.setupUi(self.edit_phone_window)
            self.ui_edit_phone.PhoneEdit.setText(curr_phone)
            self.edit_phone_window.show()
            phone_id = self.phone_model.data(self.model.index(index, 0))
            self.ui_edit_phone.SaveBTN.clicked.connect(
                lambda: (self.db.edit_phone(phone_id, self.ui_edit_phone.PhoneEdit.text()),
                         self.update_phone_table(client_id),
                         self.edit_phone_window.close()))
        except:
            mes = 'Выделите в таблице необходимый\nномер телефона для его изменения!'
            self.show_message(mes)

    def del_phone(self, client_id):
        try:
            index = self.ui_edit_client.PhoneTable.selectionModel().selectedRows()[0].row()
            self.db.delete_phone(self.phone_model.data(self.model.index(index, 0)))
            self.update_phone_table(client_id)
            mes = 'Номер телефона успешно удален!'
            self.show_message(mes)
        except:
            mes = 'Выделите в таблице номер телефона\n для его последующего удаления!'
            self.show_message(mes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
