#!python3
# madLibs.py - Creates a .txt file and substitute the keywords from input text.

import re

# Entering the name of the file.
print('Please enter the name of the file you want to create:')
nameFile = str(input())

# Entering the text.
print('''Welcome to the Mad Libs!
Please enter the text you want to substitute.
Remember that it must have at least one of the words ADJECTIVE, NOUN, ADVERB and VERB.
(It must be uppercased)
''')
textFile = str(input())

wordsSub = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
searchWordsSub = wordsSub.search(textFile)
if searchWordsSub == None:
    print('Not found any ADJECTIVE, NOUN, ADVERB or VERB words in your text.')
if re.compile(r'ADJECTIVE').search(textFile) != None:
    print('Enter an adjective:')
    adjWord = str(input())
    textFile = re.compile(r'ADJECTIVE').sub(adjWord, textFile)
if re.compile(r'NOUN').search(textFile) != None:
    print('Enter a noun:')
    nounWord = str(input())
    textFile = re.compile(r'NOUN').sub(nounWord, textFile)
if re.compile(r'ADVERB').search(textFile) != None:
    print('Enter an adverb:')
    advWord = str(input())
    textFile = re.compile(r'ADVERB').sub(advWord, textFile)
if re.compile(r'VERB').search(textFile) != None:
    print('Enter a verb:')
    verbWord = str(input())
    textFile = re.compile(r'VERB').sub(verbWord, textFile)
print(textFile)

txtFile = open(nameFile+'.txt', 'w')
txtFile.write(textFile)
txtFile.close()