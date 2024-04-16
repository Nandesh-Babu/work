#l=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#l=[[1,1,1],[1,0,1],[1,1,1]]
l=[[1,1,0],[1,1,1]]
# 0,0  0,1  0,2  0,3
# 1,0  1,1  1,2  1,3
# 2,0  2,1  2,2  2,3
m=len(l[0]) #col
n=len(l) #rows
l1=[[l[i][j] for j in range(m)] for i in range(n)]
print(l1)
for i in range(n):
    for j in range(m):
        if l[i][j]==0:
            for k in range(m):
                l1[i][k]=0
            for t in range(n):
                l1[t][j]=0
for i in l1:
    print(i)