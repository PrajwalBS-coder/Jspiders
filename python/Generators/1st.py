def a():
    v1=10
    yield v1
    v2=90
    yield v2
print(next(a()))#it'll call the 1st yield statement
print(next(a()))#here also same cause we're using same method name ,so we've to go with function obj
o1=a()
print(next(o1))#it'll call the 1st yield statement
print(next(o1))#it'll call the 2nd yield statement
print(next(o1))#error stop iteration