inp = 'aaabbbbcaaddd'
#output = a3b4c3a2d3
result = ""

# l=0
a = inp[0]
count = 0
for i in range(len(inp)):
    if inp[i] == a:
        count+=1
    else:
        a = inp[i]
        result += inp[i-1]+str(count)
        count = 1
print(result+a+str(count))