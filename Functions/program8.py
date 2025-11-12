def display_student_details(**kwargs):
    print("Student Details:")
    for key ,value in kwargs.items():
        print(key, ":",value)
display_student_details(name="Bharati", age=22,course="BCA")
