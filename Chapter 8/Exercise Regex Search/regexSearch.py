#!python3
# regexSearch.py - program that opens all .txt files in a folder and 
# searches for any line that matches a user-supplied regular expression.

import re, os
print('Please enter the expressions to be searched:')
textSearch = str(input())

for file in os.listdir('.'):
    if file.endswith(".txt"):
        
        fileOpen = open(file)
        box = re.compile('.*' + (textSearch) + '.*')
        print(box.findall(fileOpen.readline()))
        fileOpen.close()