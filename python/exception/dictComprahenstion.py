# print({str(v):v for v in range(1,10)})
print({str(v):v if v%2==0 else 0 for v in range(1,10)})