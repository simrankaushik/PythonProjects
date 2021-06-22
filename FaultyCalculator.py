# Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

num1=float(input("Enter the 1st number: "))
num2=float(input("Enter the 2nd number: "))
print("OPERATIONS= +, -, *, /")
op=input("Which operation would you like to perform: ")

if op=="+" and num1==56 and num2==9:
    print("77")
elif op=="*" and num1==45 and num2==3:
    print("555")
elif op=="/" and num1==56 and num2==6:
    print("4")
elif op=="+":
    plus=num1+num2
    print(plus)
elif op=="-":
    sub=num2-num1
    print(sub)
elif op=="*":
    pro=num1*num2
    print(pro)
elif op=="/":
    div=num1/num2
    print(div)

else:
    print("Plz check your inputs")

