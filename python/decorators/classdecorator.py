def outer(a):
    def inn():
        a()
    return inn
@outer
class a:
    def __init__(self):
        print("hello object created")
a()