#Replace duplicate Occurrence in String test_str = 'Gfg is best . Gfg also has Classes now. \ Classes help understand better .'
# ' repl_dict = {'Gfg' : 'It', 'Classes' : 'They' } output: Gfg is best.It also has Classes now. They help understand better

test_str = 'Gfg is best . Gfg also has Classes now. \ Classes help understand better'

repl_dict = {'Gfg' : 'It', 'Classes' : 'They' }

l = list(repl_dict.keys())

lst = test_str.split(" ")
c = 0
for i in l:
    
    for j in range(len(lst)):
        if i == lst[j]:

            c+=1
        if c >= 2:
            lst[j] = repl_dict[i]
            c = 0
            print(lst[j], repl_dict[i])
    # print(c)
# for i 
        
