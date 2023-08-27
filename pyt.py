# #
# a,b,x,y=map(int,(input().split()))
# if 2*a+b>2*x+y:
#     print ("messi")
# if 2*a+b<2*x+y:
#     print("ronaldo")
# else:
#     print("equal")

# t=int(input())
# lis1=[]
# while t>0:
#     x,y,z=map(int,input().split())
#     if x*y%z==0:
#         a=x*y
#         b=z
#         print(a, end=" ")
#         print(b)
#     elif y*z%x==0:
#         a=z*y
#         b=x
#         print(a, end=" ")
#         print(b)
#     elif x*z%y==0:
#         a=x*z
#         b=y
#         print(a, end=" ")
#         print(b)
#     else:
#         print(-1)
#     t-=1
    # lis1.append(x)
    # lis1.append(y)
    # lis1.append(z)
    # print(lis1[1])
    # print(lis1[0])
    # print(lis1[2])
    # if lis1[0]*lis1[1]%lis1[2]==0:
    #     a=lis1[0]*lis1[1]
    #     b=lis1[2]
    #     print(a,end=" ")
    #     print(b)
    # elif lis1[0]*lis1[2]%lis1[1]==0:
    #     a=lis1[0]*lis1[2]
    #     b=lis1[1]
    #     print(a,end=" ")
    #     print(b)
    # elif lis1[1]*lis1[2]%lis1[0]==0:
    #     a=lis1[2]*lis1[1]
    #     b=lis1[0]
    #     print(a,end=" ")
    #     print(b)
    # else:
    #     print(-1)
    # print(a, end=" ")
    # print(b)
    # t-=1
# t=int(input())
# while t>0:
#     dic = {}
#     n=int(input())
#     a=map(int,(input().split()))
#     d = map(int, (input().split()))
#     for i in a:
#         if i not in dic.keys():
#             dic[i]=1
#         else:
#             dic[i]+=1
#     for j in d:
#         if j not in dic.keys():
#             dic[j]=1
#         else:
#             dic[j]+=1
#     lis=list(dic.values())
#     lis.sort(reverse=True)
#     # pri
#     print(lis[0])
#     t-=1