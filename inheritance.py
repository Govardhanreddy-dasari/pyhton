'''class parent():
    def output(self):
        print("This is parent class output method")
class child(parent):
    def outputc(self):
        print("This is child class output method")
c=child()
c.outputc()
c.output()'''
class grandfather():
    def outputgf(self):
        print("This is grandfather class output method")
class parent2(grandfather):
    def outputp(self):
        print("This is parent class output method")
class child2(parent2):
    def outputc2(self):
        print("This is child class output method")
c2=child2()
c2.outputc2()
c2.outputp()
c2.outputgf()