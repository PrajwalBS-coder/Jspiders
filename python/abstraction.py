from abc import ABC,abstractmethod

class a(ABC):
    @abstractmethod
    def do_something(self):
        pass
    def do_anything(self):
        pass
class b(a):
    def do_something(self):
        print("doing something")
    def do_anything(self):
        #return super().do_anything()(self)
        print("do naything")

o1=a()
o1.do_anything()
