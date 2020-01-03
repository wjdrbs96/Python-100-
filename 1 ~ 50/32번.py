# 버블 정렬 구현하기

list = [4,2,3,8,5]

for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            tmp = list[j]
            list[j]=list[j+1]
            list[j+1]=tmp

print(list)