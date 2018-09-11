# from collections import defaultdict
# entity = "singer_周杰|周杰伦;song_冰雨|北京欢迎你;actor_周杰伦|孙俪"
# userquery = "周杰伦"
# type = entity.split(';')
# typename = [each.split('_')[0] for each in type]
# typecontent = []
# matchdict = []
# tempmatch = []
# matched = []
# index = 0
# for each in type:
#     matched.append([])
#     temp = set([])
#     matchdict.append(defaultdict(int))
#     tempmatch.append([])
#     typecontent.append(defaultdict(int))
#     for entityname in each.split('_')[1].split('|'):
#         temp.update(entityname)
#         for word in temp:
#             typecontent[index][word] = 1
#
#
#     index+=1
# print (typecontent)
# print (matchdict)
# for index in range(len(userquery)):
#     eachword  = userquery[index]
#     nowmatched = []
#     for eachtype in range(len(typecontent)):
#         if typecontent[eachtype][eachword]:
#             for each in range(tempmatch[eachtype]):
#                  tempmatch[eachtype][each]




# for index in range(len(userquery)):
#     eachword = userquery[index]
#     typeindex = 0
#     while typeindex < len(typename):
#         entityindex = 0
#         while entityindex < len(typecontent[typeindex]):
#             if eachword == typecontent[typeindex][entityindex][tempmatch[typeindex][entityindex]]
#                 tempmatch[typeindex][entityindex]+=1
#             else:
#                 tempmatch[typeindex][entityindex] = 0
#         for each in
#
#             entityindex+=1
#         entityindex+=1
x = {}
for each in range(100000000000):
    x[each] = 1
for temp in range(100000000):
    if temp not in x:
       z =1
    else :
        z=2
print('finish')