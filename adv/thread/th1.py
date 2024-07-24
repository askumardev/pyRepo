import threading

def print_numbers():
  for i in range(10):
    print(i)

# Create a Thread object
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()

# python3 Basics/thread/th1.py