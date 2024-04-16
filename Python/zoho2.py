#3,5,8,13,21
#8,4,2,0,-2
#1,4,1,5,9,26
# array = [8, 6, 3, 10, 0]
array = [3,5,8,13,21]
count=0
count1=0
for i in range(len(array)-1):
    if array[i]<array[i+1]:
        count+=1
    else:
        count1+=1
if count==len(array)-1 or count1==len(array)-1:
    print(True)
else:
    print(False)