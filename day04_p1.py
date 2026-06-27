def add_student(students, name, student_class, grade):
    """Add one student record and return the updated list."""
    students.append({"name": name, "class": student_class, "grade": grade})
    return students

def remove_student(students, name):
    """Remove a student by name and return the updated list."""
    return [s for s in students if s["name"] != name]

def class_average(students):
    """Return the average grade across all students."""
    return sum(s["grade"] for s in students) / len(students)

def print_roster(students):
    """Print all students with position numbers."""
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']} - {s['class']} - {s['grade']}")

students = []

while True:
    name = input("Enter student's name: ")
    student_class = input("Enter student's class: ")
    grade = float(input("Enter student's grade: "))
    add_student(students, name, student_class, grade)

    more = input("Add another student? (yes/no): ")
    if more.lower() != "yes":
        break

print_roster(students)
print("Class average:", class_average(students))

remove = input("Remove a student? (yes/no): ")
if remove.lower() == "yes":
    name_to_remove = input("Enter name to remove: ")
    students = remove_student(students, name_to_remove)
    print_roster(students)