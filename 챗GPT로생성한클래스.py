class Person:
    def __init__(self, id, phoneNumber):
        self.id = id  # 사람의 ID
        self.phoneNumber = phoneNumber  # 사람의 전화번호

    def printInfo(self):
        print(f"ID: {self.id}, 전화번호: {self.phoneNumber}")

class Manager(Person):
    def __init__(self, id, phoneNumber, skill):
        super().__init__(id, phoneNumber)
        self.skill = skill  # 관리자의 기술 스킬

    def printInfo(self):
        super().printInfo()
        print(f"기술: {self.skill}")

class Employee(Person):
    def __init__(self, id, phoneNumber, title):
        super().__init__(id, phoneNumber)
        self.title = title  # 직원의 직급

    def printInfo(self):
        super().printInfo()
        print(f"직급: {self.title}")

# 예제 사용:
person1 = Person("12345", "555-555-5555")
person1.printInfo()

manager1 = Manager("67890", "666-666-6666", "리더십")
manager1.printInfo()

employee1 = Employee("24680", "777-777-7777", "소프트웨어 엔지니어")
employee1.printInfo()
