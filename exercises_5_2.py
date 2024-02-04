operator=input("Enter(+,-,*,/):")
num_1=int(input("Enter number one "))
num_2=int(input("Enter number two"))
result= 0
if operator=="+":
 result=(num_1+num_2)
elif operator==("-"):
 result=(num_1-num_2)
elif operator=="*":
 result=(num_1*num_2)
elif operator=="/":
    result=(num_1/num_2)
    print(result)
while True:
    word = input("Enter do you want continue?:")
    if word == "yes":
      print(input("Enter(+,-,*,/):"))
    if word != "yes":
        break
        print("end")





