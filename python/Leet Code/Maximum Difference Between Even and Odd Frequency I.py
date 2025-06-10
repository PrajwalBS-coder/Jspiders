s = "aaaaabbc"
odd=[s.count(s[i]) for i in range(len(s)) if s.count(s[i])%2!=0]

even=[s.count(s[i]) for i in range(len(s)) if s.count(s[i])%2==0]
print(max(odd)-min(even))
print(odd,even)
