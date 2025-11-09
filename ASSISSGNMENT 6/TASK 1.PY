class Student:
    def __init__(self, name):
        self.name = name
        self.roll_no = "123"       # fixed / default value
        self.branch = "ECE"        # fixed / default value

    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Branch:", self.branch)


# Taking only name from user
name = input("Enter Student Name: ")

# Creating object
student1 = Student(name)

# Displaying details
student1.display_details()