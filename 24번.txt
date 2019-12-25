#소수 판별하기
#소수이면 Yes, 아니면 No

count=0
num = int(input())
for i in range(2,num+1):
    if num % i == 0:
        count+=1

if(count==1):
    print("Yes")
else:
    print("No")
