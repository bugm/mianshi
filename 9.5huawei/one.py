first = input()
second = input()
result = ""
f_index = len(first)-1
s_index = len(second)-1
zero = ord('a')
addbit = False
while f_index>-1 and s_index>-1:
    tempresult = ord(first[f_index])+ord(second[s_index]) - 2 * zero
    if addbit:
        tempresult+=1
        addbit = False
    if tempresult>25:
        addbit = True
    result+=chr(zero+tempresult%26)
    f_index-=1
    s_index-=1
while f_index>-1:
    tempresult = ord(first[f_index])-zero
    if addbit:
        tempresult+=1
        addbit = False
    if tempresult>25:
        addbit = True
    result+=chr(zero+tempresult%26)
    f_index-=1

while s_index>-1:
    tempresult = ord(second[s_index]) - zero
    if addbit:
        tempresult += 1
        addbit = False
    if tempresult > 25:
        addbit = True
    result += chr(zero + tempresult % 26)
    s_index-=1
if addbit == True:
    result +='b'
print (result[::-1])



