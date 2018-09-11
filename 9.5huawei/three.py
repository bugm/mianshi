istr  = input()
information = []
lastindex = 0
nowindex = 0
tempindex = -1
for each in istr:
    if each.isdigit():
        tempindex = nowindex+1
        while tempindex<len(istr) and istr[tempindex].isdigit():
            tempindex+=1
        information.append((istr[lastindex:nowindex],int(istr[nowindex:tempindex])))
        lastindex = nowindex+1
    nowindex+=1
result = []
# information.sort(key=lambda x:x[0])
# information.sort(key=lambda x:x[1])
information.sort(key = lambda x:(x[1],x[0]))
result = ''
for each in information:
    for x in range(each[1]):
        result+=each[0]
print (result)