# low = 3
# high = 7
# c=0
# for i in range(low,high+1):
#     if(i%2==1):
#         c+=1
# print(c)

low = 3
high = 7
odd = (high - low) // 2
if low % 2 == 1 or high % 2 == 1:
    odd += 1
print(odd)