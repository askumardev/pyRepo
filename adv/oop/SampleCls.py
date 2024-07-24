# python3 Basics/ObjCls/SampleCls.py

class Computer:

  def config(self):
    print("Hello Computer")

com = Computer()
print(type(com))

com.config()
# Computer.config() #TypeError: config() missing 1 required positional argument: 'self'
Computer.config(com)