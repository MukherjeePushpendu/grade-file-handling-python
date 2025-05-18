# Student Grades
# This program manages student grades using a dictionary.

grades = {}

while True:
    print("\nMenu:")
    print("1. Add new student and grade")
    print("2. Update existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        grades[name] = grade
        print(f"{name} added successfully.")

    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in grades:
            new_grade = input("Enter new grade: ")
            grades[name] = new_grade
            print(f"{name}'s grade updated.")
        else:
            print(f"{name} not found.")

    elif choice == '3':
        print("\nStudent Grades:")
        for student, grade in grades.items():
            print(f"{student}: {grade}")

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
