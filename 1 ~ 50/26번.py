#10진수를 2진수로 바꾸기

num = int(input())
list=[]
while num > 1:
    list.append(num%2)
    num = num // 2
    if num==1:
        list.append(num)

list.reverse()

for i in range(len(list)):
    print(list[i],end="")
