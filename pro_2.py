class Tutor:
    def __init__(self, tutor_id, name, subject):
        self.tutor_id = tutor_id
        self.name = name
        self.subject = subject

    def display(self):
        print(f"Tutor ID: {self.tutor_id}")
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")


class OnlineTutoringSystem:
    def __init__(self):
        self.tutors = []
        self.students = []

    def add_tutor(self):
        tutor_id = input("Enter Tutor ID: ")
        name = input("Enter Tutor Name: ")
        subject = input("Enter Subject: ")
        self.tutors.append(Tutor(tutor_id, name, subject))
        print("Tutor added successfully!\n")

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        self.students.append(Student(student_id, name))
        print("Student added successfully!\n")

    def view_tutors(self):
        if not self.tutors:
            print("No tutors available.\n")
        else:
            print("\nTutor List")
            for tutor in self.tutors:
                tutor.display()
                print()

    def view_students(self):
        if not self.students:
            print("No students registered.\n")
        else:
            print("\nStudent List")
            for student in self.students:
                student.display()
                print()


system = OnlineTutoringSystem()

while True:
    print("\n--- Online Tutoring System ---")
    print("1. Add Tutor")
    print("2. Add Student")
    print("3. View Tutors")
    print("4. View Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        system.add_tutor()
    elif choice == '2':
        system.add_student()
    elif choice == '3':
        system.view_tutors()
    elif choice == '4':
        system.view_students()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
