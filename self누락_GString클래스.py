#전역변수
str = "Not Class Member"
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #self 누락
        print(self.str)

g = GString()
g.set("First Message")
g.print()
