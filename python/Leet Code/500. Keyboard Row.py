fst="qwertyuiop"
sec="asdfghjkl"
thr="zxcvbnm"
words = ["Hello","Alaska","Dad","Peace"]
p=[]
for word in words:
    for l in word:
        if  l in fst or l in sec or l in thr:
            pass
        else:
            break
    p.append(word)

print(p)