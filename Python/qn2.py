# print duplicate string : helloo
# op: ["l","o"]
s = "helloo"
l=[]
for i in range(len(s)):
    if s[i] in s[i+1:]:
        l.append(s[i])

print(l)

