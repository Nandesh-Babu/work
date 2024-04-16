l = [2, 7, 11, 15]
t =  9

#l = input()
# l=[-11, 3, 5, 20, 45, 6]
# l=[3,-1,2]
# t=-5
# t=7
index=[]
f=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if i==j:
            continue
        else:
            temp = l[i]+l[j]
            if temp==t:
                f+=1
                index.append(i)
                index.append(j)
                print(True)
                print("Indices:",index)
                break
if f==0:
    print(False)

# f=0
# for i in range(len(l)-1):
#     temp=l[i]+l[i+1]
#     if temp==t:
#         f=0
#         index.append(i)
#         index.append(i+1)
#         print(True)
#         print("Indices:",index)
#         break
#     else:
#         f=1
# if f==1:
#     print(False)