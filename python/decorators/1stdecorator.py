def f1(a):
    def f2():
        a()
        print("Bye")
    return f2
@f1
def f3():
    print("hello")
f3()