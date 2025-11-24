"""
Student Marks Analysis - Solution
Compute mean and list students above the mean
"""

def analyze_student_marks(students_data):
    """
    Analyze student marks and find those above the mean.
    
    Args:
        students_data: Dictionary with student names as keys and marks as values
        
    Returns:
        tuple: (mean, list of students above mean)
    """
    if not students_data:
        return 0, []
    
    # Calculate mean
    marks = list(students_data.values())
    mean = sum(marks) / len(marks)
    
    # Find students above mean
    above_mean = [name for name, mark in students_data.items() if mark > mean]
    
    return mean, above_mean


def main():
    # Sample data
    students = {
        "Alice": 85,
        "Bob": 72,
        "Charlie": 90,
        "Diana": 78,
        "Eve": 95,
        "Frank": 68
    }
    
    mean, above_mean_students = analyze_student_marks(students)
    
    print("Student Marks Analysis")
    print("=" * 40)
    print("\nAll Students:")
    for name, mark in students.items():
        print(f"  {name}: {mark}")
    
    print(f"\nMean: {mean:.2f}")
    print(f"\nStudents Above Mean:")
    for student in above_mean_students:
        print(f"  {student}: {students[student]}")


if __name__ == "__main__":
    main()
