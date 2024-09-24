s = "aacecaaa"
length = len(s)
reversed_string = s[::-1]  
for i in range(length):
    if s[: length - i] == reversed_string[i:]:
        print(reversed_string[:i] + s)
print("")