#program to find strings are isomorph

def isisomorphic(s,t):
    
    if len(s)!=len(t):
       return False
    else:
       mapping1={}
       mapping2={}
       for i in range(len(s)):
           character1=s[i]
           character2=t[i]
           if character1 not in mapping1:
               mapping1[character1]=character2
           if character2 not in mapping2:
               mapping2[character2]=character1
           if mapping1[character1]!=character2 or mapping2[character2]!=character1:
               return false
    print(" true")
s=input("enter string s = ")
t=input("enter string t =")
print(isisomorphic(s,t))  
