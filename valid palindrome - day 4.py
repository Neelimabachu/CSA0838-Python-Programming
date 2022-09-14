#program to check valid palindrome 




class Solution:
   def isPalindrome(self, string: str):
       
       sequence=""
       for i in string:
           if i.isalpha():
               sequence+=i
           elif i.isdigit():
               sequence+=i
       sequence=sequence.lower()
       for i in range(len(sequence)//2):
           if sequence[i] != sequence[len(sequence)-1-i]:
               return False
       return True
  
if __name__ == '__main__':
   string = 'Was it a car or a cat I saw!!'
   print(f'Is "{string}" a palindrome? : {Solution().isPalindrome(string)}')
   string2 = 'A man, a plan,a canal:panama'
   print(f'Is "{string2}" a palindrome? : {Solution().isPalindrome(string2)}')

