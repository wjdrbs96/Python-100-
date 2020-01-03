#요일 구하기
#2020년 1월 1일은 수요일입니다. 2020년 a월 b윌은 무슨 요일일까요?
#라이브러리를 이용해서 구하는거라 알아두기
import datetime
def solution(a,b):
    day=['Mon','Tue','WED','THU','FRI','SAT','SUN']
    return day[datetime.date(2019,a,b).weekday()]

a = int(input())  # a = month
b = int(input())  # b = day

print(solution(a,b))