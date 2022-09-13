#program to count no of words in a sentence


def countstrings(n, start):
    while(n>0):
        if n == 0:
            return 1
        cnt = 0
        for i in range(start, 5):
            cnt += countstrings(n - 1, i)
        return cnt
     
def countVowelStrings(n):
    return countstrings(n, 0)
 
n = int(input("enter a number = "))
print(countVowelStrings(n))
