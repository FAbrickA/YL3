from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
import sqlite3
import sys


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_path = "coffee.sqlite"

        loadUi("main.ui", self)
        self.make_table()

    def make_table(self):
        db = sqlite3.connect(self.db_path)
        c = db.cursor()
        c.execute("SELECT * FROM coffee")
        print(c.description)
        self.table_widget.setColumnCount(len(c.description))
        self.table_widget.setHorizontalHeaderLabels(map(lambda x: x[0], c.description))
        arr = c.fetchall()
        db.close()
        self.table_widget.setRowCount(len(arr))
        for i, row in enumerate(arr):
            for j, col in enumerate(row):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(col)))


if __name__ == '__main__':
    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)

    sys.excepthook = except_hook
    app = QApplication(sys.argv)

    my_app = MyApp()
    my_app.show()

    sys.exit(app.exec_())
