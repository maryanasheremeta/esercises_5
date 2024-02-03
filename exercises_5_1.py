the_text= input("Enter String:")

kwlist = {*'''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~'''}
ban = __import__('keyword').iskeyword
is_valid = True
if not the_text[0].isnumeric() and not ban(the_text):
    for sym in the_text:
        if sym.isupper() or sym in kwlist:
            is_valid = False
            break
else:
    is_valid = False
print(is_valid)

import keyword
name=input("Enter variables :")
if name.isidentifier()and name [0]!="_"and name.count("_")<=1 and name not in keyword.kwlist:
    print(True)
else:
    print(False)

