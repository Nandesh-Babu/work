l=5601
n=60
a=[i for i in str(l)]
count=0
for j in range(n):
    temp=[i for i in str(j)]
    length=len(temp)
    f=0
    for k in temp:
        if k in a:
            f+=1
    if f==length:
        count+=1
        print(j,end=" ")

print("\n",count)