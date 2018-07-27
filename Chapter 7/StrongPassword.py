import re

def strongPassword(text):
    digit = re.compile(r'(\d)')
    upperCase = re.compile(r'([A-Z])')
    lowerCase = re.compile(r'([a-z])')

    if len(text) < 8:
        return('The password must have at least eight characters.')
    if lowerCase.findall(text) == []:
        return('The password must have at least one lowercase letter.')
    if upperCase.findall(text) == []:
        return('The password must have at least one uppercase letter.')
    if digit.findall(text) == []:
        return('The password must have at least one digit.')
    else:
        return('Your password is strong!')

print(strongPassword('M4rt1n15'))
print(strongPassword('martin15'))
print(strongPassword('Martinin'))
print(strongPassword('MARTIN15'))
print(strongPassword('martin'))