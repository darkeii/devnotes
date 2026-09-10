# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                   Good for I/O bound tasks like reading files or fetching data from APIs
#                   threading.Thread(target-my_function)
#

import threading
import time
from threading import Thread


def walk(name):
    time.sleep(8)
    print(f"You finish walking {name}")

def trash():
    time.sleep(2)
    print("You take out the trash")

def get_mails():
    time.sleep(4)
    print("You get the mails")

chore1 = threading.Thread(target=walk, args=("Scooby",))            # that comma is needed when only passing single argument, or it iterates each character of the string and takes them as an argument given.
chore1.start()

chore2 = threading.Thread(target=trash)
chore2.start()

chore3 = threading.Thread(target=get_mails)
chore3.start()

