import csv
def write_csv_file(file_path,student):
    filednames=["name","section","marks"]
    with open(file_path,mode="w") as f:
        writer=csv.DictWriter(f,fieldnames=filednames)
        writer.writeheader()
        for student in student:
            writer.writerow(student)

def read_csv_file(file_path):
    with open(file_path,mode="r",newline="")as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
    
  
def print_students(students):
    """
    Print student records in a readable format.

    Parameters:
        students (list of dict): student records to print.
    """
    for s in students:
        print(f"Name: {s['name']}, section: {s['section']}, Marks: {s['marks']}")


if __name__ == "__main__":
    filepath = "students.csv"

    sample_students = [
        {"name": "pey", "section": 101, "marks": 88},
        {"name": "Ravi", "section": 102, "marks": 76},
        {"name": "Meena", "section": 103, "marks": 92},
    ]

    write_csv_file(filepath, sample_students)
    loaded_students = read_csv_file(filepath)
    print_students(loaded_students)
        



