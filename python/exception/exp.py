class Converter(BaseException):
    def __init__(self,msg='Invalid Money Figures'):
         self.msg=msg
    def __str__(self):#this method is needed for printing error message if the exception didn't get any messages 
        return self.msg#printing of default error message or error message
def currency(money):
    try:
        if money!=0:
            print( money*80)
        else:
            raise Converter()
    except Converter as c:
        print(c)
    else:
        print('Nothing Happend')
    finally:
        print("DONE")
currency(20)