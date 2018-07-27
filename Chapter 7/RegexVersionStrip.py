import re
def regexVersionStrip (text, word=None):
    if word == None:
        removeSpaces = re.compile(r'(\w+\s\w+(\s\w+){0,})')
        return(removeSpaces.search(text).group())
    else:
        removeWord = re.compile(r'[^'+word+']+')
        return(removeWord.search(text).group())

text = '                 Hello World            '
print(regexVersionStrip(text))

text2 = '***************Hello World***********'
print(regexVersionStrip(text2, '*'))
