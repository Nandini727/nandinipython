# def encrypt(FED,s):
#     result=""
#     for char in FED:
#         if char.isupper():
#             result+=chr((ord(char)-65+s)%26+65)
#         else:
#             result+=chr((ord(char)+s-97)%26+65)
#     return result
# def decrypt(text,s):
#     result=""
#     for char in text:
#         if char.isupper():
#             #65->65+23
#             result += chr((ord(char) + (26-s) - 65) % 26+65)
#         else:
#             result += chr((ord(char) + (26-s) - 97) % 26+97)
#     return result
# print(encrypt("X",3))
# n=str(input())
# m=str(input())
# if len(n)<=6 and
#     print(encrypt(n,4))
def encrypt(letter,s):
    result=""
    for char in letter:
        if char.islower():
            result+=chr((ord(char)-97+s)%26+97)
        else:
            result+=chr((ord(char)+s-122)%26+97)
    return result
q=int(input())
while q>0:
    N=int(input())
    s=input()
    len(s)=N

    q-=1