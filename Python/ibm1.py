a = 5
b = 5
a_count = [1,1,4,5,5]
b_count = [4,4,3,1,5]
k = 2
c=0
for i in range(0,a):
    for j in range(i+1,a):
        # print(j)
        if a_count[i] == a_count[j]:
            for k in range(0,len(set(b_count))):
                if b_count[k] not in a_count:
                    # print(i,j)
                    a_count[j] =  b_count[k]
                    c += 1
    # print(a_count)
    if c == k:
        break

a_count = set(a_count)
print(a_count)
print(len(a_count))




# a_count = len(a)
# b_count = len(b)
# c = 0
# for i in range(0,a_count):
#     for j in range(i+1,a_count):
#         print(j)
#         if a[i] == a[j]:
#             for k in range(0,len(set(b_count))):
#                 if b[k] not in a:
#                     # print(i,j)
#                     a[j] =  b[k]
#                     c += 1
#     # print(a_count)
#     if c == k:
#         break

# return len(set(a))