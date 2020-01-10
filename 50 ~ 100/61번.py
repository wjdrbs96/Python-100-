#문자열 압축하기

count = 0
name = input()
str1=""
#str1=[]
list=[]

for i in range(len(name)):
    list.append(name[i])

start = list[0]

for j in range(len(name)):
    if start == list[j]:
        count+=1

    else:
        #str1.append(start + str(count))
        str1+=start + str(count)
        start = list[j]
        count = 0
        count+=1

#str1.append(start + str(count))
str1+=start + str(count)

print(str1)
#for k in str1:
 #   print(k, end="")


