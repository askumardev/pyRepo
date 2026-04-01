# import time
# from plyer import notification
# from datetime import datetime


# while True:
#   print("Please flex your muscles and take a break!")
#   notification.notify(
#     title = "Time to take a break!",
#     message = "Please flex your muscles and take a break!")
#   time.sleep(3600) # Sleep for 1 hour (3600 seconds)


import time
import subprocess
from datetime import datetime


def send_notification(title, message):
    try:
        subprocess.run(["notify-send", title, message], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass  # silently skip if no display available

while True:
    now = datetime.now().strftime("%H:%M")
    message = "Please flex your muscles and take a break!"
    
    print(f"[{now}] {message}")
    send_notification("Time to take a break!", message)
    time.sleep(3600)
# python3 projs/notifications.py