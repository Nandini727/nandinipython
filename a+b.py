# n=int(input())
# def ad(a,b):
#     return a+b
# for i in range(n):
#     a,b=map(int,input().split())
#     print(ad(a,b))
# t=int(input())
# i=0
# for i in range(10):
#     s=str(input())
#     print(s,end="")
t=int(input())
while t>0:
    lis=[]
    var=0
    s=str(input())
    s.split(",")
    lis.append(s)
    if lis[0]!="c":
        var+=1
    elif lis[1]!="o":
        var+=1
    elif lis[2]!="d":
        var+=1
    elif lis[3]!="e":
        var+=1
    elif lis[4]!="f":
        var+=1
    elif lis[5]!="o":
        var+=1
    elif lis[6]!="r":
        var+=1
    elif lis[7]!="c":
        var+=1
    elif lis[8]!="e":
        var += 1
    elif lis[9]!="s":
        var+=1
    print(var)
    t-=1