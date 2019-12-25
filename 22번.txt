#오타 수정하기 => q 를 e로 바꾸기
# str1 = list(input())
# for i in range(len(str1)):
#     if str1[i] =='q':
#         str1[i]='e'

# for j in range(len(str1)):
#     print(str1[j],end="")

#내장함수를 사용하면 간단히 해결가능
str1 = input()
print(str1.replace('q','e'))

