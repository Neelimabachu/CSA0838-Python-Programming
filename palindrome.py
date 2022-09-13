#program to check palindrome

def ispalindrome(s) :
    rev =''.join(reversed(s))
    if (s==rev):
        return True
    return False
s=input("enter the word")
ans= ispalindrome(s)
if(ans):
    print("yes,it is a palindrome")
else:
    print("no,it is not a palindrome")
