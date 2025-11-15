age=int(input("Enter age:"))
weight=int(input("Enter weight:"))
hb=float(input("Enter hb:"))
if age<18 or age>65:
    print("You are not eligible for blood donation")
elif weight<=50:
    print("You are not eligible for blood donation")
elif hb<=12.5:
    print("You are not eligible for blood donation")
else:
    print("Eligible for blood donation")

