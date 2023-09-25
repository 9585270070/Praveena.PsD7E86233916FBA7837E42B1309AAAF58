def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


# Define a Student class
class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


# Test the function
if __name__ == "__main__":
  students = [
      Student("Alice", "A001", 3.9),
      Student("Bob", "B002", 3.7),
      Student("Charlie", "C003", 4.0),
      Student("David", "D004", 3.8),
  ]

  sorted_students = sort_students(students)

  for student in sorted_students:
    print(
        f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}"
    )
