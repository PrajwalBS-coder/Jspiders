# arr = [1,2,3,10,4,2,3,5]
# l=[]
# for i in range(1,len(arr)+1):
#     if arr[i-1]<=arr[i]<=arr[i+1]:
#         pass
#     else:
#         l.append(arr[i])
#         arr.pop(i)
# print(arr)
# print(l)

arr = [5,4,3,2,1]
arr2=arr.copy()
arr.sort()
if arr==arr2:
    print(len(arr)-1)
l = []
i = 1  # start from the second element

# Loop while i is within the array bounds


while i < len(arr) - 1:
    if arr[i-1] <= arr[i] <= arr[i+1]:
        i += 1
    else:
        l.append(arr[i])
        arr.pop(i)

print("Updated arr:", arr)
print("Elements removed:", l)
