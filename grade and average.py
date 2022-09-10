#program to find garde and average

mark1=int(input("enter maths marks out of 100="))
mark2=int(input("enter python marks out of 100="))
mark3=int(input("enter physics marks out of 100="))
average=(mark1+mark2+mark3)/3
if(average>90):
    grade='S'
elif(average<90&average>80):
    grade='A'
elif(average<80&average>70):
    grade='B'
elif(average<70&average>60):
    grade='C'
elif(average<60&average>50):
    grade='D'
else:
    grade='fail'
print("grade=",grade)
print("average=",average)
