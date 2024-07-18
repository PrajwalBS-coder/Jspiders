def outer(arg):
    def inner(n1,n2):
        if(n2==0):
            arg(n2,n1)
        else:
            arg(n1,n2)
    return inner
@outer
def div(a,b):
    print(a/b)
div(2,3)
div(2,0)