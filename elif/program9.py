amount=float(input("Enter your purchase amount:"))
if amount<1000:
    discount=0
elif amount<5000:
    discount=5
elif amount<10000:
    discont=10
elif amount<20000:
    discount=20
else:
 discount=30
final_amount=amount-(amount*discount/100)
print("Discount applied")
print("Final amount",final_amount)
