# logical_and_nested_if.py

is_student = True
is_employed = False

if is_student and is_employed:
    print("You are a working student.")
elif is_student and not is_employed:
    print("You are a student.")
elif not is_student and is_employed:
    print("You are employed but not a student.")

# Nested if statements
age = int(input("Enter your age: "))
if age >= 18:
    has_license = input("Do you have a driver's license? (yes/no): ").lower()
    if has_license == "yes":
        print("You are allowed to drive.")
    else:
        print("You need a driver's license to drive.")
else:
    print("You are not old enough to drive.")
