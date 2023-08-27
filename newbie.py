# N=int(input())
# lis=[]
# li s1=[]
# lis2=[]
# lis3=[]
# while N>0:
#     a,b=map(int,(input().split()))
#     lis.append(a)
#     lis1.append(b)
#     lis2.append(a - b)
#     lis3.append(b - a)
#     N-=1
# lis2.sort(reverse=True)
# lis3.sort(reverse=True)
# if lis2[0]>lis3[0]:
#     print(1,lis2[0])
# else:
#     print(2,lis3[0])
# var=0
# var1=0
# lis=[]
# lis1=[]
# N=int(input())
# while N>0:
#     a,b=map(int,(input().split()))
#     var+=a-b
#     var1+=b-a
#     if a-b>=var:
#         lis.append(var-var1)
#     if b-a>=var1:
#         lis1.append(var1-var)
#     N-=1
# lis.sort(reverse=True)
# lis1.sort(reverse=True)
# if lis[0]>lis1[0]:
#     print(1,lis[0])
# else:
#     print(2,lis1[0])