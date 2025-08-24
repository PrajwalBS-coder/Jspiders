
def reorderedPowerOf2(n: int) -> bool:
    def count_digits(x):
        return ''.join(sorted(str(x)))

    target = count_digits(n)
    print(f"Target digit count: {target}")
    
    for i in range(31):
        if count_digits(1 << i) == target:
            return True
    return False

print(reorderedPowerOf2(n=1111))  # True