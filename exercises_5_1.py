the_text= input("Enter String:")
kw_list = {*'''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~'''}
kw_list_1 = __import__('keyword').iskeyword
is_valid = True
if not the_text[0].isnumeric() and not kw_list_1(the_text):
    for sym in the_text:
     if sym.isupper() or sym in kw_list:
            is_valid = False
            break
else:
    is_valid = False
print(is_valid)




