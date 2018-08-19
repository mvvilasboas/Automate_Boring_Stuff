#! python3
# selectiveCopy.py - walks through a folder tree and searches for files with a certain file extension, 
# copy these files from whatever location they are in to a new folder.

import shutil, os

def selectiveCopy(rootFolder, ext, newfolder):
    # Transforming Parameters into variables
    rootFolder = rootFolder
    ext = ext

    # Checking if the new folder don't already exists.
    newFolderName = newfolder
    number = 1
    if not os.path.exists(newFolderName):
        os.makedirs(newFolderName)
        newFolder = os.path.abspath(newFolderName) 
    else:
        while True:
            if not os.path.exists(newFolderName + '_' + str(number)):
                os.makedirs(newFolderName+'_'+str(number))
                newFolder = os.path.abspath(newFolderName+'_'+str(number))
                break
            number = number + 1

    # Finding the files with the ext.
    for foldername, subfolders, filenames in os.walk(rootFolder):
        print('Searching for files in %s...' %(foldername))
        for filename in filenames:
            if not filename.endswith('.'+ext):
                continue
            filename = os.path.join(os.path.abspath(filename),filename)
            shutil.copy(str(filename), str(newFolder))
            #print('Copying the file %s' %(filename))
    print('Done.')

selectiveCopy('/home/vilasboasmv/Automate_Boring_Stuff/automate_online-materials', 'txt', 'test')    