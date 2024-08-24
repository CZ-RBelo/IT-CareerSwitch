# Working with Files (shutil - os)

print("\n-> Reading Files - shutil.copy")

import shutil

src="c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/Module15.txt"
dst="c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/Module15-copy.txt"

shutil.copy(src, dst)

print("\n-> Reading Files - os.rename")

import os

src="c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/Module15-copy.txt"
dst="c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/Module16.txt"

os.rename(src, dst)


print("\n-> Reading Files - os.remove")

import os

dst="c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/Module16.txt"

os.remove(dst)