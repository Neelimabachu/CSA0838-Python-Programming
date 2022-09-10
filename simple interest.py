#program to find simple interest

principle_amount=int(input("enter the principle amount="))
rate_of_interest=int(input("enter the rate of interest="))
time=int(input("enter the duration="))
simple_interest=(principle_amount*rate_of_interest*time)/100
print("the simple interest=",simple_interest)
