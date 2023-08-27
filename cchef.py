T=int(input())
while T>0:
    N=int(input())
    l=list(map(int,input().split()))
    sum=0
    cnt=0
    streakom=0
    streakaddy=0
    for i in l:
        if i==0:
            streakom=max(streakom,cnt)
            cnt=0
        else:cnt+=1
    streakom=max(streakom,cnt)
    b=list(map(int,(input().split())))
    mus=0
    tnuoc=0
    for j in b:
        if j==0:
            streakaddy=max(streakaddy,tnuoc)
            tnuoc=0
        else:
            tnuoc+=1
    streakaddy=max(streakaddy,tnuoc)
    if streakom>streakaddy:
        print("OM")
    elif streakom<streakaddy:
        print("ADDY")
    else:
        print("DRAW")
    T-=1