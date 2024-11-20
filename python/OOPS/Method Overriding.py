class A:
    def disp(self):
        print("It's Parent")

class B(A):
    def disp(self,msg='Hello'):
        A().disp()
        print(f'{msg} Child')

o1=B()
o1.disp('Hi')
o2=A()
o2.disp()
# class Parent:
#     def display(self):
#         print("Parent display method")

# class Child(Parent):
#     def display(self):
#         print(f"Child display method")

# # Usage
# obj = Child()
# obj.display()  # Error: Unexpected behavior due to mismatch in method signatures
