floor = int(input())
result = 0
if floor < 3:
    result = 1 if floor == 1 else 2
else:
    temp1 = 1
    temp2 = 2
    index = 3
    while index<= floor:
        result = temp1+temp2
        temp1 = temp2
        temp2  = result
        index+=1
print (result)