#최대값 구하기

#data = list(map(int, input().split()))  으로 하는것도 가능함
#알아두기
l = input().split()
l = [int(i) for i in l]
#max 함수 쓰는것도 기억해두자

l.sort()
print(l[-1])