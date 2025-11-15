income=float(input("Enter your income:"))
if income<=250000:
    tax=0
elif income<=50000:
    tax=income*0.05
elif income<=100000:
    tax=income*0.20
else:
    tax=income*0.30
print("Tax to be paid in rupees",tax)
