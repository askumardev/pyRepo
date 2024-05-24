import threading

class MyThread(threading.Thread):
  def run(self):
    for i in range(10):
      print(i)

# Create and start the thread
thread = MyThread()
thread.start()
thread.join()

# python3 Basics/thread/th_subclassing.py