#l=[1,4,3,2,5,2]
l=[1,8,6,2,7,4,3,5,2]
#1,2,3,2,8,6,7,4,5
x=3
length=len(l)
count = 0
for i in range(length):
    # print(l)
    if l[i]<=x:

        for j in range(count+1,i):
            if l[i]<=l[j]:
                #temp=l.remove(l[i])
                t=l[j]
                l[j]=l[i]
                l[i]=t
                count+=1
                # l.insert(i,)
print(l)