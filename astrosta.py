n=int(input())
m=int(input())
if m==0:
    for i in range(n):
        for j in range(i+1):
            print('*',end="")
        print()


