#program to find greatest of three numbers

num1=int(input("enter first number="))
num2=int(input("enter second number="))
num3=int(input("enter the third number="))
if(num1>num2&num1>num3):
    print("greatest number is =",num1)
elif(num2>num3):
    print("greatest number is =",num2)
else:
    print("greatest number is=",num3)
