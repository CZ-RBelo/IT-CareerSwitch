# Working with Files (shutil - os)

print("\n-> Working with Files - shutil.copy")

import shutil

src_folder="c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/"
dst_folder="c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/"

src_file="Module15.txt"
dst_file="Module15-copy.txt"

shutil.copy(src_folder+src_file, dst_folder+dst_file)


print("\n-> Working with Files - os.rename")

import os

src="c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/Module15-copy.txt"
dst="c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/Module16.txt"

os.rename(src, dst)


print("\n-> Working with Files - os.remove")

import os

dst="c:/Users/jrbel/Workspace/IT-CareerSwitch/Courses/Python/Module16.txt"

os.remove(dst)