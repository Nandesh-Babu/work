def con_vow(s):
    vow=0
    d_vow={}
    d_con={}
    con=0
    for i in s:
        if i in "aeiouAEIOU":
            vow+=1
            if i in d_vow:
                d_vow[i]=d_vow[i]+1
            else:
                d_vow[i]=1
            #-----vowels dict 
        elif i.isalpha() and i not in "aeiouAEIOU":
            con+=1
            if i in d_con:
                d_con[i]=d_con[i]+1
            else:
                d_con[i]=1
    print(d_vow,d_con,end="\n")
    return f"Number of vow is {vow} and Number of Con is {con}"
        

s = "This is a Mango Tree"
print(con_vow(s))
