def out(arg):
    def inner():
        arg()
    return inner
@out
class a:
    def __init__(self):
        print("init")
a()
a()