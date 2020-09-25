import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QLabel, QPushButton, QRadioButton, QDialog, QVBoxLayout
from PyQt5 import uic


class MainForm(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('color.ui', self)
        self.Button_main.clicked.connect(self.print_colors)

    def print_colors(self):
        self.line = ''
        for j in [self.verticalLayout, self.verticalLayout_2, self.verticalLayout_3]:
            for i in [j.itemAt(i).widget() for i in range(3)]:
                if i.isChecked():
                    self.line += i.text() + ' '
        self.label_answer.setText('Цвета: ' + self.line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())
