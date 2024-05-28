def fun():
    global n#if we use global keyword to declare a same var in function and alter it it 'll afect rest of the code 
    n-=1
    print(n)#we can access n because it's in globla/main space

n=89
print(n)
fun() 
print(n)