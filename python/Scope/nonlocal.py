def fun():
    global var
    var=90
    print("hi",var)#non local scope
    def f2():
        print("hello",var)#non-local scope
        def f3():
            print("world",var)#local scope
        f3()
    f2()


fun()
print(var)