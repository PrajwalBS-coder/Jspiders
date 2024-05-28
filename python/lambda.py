var=lambda v1,v2,v3:v1+v2+v3

print(var(1,2,3))

print((lambda v1,v2,v3:v1*v2*v3)(1,2,3))
print((lambda v1,v2,v3:v1+v2+v3)('1','2','3'))

l=[2,3,4,5,6,7]
k=[2,3,4,5,6,7]
j=[2,3,4,5,6,7]
print(list(map(lambda al,a2,a3:al+a2+a3 ,l,k,j)) )