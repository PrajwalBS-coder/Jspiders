s="abaaaba"
for ind in range(len(s)//2+1):
    #print(len(s)-1)
    #print(len(s)-ind)
    if(s[ind]!=s[len(s)-ind-1]):
        print("not palindrome")
        break
else:
    print("Palindrome")