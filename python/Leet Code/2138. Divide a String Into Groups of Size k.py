s = "abcdefghij"
k = 3
fill = "x"
if len(s) % k == 0:
    result = [s[i:i + k] for i in range(0, len(s), k)]
else:
    s += fill * (k - len(s) % k)
    result = [s[i:i + k] for i in range(0, len(s), k)]
print(result)