def student_management():
    """A simple student management system using a dictionary."""
    students = {}
    while True:
        print("\n===== Student Management =====")
        print("1. Add Student")
        print("2. Look Up Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Quit")
        choice = input("Enter your choice (1-5): ")
        # Add Student
        if choice == "1":
            name = input("Enter student name: ")
            section = input("Enter section: ")
            marks = input("Enter marks: ")
            students[name] = {
                "section": section,
                "marks": marks
            }
            print(f"{name} added successfully.")
        # Look Up Student
        elif choice == "2":
            name = input("Enter student name to search: ")
            student = students.get(name)
            if student:
                print(f"\nName    : {name}")
                print(f"Section : {student['section']}")
                print(f"Marks   : {student['marks']}")
            else:
                print("Student not found.")
        # Update Student
        elif choice == "3":
            name = input("Enter student name to update: ")
            if name in students:
                new_section = input("Enter new section: ")
                new_marks = input("Enter new marks: ")
                students[name]["section"] = new_section
                students[name]["marks"] = new_marks
                print("Student updated successfully.")
            else:
                print("Student not found.")
        # Delete Student
        elif choice == "4":
            name = input("Enter student name to delete: ")
            if name in students:
                del students[name]
                print("Student deleted successfully.")
            else:
                print("Student not found.")
        # Quit
        elif choice == "5":
            print("Thank you for using the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
# Call the function
student_management()




            

