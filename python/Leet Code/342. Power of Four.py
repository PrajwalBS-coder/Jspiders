n=1
def find(n):
    for i in range(n):
        if n==4**i:
            return True
    else:
        return False
print(find(n))