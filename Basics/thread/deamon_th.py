import threading
import time

def background_task():
  while True:
    print("Running in the background")
    time.sleep(1)

# Create a daemon thread
thread = threading.Thread(target=background_task)
thread.daemon = True
thread.start()

# Main program will exit after 3 seconds
time.sleep(3)
print("Main program exits")

# python3 Basics/thread/deamon_th.py