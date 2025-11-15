temp=float(input("Enter tempreture:"))
if temp<0:
    print("Freezing cold")
elif temp<=10:
    print("Very Cold")
elif temp<=20:
    print("Cold")
elif temp<=30:
    print("Warm")
elif temp<=40:
    print("Hot")
else:
    print("Extreme heat")
