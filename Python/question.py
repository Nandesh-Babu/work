#Counting the frequencies in a list using dictionary in Python Input: [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
# Output: 1 : 5   2 : 4   3 : 3   4 : 3   5 : 2 Explanation: Here 1 occurs 5 times, 2 occurs 4 times and so on...

l = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
d= {}

for i in l:
    d[i] = 0
    c = 0
    for j in range(0,len(l)): 
        if i == l[j]:
            # l[j].pop()
            c += 1

    d[i] = c
print(d)

