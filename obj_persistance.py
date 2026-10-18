import pickle
import shelve
# Define a Student class
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)

# Create student objects
s1 = Student("Aditya", 101, 95)
s2 = Student("Khushi", 102, 67)

students = [s1, s2]

# Save objects using pickle
with open("students.pkl", "wb") as file:
    pickle.dump(students, file)

print("Objects saved using pickle.")

# Restore objects using pickle
with open("students.pkl", "rb") as file:
    loaded_students = pickle.load(file)

print("\nRestored Objects:")
for student in loaded_students:
    student.display()
    print()

# Save objects using shelve
with shelve.open("student_data") as database:
    database["student1"] = s1
    database["student2"] = s2

print("Objects saved using shelve.")

# Restore objects using shelve
with shelve.open("student_data") as database:
    print("\nObjects restored using shelve:")

    for key in database:
        student = database[key]
        student.display()
        print()
