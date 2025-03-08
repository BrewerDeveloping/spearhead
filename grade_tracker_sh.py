class Student:
    def __init__(self, name, f_name, int):
        self.name = name
        self.f_name = f_name
        self.int = int

    def __repr__(self):
        return f"{self.name} {self.f_name}, Grade: {self.int}"


class Classroom:
    def __init__(self):
        self.students = []

    def addStudent(self, name, f_name, int):
        new_student = Student(name, f_name, int)
        self.students.append(new_student)

    def getHighestGrade(self):
        return max(student.int for student in self.students)

    def getLowestGrade(self):
        return min(student.int for student in self.students)

    def getAllStudents(self):
        return self.students


# Creating an instance of Classroom
classroom = Classroom()

# Adding students
classroom.addStudent("Name:", "John", 85)
classroom.addStudent("Name:", "Alice", 92)
classroom.addStudent("Name:", "Bob", 78)
classroom.addStudent("Name:", "Carol", 88)
classroom.addStudent("Name:", "Dave", 72)

# Displaying all students
all_students = classroom.getAllStudents()
print("Students in the classroom:")
for student in all_students:
    print(student)

# Reporting highest and lowest grades
highest_grade = classroom.getHighestGrade()
lowest_grade = classroom.getLowestGrade()

print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")
