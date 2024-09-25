message = ["hello","programming","fun"]
bannedWords = ["world","programming","leetcode"]
c=0
for i in message:
    if i in bannedWords:
        c+=1
if(c>=2):
    print(True)
else:
    print(False)