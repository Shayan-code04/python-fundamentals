class InvalidInputError(Exception):
    """Exception raised for invalid input."""
    pass
class IncorrectMarksError(Exception):
    """Exception raised for incorrect marks."""
    pass

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_grade(self):
        if not isinstance(self.marks, (int,float)):
         raise InvalidInputError("Marks must be a number.")
        elif self.marks < 0 or self.marks > 100:
            raise IncorrectMarksError("Marks must be between 0 and 100.")
        if self.marks>=90: return "A"
        elif self.marks>=80: return "B"
        elif self.marks>=70: return "C"   
        else: return "F"
    def __str__(self):
     return (f"Name: {self.name},"
     F"Roll Number: {self.roll_number},"
     F"Marks: {self.marks},"
     F" Grade: {self.calculate_grade()}" )
     
s1 = Student("Alice", 1, 95)
s2 = Student("Bob", 2, 72)
s3 = Student("Bom", 3, 9)

print(s1)
print(s2)    
print(s3)