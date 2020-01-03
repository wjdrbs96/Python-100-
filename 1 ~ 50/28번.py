# 1부터 20까지의(20포함) 모든 숫자의 자리수의 총 합을 구하시오

sum=0
for i in list(range(1,21)):
    for j in str(i):           # i가 문자형이어서 for 문 돌아감
        sum+=int(j)

print(sum)