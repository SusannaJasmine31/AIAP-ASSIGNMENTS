class sru_student:
    """A class to represent a SRU student with hostel information and fee management.

    This class manages student information including name, roll number, and hostel
    status, with methods to update fees and display student details.

    Attributes:
        name (str): The full name of the student.
        roll_no (str): The roll number of the student.
        hostel_status (str): The hostel status ('In-Hostel' or 'Day Scholar').
        fees_paid (float): Amount of fees paid by the student (default: 0.0).

    Methods:
        fee_update(amount): Updates the fees paid by adding the given amount.
        display_details(): Displays all student information in a formatted manner.
    """

    def __init__(self, name, roll_no, hostel_status, fees_paid=0.0):
        """Initialize a student object.

        Args:
            name (str): Student's full name.
            roll_no (str): Student's roll number.
            hostel_status (str): Hostel status ('In-Hostel' or 'Day Scholar').
            fees_paid (float, optional): Initial fees paid. Defaults to 0.0.
        """
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fees_paid = fees_paid

    def fee_update(self, amount):
        """Update the fees paid by the student.

        Args:
            amount (float): The amount to add to the fees paid.

        Returns:
            float: The updated total fees paid.

        Raises:
            ValueError: If the amount is negative.

        Examples:
            >>> student = sru_student("jasli", "A001", "In-Hostel", 5000)
            >>> student.fee_update(2000)
            7000.0
        """
        if amount < 0:
            raise ValueError("Fee amount cannot be negative.")
        
        self.fees_paid += amount
        return self.fees_paid

    def display_details(self):
        """Display all student details in a formatted manner.

        Prints the student's name, roll number, hostel status, and fees paid
        in a well-organized tabular format.

        Returns:
            None
        """
        print("\n" + "=" * 60)
        print("                    STUDENT DETAILS                      ")
        print("=" * 60)
        print(f"Name            : {self.name}")
        print(f"Roll Number     : {self.roll_no}")
        print(f"Hostel Status   : {self.hostel_status}")
        print(f"Fees Paid (₹)   : {self.fees_paid}")
        print("=" * 60 + "\n")


# ============================================================================
# TEST CASES
# ============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("         SRU STUDENT MANAGEMENT SYSTEM")
    print("=" * 60)

    # Create student objects
    student1 = sru_student("Jasmine Singh", "A001", "In-Hostel", 5000)
    student2 = sru_student("Kiran Kumar", "A002", "Day Scholar", 3000)
    student3 = sru_student("susan roy", "A003", "In-Hostel")

    # Display initial details
    print("\n--- Initial Student Details ---")
    student1.display_details()
    student2.display_details()
    student3.display_details()

    # Update fees for students
    print("\n--- Updating Fees ---")
    print(f"Student 1: Fee updated to ₹{student1.fee_update(2000)}")
    print(f"Student 2: Fee updated to ₹{student2.fee_update(1500)}")
    print(f"Student 3: Fee updated to ₹{student3.fee_update(5000)}")

    # Display updated details
    print("\n--- Updated Student Details ---")
    student1.display_details()
    student2.display_details()
    student3.display_details()

    # Test error handling
    print("\n--- Testing Error Handling ---")
    try:
        student1.fee_update(-500)
    except ValueError as e:
        print(f"Error caught: {e}")

    print("\n--- Final Student Details ---")
    student1.display_details()
    student2.display_details()
    student3.display_details()