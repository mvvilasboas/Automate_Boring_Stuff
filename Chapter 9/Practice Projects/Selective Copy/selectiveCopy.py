#! python3
# selectiveCopy.py - walks through a folder tree and searches for files with a certain file extension, 
# copy these files from whatever location they are in to a new folder.

import os
import shutil

def selectiveCopy(folder):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.txt'):
                shutil.copy(os.path.join(foldername, filename), 'C:\\Users\\Marcus Vinícius\\Documents\\Automate the Boring Stuff\\Automate_Boring_Stuff\\Chapter 9\\Practice Projects\\Selective Copy\\copyTo') #Commented out to protect against accidental copying
                print('Copying ' + filename + '...') #Print only to verify working correctly

selectiveCopy(r'C:\\Users\\Marcus Vinícius\\Documents\\Automate the Boring Stuff\\Automate_Boring_Stuff\\Chapter 9\\Practice Projects\\Selective Copy\\copyFrom')