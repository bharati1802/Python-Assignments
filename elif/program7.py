percentage=float(input("Enter percentage:"))
exam_score=float(input("Enter exam score:"))
if percentage>=90 and exam_score>=90:
    print("Admission in Elite program")
elif percentage>=80 and exam_score>=70:
    print("Standrd program")
elif percentage>=60 and exam_score>=50:
    print("Basic program")
else:
    print("Not eligible")

