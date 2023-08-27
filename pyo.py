# var=0
# n, k = map(int, (input().split()))
# t=list(map(int,input().split()))
# t.sort(reverse=True)
# for i in t:
#     if i>=t[k-1] and i>0:
#         var+=1
# print(var)

# m,n=map(int,(input().split()))
# def mn(a,b):
#     if (a*b)%2==0:
#         return (a*b)//2
#     else:
#         return ((a*b)-1)//2
# print(mn(m,n))

# n=int(input())
# var=0
# while n>0:
#     t=input()
#     if t=="x++" or t=="++x" or t=="+x+" or t=="+X+" or t=="X++" or t=="++X":
#         var+=1
#     elif t=="x--" or t=="--x" or t=="-x-" or t=="--X" or t=="X--" or t=="-X-":
#         var-=1
#     n-=1
# print(var)

