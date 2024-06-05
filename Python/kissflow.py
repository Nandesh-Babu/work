# 12345
#6
def sumup(n):
    flag = 0
    a = 0 
    while flag == 0:
        a = a + (n % 10)
        t = n//10
        # print(a , t, n)
        if t == 0:
            flag = 1
            if a > 10:
                n = a
                a = 0
                flag = 0
            else:
                return a
        else:
            n = t
    return a   
    
print(sumup(12345))