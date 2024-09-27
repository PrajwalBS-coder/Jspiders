# input = "interviewquery"
input = "interv"
for i in input:
    if input.count(i)>=2:
        print(i)
        break
else:
    print(None)