s = "yyuele72uthzyoeut7oyku2yqmghy5luy9qguc28ukav7an6a2bvizhph35t86qicv4gyeo6av7gerovv5lnw47954bsv2xruaej"
k = 123365626
p=""
o=0
for i in range(len(s)):
    if s[i].isalpha():
        o+=1

if(o>1):
    for i in range(len(s)):
        if s[i].isdigit():
            p+=p*(int(s[i])-1)
        else:
            p+=s[i] 
       
if(o<=1):
    print(s[0])