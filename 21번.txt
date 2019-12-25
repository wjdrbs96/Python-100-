# 1,2,3 등이 몇명인지 세기 (중복 포함)

l = input("입력").split()
l = list(map(int,l))
# l = [int(i) for i in l]  #이 표현 기억해두기
#문자로 입력받은 리스트를 정수로 바꿔주기, map도 사용가능
count=0
for i in range(3):
    top = max(l)
    count+=l.count(top)
    for j in range(l.count(top)):
        l.remove(top)

print(count)