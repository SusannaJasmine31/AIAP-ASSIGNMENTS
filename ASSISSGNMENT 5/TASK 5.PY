def greet_user(name, gender):
    gender = gender.lower()

    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Ms."
    else:
        title = "Mx."   # Gender-neutral title

    return f"Hello, {title} {name}! Welcome."


# Taking input from the user
name = input("Enter your name: ")
gender = input("Enter your gender (male / female / neutral): ")

# Calling the function and printing the result
print(greet_user(name, gender))