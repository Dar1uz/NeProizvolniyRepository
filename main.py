import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        with sqlite3.connect("coffee.sqlite") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM coffee")
            coffees = cursor.fetchall()

            for i in range(len(coffees)):
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                id = QTableWidgetItem(str(coffees[i][0]))
                name = QTableWidgetItem(coffees[i][1])
                stage = QTableWidgetItem((coffees[i][2]))
                type = QTableWidgetItem(coffees[i][3])
                description = QTableWidgetItem(coffees[i][4])
                prices = QTableWidgetItem(str(coffees[i][5]))
                volume = QTableWidgetItem(str(coffees[i][6]))
                self.tableWidget.setItem(rowPosition, 0, id)
                self.tableWidget.setItem(rowPosition, 1, name)
                self.tableWidget.setItem(rowPosition, 2, stage)
                self.tableWidget.setItem(rowPosition, 3, type)
                self.tableWidget.setItem(rowPosition, 4, description)
                self.tableWidget.setItem(rowPosition, 5, prices)
                self.tableWidget.setItem(rowPosition, 6, volume)
            cursor.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())