#각 자리수의 합
#사용자가 입력한 양의 정수의 각 자리수의 합을 구하는 프로그램

num = int(input())
list=[]
sum=0
while num:
    list.append(num%10)
    num = num//10

for i in range(len(list)):
    sum+=list[i]

print(sum)