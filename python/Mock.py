# # # def outer(arg):
# # #     def inner():
# # #         print('innner')
# # #         arg
# # #     return inner
# # # # @outer
# # # # def fun():
# # # #     print('Hello')
# # # # fun()

# # # @outer
# # # class a:
# # #     def __init__(self):
# # #         print('ok')
# # # a()
# # # def singleton(arg):
# # #     l=[]
# # #     def inner():
# # #         if len(l)==0:
# # #             l.append(arg())
# # #         return l[0]
# # #     return inner
# # # @singleton
# # # class book:
# # #     def __init__(self):
# # #         self.ticket=100
# # #     def booking(self,t):
# # #         self.ticket-=t
# # #         print('Availbael',self.ticket)

# # # def buy():
# # #     o1=book()
# # #     t=int(input('enter ticket'))
# # #     o1.booking(t)
# # # p1=buy()
# # # p2=buy()
# # # def singleton(cls):
# # #     instance = []
# # #     def get_instance(*args, **kwargs):
# # #         if not instance:
# # #             instance.append(cls(*args, **kwargs))
# # #         return instance[0]
# # #     return get_instance

# # # @singleton
# # # class Book:
# # #     def __init__(self):
# # #         self.ticket = 100
    
# # #     def booking(self, t):
# # #         if t <= self.ticket:
# # #             self.ticket -= t
# # #             print(f'Tickets available: {self.ticket}')
# # #         else:
# # #             print('Not enough tickets available')

# # # def buy():
# # #     o1 = Book()
# # #     t = int(input('Enter number of tickets: '))
# # #     o1.booking(t)

# # # p1 = buy
# # # p1()
# # # print(r'Python Amin Jhon')
# # print({**{1:2,3:4,5:6},**{7:8,9:0}})
# class v1:
#     def __init__(self,na):
#         self.na=na
        
#     def m1(self):
#         print('Parent',self.na)
# class v2(v1):
#     def __init__(s,na,no):
#         super().__init__(na)
#         s.no=no

#     def m2(s):
#         print('Child',s.no)
#         super().m1()
# o1=v2('Amin',10)
# o1.m2()
  