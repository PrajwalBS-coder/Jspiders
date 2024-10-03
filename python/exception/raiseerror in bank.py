class pin(BaseException):
    def __init__(self,masg):
        self.masg=masg
        
class bal(BaseException):
    def __init__(self,msg):
        self.msg=msg
class bank:
    name='Robbers Bank'
    def __init__(self,na,bal,pin):
        self.na=na
        self.bal=bal
        self.pin=pin
    def wihtdraw(self):
        
        try:
            if(self.pin!=int(input('ENter pin'))):
                raise pin('Wrong Pin')

            amt=int(input('ENter amout'))
            try:
                if(self.bal<amt):
                    raise bal('Not Enough BAl')
                self.bal=self.bal-amt
                print(self.bal)
            except bal:
                raise bal ('Not Enough BAl')
        except pin:
            raise pin('wrong Pin')

o1=bank('Jhon',100000,1234)
o1.wihtdraw()