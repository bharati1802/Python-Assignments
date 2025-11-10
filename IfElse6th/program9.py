char1=input("Enter a first character:")
char2=input("Enter a second character:")
ascii_sum=ord(char1)+ord(char2)
if (ord(char1)%2!=0) and (ord(char2)%2!=0):
    print ("Sum of ASCII values:",ascii_sum)
else:
    print("sum is even")

