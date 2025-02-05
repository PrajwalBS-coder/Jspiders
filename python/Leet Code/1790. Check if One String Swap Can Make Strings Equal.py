
def is_subsequence(s1, s2):
    swap=0
    if sorted(s1)==sorted(s2):
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                swap+=1
        print(swap)
        if swap//len(s1)==1 or swap==0:
            return True
        else:
            return False
    else:
        return False
s1 = "bank"
s2 = "kanb" 
print(is_subsequence(s1,s2))