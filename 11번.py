#딕셔너리 만들기
#map을 쓰는 것도 조금 어색했고 dict 형변환, zip은 처음봤다.
name1 = input("이름입력").split()
score = map(int, input().split())
result = dict(zip(name1,score))
print(result)