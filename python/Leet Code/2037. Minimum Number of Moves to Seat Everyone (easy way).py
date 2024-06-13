seats = [3,1,5]
students = [2,7,4]

seats = sorted(seats)
students = sorted(students)
min_moves = 0
for i in range(len(seats)):
    min_moves += abs(seats[i] - students[i])
        
print(min_moves) 