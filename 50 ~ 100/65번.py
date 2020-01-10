#변형된 리스ㅌ

a = [1,2,3,4]
b = ['a','b','c','d']

list = []

for i in range(len(a)):
    if i%2==0:
        list.append([a[i], b[i]])
    else:
        list.append([b[i], a[i]])


print(list)