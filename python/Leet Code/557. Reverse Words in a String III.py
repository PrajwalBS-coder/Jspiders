s = "Let's take LeetCode contest"
l=s.split()
k=[]
for i in l:
    k.append(i[::-1])
print(" ".join(k))