# python3 adv/files/delete_file.py

import os
if os.path.exists("demofile1.txt"):
  os.remove("demofile1.txt")
else:
  print("The file does not exist")