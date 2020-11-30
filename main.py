from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QMessageBox
from UI.main import Ui_MainWindow
from UI.addEditCoffeeForm import Ui_Dialog
import sqlite3
import sys


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.db_path = "coffee.sqlite"
        self.active_row = None

        self.setupUi(self)

        self.setup_logic()

    def setup_logic(self):
        self.make_table()
        self.button_add.clicked.connect(self.button_add_handler)
        self.button_change.clicked.connect(self.button_change_handler)
        self.table_widget.cellClicked.connect(self.table_widget_handler)

    def table_widget_handler(self, row, col):
        self.active_row = row

    def button_add_handler(self):
        dialog = MyDialog(title="Добавить запись")
        dialog.exec_()
        if dialog.result == dialog.OK:
            data = dialog.get_data()
            db = sqlite3.connect(self.db_path)
            c = db.cursor()
            c.execute(f"""
                INSERT INTO "coffee" (sort_name, roast, ground, description, price, size)
                VALUES ({", ".join(["?" for _ in range(len(data))])})
            """, data)
            db.commit()
            db.close()
            self.make_table()

    def button_change_handler(self):
        if self.active_row is None:
            message_box = QMessageBox()
            message_box.setText("Ошибка\n\nВыберите ряд для редактирования\t")
            message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            message_box.setDefaultButton(QMessageBox.Save)
            message_box.exec_()
            return
        rowid = self.table_widget.item(self.active_row, 0).text()
        db = sqlite3.connect(self.db_path)
        c = db.cursor()
        c.execute(f"SELECT * FROM coffee WHERE id = {rowid}")
        props = c.fetchone()[1:]
        db.close()
        dialog = MyDialog(title="Редактировать запись", props=props)
        dialog.exec_()
        if dialog.result == dialog.OK:
            data = dialog.get_data()
            db = sqlite3.connect(self.db_path)
            c = db.cursor()
            c.execute(f"""
                UPDATE coffee
                SET sort_name = ?, roast = ?, ground = ?,
                description = ?, price = ?, size = ?
                WHERE id = {rowid}
            """, data)
            db.commit()
            db.close()
            self.make_table()

    def make_table(self):
        db = sqlite3.connect(self.db_path)
        c = db.cursor()
        c.execute("SELECT * FROM coffee")
        self.table_widget.setColumnCount(len(c.description))
        self.table_widget.setHorizontalHeaderLabels(map(lambda x: x[0], c.description))
        arr = c.fetchall()
        db.close()
        self.table_widget.setRowCount(len(arr))
        for i, row in enumerate(arr):
            for j, col in enumerate(row):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(col)))


class MyDialog(QDialog, Ui_Dialog):
    OK = 0
    BAD = 1

    def __init__(self, title="", props=None):
        super().__init__()
        self.title = title
        self.props = props
        self.result = self.BAD
        self.data = None

        self.setupUi(self)
        self.label_title.setText(self.title)
        self.setWindowTitle(self.title)
        if props is not None:
            self.line_edit_sort.setText(props[0])
            self.line_edit_roast.setText(props[1])
            self.checkbox_ground.setChecked(bool(props[2]))
            self.text_edit_description.setText(props[3]),
            self.spin_price.setValue(props[4]),
            self.spin_size.setValue(props[5])

        self.setup_logic()

    def setup_logic(self):
        self.button_ok.clicked.connect(self.button_ok_handler)
        self.button_cancel.clicked.connect(self.button_cancel_handler)

    def button_ok_handler(self):
        self.result = self.OK
        self.data = (
            self.line_edit_sort.text(),
            self.line_edit_roast.text(),
            1 if self.checkbox_ground.isChecked() else 0,
            self.text_edit_description.toPlainText(),
            self.spin_price.value(),
            self.spin_size.value()
        )
        self.accept()

    def get_data(self):
        return self.data

    def button_cancel_handler(self):
        self.result = self.BAD
        self.accept()


if __name__ == '__main__':
    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)

    sys.excepthook = except_hook
    app = QApplication(sys.argv)

    my_app = MyApp()
    my_app.show()

    sys.exit(app.exec_())
