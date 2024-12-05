# l=[v for v in range(1,10)]
# print(l)
# l=[v for v in range(1,10) if v%2==0]
# print(l)
# l=[v for v in range(1,100) if v%2==0 and v%4==0]
# print(l)

# l=['A' if v%2==0  else 'B' for v in range(1,100) ]
# print(l)
# l=[[v,k] for v in range(1,10) for k in range(11,20)]
# print(l)

s=[s if s%2==0 else 'No' for s in range(10) ]
print(s)