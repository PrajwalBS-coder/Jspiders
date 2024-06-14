s = "abc", 
shifts = [[0,1,0],[1,2,1],[0,2,1]]
for i in range(len(shifts)):
    for j in range(len(s)):
        if(shifts[i][-1]==0):
            for k in range(shifts[i][0],shifts[i][1]):