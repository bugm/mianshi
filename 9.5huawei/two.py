str1 = input()
str2 = input()
shown = [0 for each in range(26)]
for each in str1:
    shown[ord(each)-ord('A')] = 1
cancover = True
for each in str2:
    if shown[ord(each)-ord('A')] ==0:
        cancover = False
        break
if cancover:
    print("true")
else:
    print("false")

