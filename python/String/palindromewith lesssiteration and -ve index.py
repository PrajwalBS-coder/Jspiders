s="SMss"
for ind in range(len(s)//2):
    if s[ind] != s[-ind-1]:
        print("NOT PAL")
        break
else:
    print("PAL")
