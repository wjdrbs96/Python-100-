# enumerate

student = ['강은지','김유정','박현서','최성훈','홍유진','박지호',
           '권윤일','김채리','한지호','김진이','김민호','강채연']

student.sort()

for i in enumerate(student):
    print("번호: %d"  %(i[0]+1), end=", ")    #포맷팅 하는 법 기억하기
    print("이름: %s" %i[1])