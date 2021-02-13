from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel
import sys
from PyQt5.QtGui import QPixmap,QIcon

class ImageGallary(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Open File"
        self.top = 200
        self.left = 700
        self.width = 400
        self.height = 600
        self.current=0
        self.fname=''
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QIcon("icon.ico"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        self.btn1 = QPushButton("Open Image")
        self.btn2 = QPushButton("Next")
        self.btn3 = QPushButton("Prev")
        self.label = QLabel("Image will show here")
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.label)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)

        self.btn1.clicked.connect(self.getImage)
        self.btn2.clicked.connect(self.nextImage)
        self.btn3.clicked.connect(self.prevImage)

        self.setLayout(vbox)
        self.show()

    def getImage(self):
        import os
        desktop=os.getlogin()
        # imagePath=""
        self.fname = QFileDialog.getOpenFileNames(self, 'Open file',os.getcwd(), "Image files (*.jpg *.gif *.jpeg)")
        try: 
            imagePath=self.fname[0][0]
            print("first image Path  = {}".format(imagePath))
            print("list of image fname = {}".format(self.fname))
            print("type imagePath{}".format(type(imagePath)))
            print("type fname {}".format(type(self.fname)))
            pixmap = QPixmap(imagePath)
            self.label.setPixmap(QPixmap(pixmap))
            self.resize(pixmap.width(), pixmap.height())
        except IndexError as e:
            print(e)

    def nextImage(self):
        try:
            # print(self.fname)
            if self.current >= len(self.fname[0]) - 1 :
                print('End of Next')
            else:
                self.current+=1
                imagePath = self.fname[0][self.current]
                pixmap = QPixmap(imagePath)
                self.label.setPixmap(QPixmap(pixmap))
                self.resize(pixmap.width(), pixmap.height())
                print(self.fname[0][self.current])
        except IndexError as e:
            print(e)

    def prevImage(self):
        if self.current > 0 :
            self.current -= 1 
            imagePath = self.fname[0][self.current]
            pixmap = QPixmap(imagePath)
            self.label.setPixmap(QPixmap(pixmap))
            self.resize(pixmap.width(), pixmap.height())
            print(self.fname[0][self.current])
        else:
            print('End of Prev  ')
        
App = QApplication(sys.argv)
window = ImageGallary()
sys.exit(App.exec())