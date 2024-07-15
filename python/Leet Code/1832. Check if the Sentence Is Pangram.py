sentence = "thequickbrownfoxjumpsoverthelazydog"
s=str(set(sentence))
print(len(s),len(sentence))
c=0
#set is a collection which is unordered and unindexed. In Python, sets are written with curly
#braces, and you can add elements, remove elements, or iterate over sets.
#set is a collection which is unordered and unindexed. In Python, sets are written with curly
#braces, and you can add elements, remove elements, or iterate over sets.
for i in range(28):
    if(chr(95+i) in s):
        print(chr(95+i))
        c+=1
print(c)
if(c==26):
    print("OK")
else:
    print("NOT OK")
