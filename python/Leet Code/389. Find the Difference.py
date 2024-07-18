# s = "abcd"
# t = "abcde"
# print(str(set(t)-set(s)).strip("'{}'"))

s = "a"
t = "aa"
for i in range(len(t)):
    if t[i] in s:
        s=s.replace(t[i],"")
    else:
        print(t[i])
print(s.count("a"))
