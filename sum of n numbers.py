#program to find sum of n numbers

n=int(input("enter the no.of numbers to be added="))
sum=0

while(n>0):
    sum=sum+n
    n=n-1
print("sum of the numbers is =",sum)
