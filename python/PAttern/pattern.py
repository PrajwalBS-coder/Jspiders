var=10
for l in range(1,(var%2)+3):
    print(" "*(var-l)+"*" * ((2*l)-1))

for l in range(((var%2)+3),0,-1):
    print(" "*(var-l)+"*" * ((2*l)-1))#only work for var=7