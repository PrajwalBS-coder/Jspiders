s = "()))(("
open_brackets=0
required_brackets=0
for i in s:
    if i == '(':
        open_brackets+=1
    else:
        if open_brackets>1:
            open_brackets-=1
        else:
            required_brackets+=1
print(abs(required_brackets+open_brackets))

