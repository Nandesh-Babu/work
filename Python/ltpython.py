# [15:31] Sanchit Sudhir Moraskar
# abcbea

# s = "abcba"

# l = list(s)
# cnt = len(l)
# temp = 0
# for i in range(0,len(l)):
#     if l[i] == l[cnt - i]:
#         temp +=1
# if temp == ((cnt - 1)/2):
#     print("palin")
# else:
#     print("not palin") 


# [a,b,c,d]

l = ["a","b","c","d"]

d = {}

for i in range(0,len(l)):
    d[i+1] = l[i]

print(d)


 