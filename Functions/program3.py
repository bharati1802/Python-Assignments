def check_voting_eligibility(age):
    if age>=18:
        print("Your are eligible to vote")
    else:
        print("You are not eligible to vote")
user_age=int(input("Enter your age:"))
check_voting_eligibility(user_age)
