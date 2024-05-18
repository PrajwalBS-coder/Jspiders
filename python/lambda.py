var=lambda v1,v2,v3:v1+v2+v3

print(var(1,2,3))

print((lambda v1,v2,v3:v1*v2*v3)(1,2,3))
print((lambda v1,v2,v3:v1+v2+v3)('1','2','3'))

l=[2,3,4,5,6,7]
print(list(map(lambda al:al*al,l)))