#! python3
# fillingGaps.py -  finds all files with a given prefix, such as spam001.txt, 
# spam002.txt, and so on, in a single folder and locates any gaps in the numbering and
# have the program rename all the later files to close this gap.

import os, shutil, re

pattern = re.compile(r'(spam)(\d+)(.txt)')
path = 'C:\\Users\\Marcus Vinícius\\Documents\\Automate the Boring Stuff\\Automate_Boring_Stuff\\Chapter 9\\Practice Projects\\Filling in the Gaps\\Spamtxt'

number = 1
for files in os.listdir(path):
    print(files)
    check = pattern.search(files)
    if check == None:
        print('exiting on pattern match')
        continue
    spamPart = check.group(1)
    digitPart = check.group(2)
    extPart = check.group(3)
    if digitPart == number:
        print('Exiting on sequential number')
        number += 1
        continue
    digitPart = str(number)
    newName = spamPart + digitPart + extPart
    absFileDir = os.path.join(path, files)
    absNewDir = os.path.join(path, newName)
    print('Renaming "%s" to "%s".' % (str(files), str(newName)))
    shutil.move(absFileDir, absNewDir)
    number += 1
