#program to find factorial of anumber

number=int(input("enter a number="))
fact=1
while(number>0):
    fact=fact*number
    number=number-1
print("factorial of the number =",fact)
