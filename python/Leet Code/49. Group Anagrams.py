strs = [""]#time limit exceed
l=[]
# for i in range(len(strs)):
#     p=[]
#     # p.append(strs[i])
#     for j in range(len(strs)):
#         if sorted(strs[i])==sorted(strs[j]):
#             p.append(strs[j])
#     l.append(p)
# unique_lists = list(set(tuple(x) for x in l))
# unique_lists = [list(x) for x in unique_lists]
# print(unique_lists)
anagram_map = dict(list)
for word in strs:
    sorted_word = ''.join(sorted(word))
    anagram_map[sorted_word].append(word)
print(list(anagram_map.values()))