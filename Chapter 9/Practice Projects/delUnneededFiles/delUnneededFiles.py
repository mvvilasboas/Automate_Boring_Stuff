#! python3
# delUnneededFile.py - walks through a folder tree and searches for exceptionally large
# files or folders (size of more than 100MB).

import os
def delUnneededFile(folder):
    for folderName, subFolders, filenames in os.walk(folder):
        if os.path.getsize(folderName) > 100000:
            print('The folder ' + folderName + ' has the size: ' + str(os.path.getsize(folderName)) + '. And you can find it going to ' + str(os.path.abspath(folderName)))
        for filename in filenames:
            if os.path.getsize(os.path.join(folderName, filename)) > 100000:
                print('The file '+ filename + ' has the size: ' + str(os.path.getsize(os.path.join(folderName, filename))) + '. And you can find it going to ' + str(os.path.abspath(filename)))

delUnneededFile('C:\\Users\\Marcus Vinícius\\Downloads')