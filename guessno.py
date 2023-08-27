print("test your guessing skills with this mini number guessing game!")
print("maximum no. of guesses=6")
count=0
flag=1
while count<6:
    count=count+1
    # for i from 0 to 6
    # for i from 1 to 6 range(1,6)
    # form 1 to 6 skip 2 range(1,6,2)
    n=int(input("Enter guess: "))
    if n==18:
        print('mizuketa!')
        print("nice")
        break
    elif n<18:
        print("motto ue")
    else:
        print('hayesugiru')
if count>=6:
    print('fail :(')