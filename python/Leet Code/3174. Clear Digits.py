s = "cbef"
i = 0
l=[]

for i in s:
    if i.isalpha():
        l.append(i)
    if i.isdigit():
        if l:
            l.pop()
print("".join(l))
