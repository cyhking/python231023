# -*- 생성자와 소멸자 -*-
class MyClass:
    #생성자(초기화메서드)
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    #소멸자(청소, 정리하는 작업)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성
m = MyClass(5)
#del m

print("전체 코드 실행 종료")