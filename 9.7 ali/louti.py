a = 2
b = 5
x= [1]
for each in range(1,b):
     x.append(sum(x)+1)
result = 0
if a<=b:
    result = x[a-1]

else:
    nowindex= b
    while nowindex < a:
        total = 0
        for each in x:
            total += each
        for index in range(len(x) - 1):
            x[index] = x[index + 1]
        x[-1] = total
        nowindex += 1
    result = x[-1]

print (result%10007)


