#program to find maximum ways to climb staircase


def stair(n):
    if n <= 1:
        return n
    else:
        return stair(n-1) + stair(n-2)
s=int(input("enter no of steps to be climbed each time ="))
print(stair(s+1))
