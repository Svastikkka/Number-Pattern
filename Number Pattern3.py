num=int(input())
i=1
while num>=i:
    j=1
    while j<=i:
        print(j,end="")
        j+=1

    space=1
    spaces=1
    while spaces<=(num-i):
        print(" ",end="")
        spaces=spaces+1
    spaces=1
    while spaces<=(num-i):
        print(" ",end="")
        spaces=spaces+1
    k=i
    while k>=1:
        print(k,end="")
        k=k-1
    print()
    i += 1
