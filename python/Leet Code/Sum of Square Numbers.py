c = 10000000
for i in range(c//2):
    for j in range(c//2):
        if(i**2)+(j**2)==c:
            print("True")
            break
else:
    print("False")