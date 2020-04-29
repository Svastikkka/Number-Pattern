
"""
Pattern for N = 4
1
23
345
4567

"""
num=int(input())
count=num
for i in range(1,num+1):
    while count>0:
        print("  ",end="")
        count=count-1
    for j in range(0,i):
        print(i+j,end="")
    print()
    count=num-i