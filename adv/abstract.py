# python3 Basics/abstract.py

from abc import ABC, abstractmethod 

class Computer:
  @abstractmethod
  def process(self):
    pass

class Laptop(Computer):
  def process(self):
    print("Running")

class Programmer:
  def work(self,com1):
    com1.process()
    print("solving")

com = Computer()
com.process()
com1 = Laptop()
com1.process()
p1 = Programmer()
p1.work(com1)