#program to find leap year


year=int(input("enter a year "))
mod=year%4
if(year>0):
    if(year%4==0 and year%400==0 and year%100!=0):
         print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
        print("previous leap year is = ",year-(4-mod))
else:
    print("invalid input")
