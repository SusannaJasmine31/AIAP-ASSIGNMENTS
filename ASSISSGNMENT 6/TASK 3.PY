def classify_age(age):
    if age < 0:
        print("Invalid age entered.")
    else:
        if age <= 12:
            print("Child")
        elif age <= 19:
            print("Teenager")
        elif age <= 35:
            print("Young Adult")
        elif age <= 60:
            print("Adult")
        else:
            print("Senior Citizen")


# Taking user input
age_value = int(input("Enter your age: "))
classify_age(age_value)