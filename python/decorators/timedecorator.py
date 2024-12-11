import time

def fun2(a):
    def fun3():
        a()
        print("Bye")
        print(time.time())    
    return fun3
@fun2
def fun():
    print(time.time())
    print('Hi')
fun()