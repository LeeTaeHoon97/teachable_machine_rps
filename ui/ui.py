from cProfile import label
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import cv2
import sys

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

import threading
import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("ui/untitle.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        running = False

        self.btn.clicked.connect(self.loadImageFromFile)
        self.start()
        
    
    def run(self):
        global running
        cap = cv2.VideoCapture(-1)
        print("cam : ",cap)
        width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.cam.resize(width,height)

        while running:
            ret, img=cap.read()
            if ret:
                img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                h,w,c=img.shape
                qImg=QtGui.QImage(img.data,w,h,w*c,QtGui.QImage.Format_RGB888)
                pixmap=QtGui.QPixmap.fromImage(qImg)
                self.cam.setPixmap(pixmap)
            # else:
            #     QtWidgets.QMessageBox.about(win,"Error","Cannot read frame.")
            #     print("cannot read frame.")
            #     break
        cap.release()

    def start(self):
        global running

        running = True

        th = threading.Thread(target=self.run)

        th.start()
        print("started..")


    def loadImageFromFile(self) :
        #QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시
        rps_lst= ['R','P','S']
        index= random.randint(0,2)
        self.qPixmapFileVar = QtGui.QPixmap()
        self.qPixmapFileVar.load(f"imgs\{rps_lst[index]}.jpg")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(224)
        self.center.setPixmap(self.qPixmapFileVar)

   



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    