def quicksort_partition(arr):
    pivot = arr[0]  # Choose the first element as pivot
    left = []       # Elements less than pivot
    right = []      # Elements greater than pivot

    for elem in arr[1:]:  # Start from the second element
        if elem < pivot:
            left.append(elem)
        else:
            right.append(elem)

    return left + [pivot] + right  # Combine lists

# Input
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the array elements: ").split()))

# Output
result = quicksort_partition(arr)
print(" ".join(map(str, result)))
