# largest and smallest no in list : [20,10,20,1,100]

l = [20,10,20,1,100,200,0]

c = len(set(l))
# print(c)
maxi = 0
mini = 0

for i in l:
    lar = 0
    small = 0
    for j in range(len(l)):
        if i > l[j] and i!=l[j]:
            lar += 1
# # print(lar)
# if lar == c:
    # print(i)
        elif i< l[j] and i!=l[j]:
            small += 1
    if lar == c - 1 :
        maxi = i
    elif small == c :
        mini = i
print(maxi, mini)
