from PyQt5.QtWidgets import *
import sys
from main import f

class QLabelBuddy(QDialog) :
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Косоголова Наталия. Вариант 14')
        self.setFixedWidth(300)

        # Поле ввода Х
        self.xLineEdit = QLineEdit(self)
        self.xLabel = QLabel('&Введите "x"',self)
        self.xLabel.setBuddy(self.xLineEdit)

        self.yLabel = QLabel('y = ',self)

        # Кнопки
        btnOK = QPushButton('&Вычислить')
        btnOK.clicked.connect(self.get_y)
        btnCancel = QPushButton('&Очистить')
        btnCancel.clicked.connect(self.clear)

        # Размещение элементов
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(self.xLabel,0,0)
        mainLayout.addWidget(self.xLineEdit,0,1,1,2)
        mainLayout.addWidget(self.yLabel,1,0)
        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)

    # Обработчик кнопки "Очистить"
    def clear(self):
        self.xLineEdit.setText(str(''))
        self.yLabel.setText('y = ')

    # Обработка кнопки "Вычислить"
    def get_y(self):
        x = self.xLineEdit.text()
        if x != "":
            self.yLabel.setText('y = ' + str(f(x)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())