#제곱을 구하자
a = int(input("a 입력"))
b = int(input("b 입력"))
sum=3
for i in range(b-1):
    sum*=a;

print(sum)