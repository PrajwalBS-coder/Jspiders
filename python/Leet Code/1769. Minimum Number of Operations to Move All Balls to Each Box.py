import itertools

boxes = "110"

# Get all combinations of the string
combinations = []
for r in range(1, len(boxes)):
    combinations.extend([''.join(comb) for comb in itertools.combinations(boxes, r)])

# Convert binary combinations to decimal
decimal_combinations = [int(comb, 2) for comb in combinations]

print(decimal_combinations)