import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


class Navigator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.level = 1
        self.setGeometry(100, 100, 1200, 900)
        self.setWindowTitle('Навигатор')
        self.btn_1level = QPushButton('1 ЭТАЖ', self)
        self.btn_2level = QPushButton('2 ЭТАЖ', self)
        self.btn_3level = QPushButton('3 ЭТАЖ', self)
        self.btn_4level = QPushButton('4 ЭТАЖ', self)
        i = 0
        self.level_btns = [self.btn_1level, self.btn_2level, self.btn_3level, self.btn_4level]
        for btn in self.level_btns:
            btn.resize(btn.sizeHint())
            btn.clicked.connect(self.change_level)
            btn.move(i, 0)
            i += 100
        self.pixmap1 = QPixmap('img/1.jpg')
        self.image1 = QLabel(self)
        self.image1.move(80, 60)
        self.image1.resize(self.pixmap1.width(), self.pixmap1.height())
        self.image1.setPixmap(self.pixmap1)

        self.pixmap2 = QPixmap('img/2.jpg')
        self.image2 = QLabel(self)
        self.image2.move(80, 60)
        self.image2.resize(self.pixmap2.width(), self.pixmap2.height())
        self.image2.setPixmap(self.pixmap2)

        self.pixmap3 = QPixmap('img/3.jpg')
        self.image3 = QLabel(self)
        self.image3.move(80, 60)
        self.image3.resize(self.pixmap3.width(), self.pixmap3.height())
        self.image3.setPixmap(self.pixmap3)

        self.pixmap4 = QPixmap('img/4.jpg')
        self.image4 = QLabel(self)
        self.image4.move(80, 60)
        self.image4.resize(self.pixmap4.width(), self.pixmap4.height())
        self.image4.setPixmap(self.pixmap4)

        self.la = QLabel('Откуда: ', self)
        self.la.move(600, 10)

        self.a = QLineEdit(self)
        self.a.move(650, 10)
        self.a.resize(100, 20)

        self.lb = QLabel('Куда: ', self)
        self.lb.move(800, 10)

        self.b = QLineEdit(self)
        self.b.move(835, 10)
        self.b.resize(100, 20)

        self.route_create_btn = QPushButton('Построить маршрут', self)
        self.route_create_btn.move(1000, 5)

        # self.a = QLineEdit(self)
        # self.a.resize(100, 50)
        # self.a.move(0,0)

    def change_level(self):
        self.image1.setVisible(False)
        self.image2.setVisible(False)
        self.image3.setVisible(False)
        self.image4.setVisible(False)
        level = self.sender().text()
        ## Изображение
        if level == '1 ЭТАЖ':
            self.level = 1
            self.image1.setVisible(True)
        if level == '2 ЭТАЖ':
            self.level = 2
            self.image2.setVisible(True)
        if level == '3 ЭТАЖ':
            self.image3.setVisible(True)
            self.level = 3
            print(self.level)
        if level == '4 ЭТАЖ':
            self.image4.setVisible(True)
            self.level = 4
            print(self.level)

        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр 
    # нашего виджета класса Example
    ex = Navigator()
    ex.show()
    # Будем ждать, пока пользователь не завершил исполнение QApplication, 
    # а потом завершим и нашу программу
    sys.exit(app.exec())
