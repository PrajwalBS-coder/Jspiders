nums = [3,30,34,5,9]
num_strings = [str(num) for num in nums]
print(num_strings)
num_strings.sort(key=lambda a: a * 10, reverse=True)
print(num_strings)
if num_strings[0] == "0":
    print("0")
print( "".join(num_strings))