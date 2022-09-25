# python3 Basics/ObjCls/SampleCls2.py

class Computer:

  def __init__(self,cpu,ram):
    self.cpu = cpu
    self.ram = ram

  def config(self):
    print("Hello Computer",self.cpu,self.ram)

com1 = Computer("i5",16)
com2 = Computer("intel",8)

com1.config() #
com2.config()
