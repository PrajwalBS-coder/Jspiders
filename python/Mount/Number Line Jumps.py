x1, v1, x2, v2=0, 2, 5, 3
if v1 == v2:  # Same speed
    print( "YES" if x1 == x2 else "NO")
    exit()
    
    # Check if they meet
if (x2 - x1) * (v1 - v2) < 0:  # Different directions
    print( "NO")
    exit()
    
if (x2 - x1) % (v1 - v2) == 0:  # Check divisibility
    print( "YES")
    exit()
    
print( "NO")