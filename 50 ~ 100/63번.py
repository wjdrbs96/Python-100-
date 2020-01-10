#63번 친해지고 싶어(말 줄이기)

name = input()

list = name.split(" ")
print(list)
j=0
for i in range(len(list)):
    print(list[i][j],end="")