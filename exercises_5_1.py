import keyword
name=input("Enter variables :")
if name.isidentifier()and name [0]!="_"and name.count("_")<=1 and name not in keyword.kwlist:
    print(True)
else:
    print(False)

