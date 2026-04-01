import time
from plyer import notification
from datetime import datetime

# tested on Windows 11. WSL2 does not support notifications.
while True:
  print("Please flex your muscles and take a break!")
  notification.notify(
    title = "Time to take a break!",
    message = "Please flex your muscles and take a break!")
  time.sleep(60) # Sleep for 1 hour (3600 seconds)



# python3 projs/notifications.py