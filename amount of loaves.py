#program to calculate amount for loaves

fresh=float(input("enter the number of fresh loaves purchased = "))
old=float(input( "enter the number of old loaves purchased =  "))
if fresh>=0 and old>=0:
    print("amout of news loaves  = "  ,185*fresh )
    print("amout of old loaves = ",74*old)
    print("Total amount = ", 185*fresh +74*old)
else:
    print("enter valid input")
