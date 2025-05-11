a = [1, 2, 3, 3, 5, 6]
first_half = a[:len(a)//2]
second_half = a[len(a)//2:]

# Calculate sum of squares of first half
sum_squares_first = sum(x**2 for x in first_half)
# Calculate sum of second half
sum_second = sum(second_half)
print(sum_squares_first,sum_second)

if sum_squares_first == sum_second:
    print(True)
else:
    print(False)