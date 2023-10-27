# DemoForm3.ui(화면) + DemoForm3.py(로직)


import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 
#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup

#ui 포함해서 빌드하기 위한 구문 시작 ---->
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path("DemoForm3.ui")
#디자인 파일 로딩(파일명 변경)
form_class = uic.loadUiType(form)[0]
#<----- ui 포함해서 빌드하기 위한 구문 끝(resource_path함수를 써서 form 변수로 넘겨야함)

#폼 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #슬롯 메서드
    def firstClick(self):
        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        f = open("c:\\work\\dangn.txt", "wt", encoding="utf-8")
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        for post in posts:
            title   = post.find("h2", attrs={"class":"card-title"})
            price   = post.find("div", attrs={"class":"card-price"})
            addr    = post.find("div", attrs={"class":"card-region-name"})
            title   = title.text.strip().replace("\n","")
            price   = price.text.strip().replace("\n","")
            addr    = addr.text.strip().replace("\n","")
            print(f"{title}, {price}, {addr}")
            f.write(f"{title}, {price}, {addr}\n")
        f.close()
        self.label.setText("당근 크롤링 완료!")
    def secondClick(self):
        self.label.setText("두번째 버튼")
    def thirdClick(self):
        self.label.setText("세번째 버튼")
        

#직접 실행했는지 여부(진입점체크)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()