# Displaying Daytime Working Directory and File Metadata

from datetime import date
from datetime import time
from datetime import datetime

import os

print("\n### Displaying Daytime ###")

print("\n-> Finding the today's date")

today = date.today()
date_time = datetime.now()

print("\nToday's date is: ", today)
print("\nAll together now: ", date_time)


print("\n\n### Displaying Working Directory ###")

dirpath = os.getcwd()
print("\nYour current directory is: " + dirpath)

foldername = os.path.basename(dirpath)
print("\nThe directory name is: " + foldername)

print("\n\n### Displaying File Metadata ###")

# The os module offers the os.stat() function wich we will use: os.stat("file here")

# st_mode - protection bits
# st_ino - inode number
# st_dev - devide
# st_nlink - number of hardlinks
# st_uid - user id of owner
# st_gid - group id ofowner
# st_size - size of file, in bytes
# st_atime - time of most recent acess
# st_mtime - time of most recent content modification
# st_ctime - time of most recent metada change

print("\n")
print(os.stat("c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/Module24.py"))
print("\n")