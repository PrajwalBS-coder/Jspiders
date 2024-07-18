# s = "(]"
# for i in range(len(s)):
#     if s[i] == '(':
#         if ')' not in s:
#             print('no')
#             break
#     if s[i] == '[':
#         if ']' not in s:
#             print('no')
#             break
#     if s[i] == '{':
#         if '}' not in s:
#             print('no')
#             break
# else:
#     print('Yes')

# s="()[]{}"
# if "()" in s:
#     s=s.replace("()","")
# if "[]" in s:
#    s= s.replace("[]","")
# if "{}" in s:
#    s= s.replace("{}","")
# print(len(s)==0)
# print(s)
s="([])"
c=0
for i in range(len(s)):
    if s[i]=='(' or s[i]=='[' or s[i]=='{':
        c+=1
    else:
        c-=1
print(c==0)