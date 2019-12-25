#별 찍기
#      *
#     ***
#    *****
#   *******
#  *********

num = int(input("입력"));
count=1;
for i in range(num-1,-1,-1):
    while i>0:
        print(" ", end="")
        i-=1
    for j in range(count):
        print("*",end="")
    count+=2;
    print("")