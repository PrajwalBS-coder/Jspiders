seats = [7,9,20]
students = [2,15,15]
if(len(seats)>3):
    seats.sort()
    students.sort()
    #seats=list(set(seats))
    
else:
    print("else")
    seats=list(set(seats))
    seats.sort()
    students.sort()
    
tot=0
print(seats,students)
for i in range(len(seats)):
    print(students[i],seats[i])
    tot+=abs(students[i]-seats[i])
print(tot)