#3번 range 함수 인자 3개일 경우

a=10;b=2;
for i in range(1, 5, 2):   #1부터 5까지 2씩 증가하기
    a+=i;   # a= 11, 14 후에 for 문 탈출

print(a+b)   # 14 + 2 = 16