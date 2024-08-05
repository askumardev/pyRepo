# python3 adv/ducktyping.py

class Car:
  def drive(self):
    print("Driving Car...")


class MotorCycle:
  def drive(self):
    print("Driving MotorCycle...")


def test_drive(item):
  item.drive()  # don't care what it is, all i care is that it can "drive"


test_drive(Car())  #=> "Driving Car..."
test_drive(MotorCycle())  # "Driving MotorCycle..."