l = [2,5,7]

lst = []
for i in l:
    temp = 1
    for j in range(1,i+1):
        temp = j * temp
        print(temp,j)
    lst.append(temp)
print(lst)