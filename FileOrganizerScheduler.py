import time

from FileOrg import FileOrg


class MyHandler():
    try:
        while True:
             fileorg = FileOrg()
             fileorg.move_files()
             time.sleep(7200) # run code every 2 hours
             print("1s")
    except KeyboardInterrupt:
        print("Exit")
     