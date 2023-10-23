# DemoDict.py

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print(phone)
print(len(phone))
print(phone["kim"])
print("park" in phone)
print("kang" in phone)
print(type("kang" in phone))

#항상 객체의 참조가 전달된다.
p = phone
print(p)
print(phone)
print(id(phone), id(p))


p["kang"]="1234"
print(p)
print(phone)


#장비 관리
device = {"아이폰":5, "아이패드":10}
print(device)
#입력
device["맥북"]      = 15
print(device)
#수정
device["아이폰"]    = 6
print(device)
#삭제
del device["아이폰"]
print(device)

print("-----------------")
for item in device.items():
    print(item)

for item in device.keys():
    print(item)

for item in device.values():
    print(item)

print("-----------------")
print(bool(0))
print(bool(3))
print(bool(""))
print(bool("test"))
print(bool([]))
print(bool([1,2,3]))

print("-----------------")
print(1 < 2)
print(1 != 2)
print(1 == 2)
print(True and True and True)
print(True and True and False)
print(True or False or False)

print("-----------------")
print(5 / 2)
print(5 // 2) #정수 나눗셈 연산자 //
print(5 % 2)