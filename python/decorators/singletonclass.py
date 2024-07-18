def singleton(arg):
    l=[]
    def inn():
        if len(l)==0:
            l.append(arg())
            print(arg)
        # return l[0]
    return inn
@singleton
class pvr:
    def __init__(self):
        print("pvr is created")
o1=pvr()