# 풀지 못한 문제
n = int(input())
result =0

while True:
    if n % 7 ==0:
        result+=n//7
        print(result)
        break
    n-=3
    result+=1

    if n < 0:
        print("-1")
        break



