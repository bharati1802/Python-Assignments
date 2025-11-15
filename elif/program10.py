a1=int(input("Enter first angle:"))
a2=int(input("Enter second angle:"))
a3=int(input("Enter third angle:"))
if a1+a2+a3!=180:
    print("Invalid Trainle")
elif a1<90 or a2<90 or a3<90:
    print ("Traingle is a Acute")
elif a1>90 or a2>90 or a3>90:
    print ("Traingle is Obtuse")
else:
    print("Traingle is right angled traingle") 
