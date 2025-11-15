num=int(input("Enter number:"))
if num==0:
    print("Zero")
elif num>0 and num%2==0:
    print("Positive even")
elif num>0 and num%2!=0:
    print("Positive odd")
elif num<0 and num%2==0:
    print("Negative even")
else:
    print("Negative odd")

