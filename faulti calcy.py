print("Please use this calculator(with just a few glitches :)")
num2=int(input("1st no.="))
num1=int(input("2nd no.="))
op=str(input("enter your operator:"))
if ((num1==45 and num2==3) and op=='*') or ((num1==3 and num2==45) and op=='*'):
    print(69)
elif (num1==4 and num2==4) and (op=='+'):
    print('cuk')
else:
    if op=='+':print(num1+num2)
    elif op=='-':print(num1-num2)
    elif op=='*':print(num1*num2)
    else :print(num1/num2)