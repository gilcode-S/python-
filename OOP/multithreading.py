

import threading
import time


def walk(first):
    time.sleep(8)
    print(f"You finish walking the {first}")


def trash():
    time.sleep(3)
    print("You take out the trash")


def mail():
    time.sleep(4)
    print("You get the mail in the mailbox")


chore1 = threading.Thread(target=walk, args=("black",))
chore1.start()


chore2 = threading.Thread(target=trash)
chore2.start()

chore3 = threading.Thread(target=mail)
chore3.start()


chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")
