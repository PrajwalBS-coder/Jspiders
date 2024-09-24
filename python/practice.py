class it:
    def __init__(self,sv,ev):
        self.sv=sv
        self.ev=ev
    def __iter__(self):
        return self
    def __next__(self):
        n=self.sv
        if(self.sv==self.ev+1):
            raise StopIteration
        self.sv+=1
        return n
o1=it(0,6)
itobj=iter(o1)
for i in range (0,6+2):
    print(next(itobj))
        