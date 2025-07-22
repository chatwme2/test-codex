class Student:
    """Represents a student and their list of grades."""

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calc_average(self):
        """Return the average grade for the student."""
        if not self.grades:
            return 0
        total = sum(self.grades)
        average = total / len(self.grades)
        return average

    def has_passed(self):
        """Return a string describing if the student passed."""
        if self.calc_average() >= 60:
            return "Passed"
        else:
            return "Failed"

def get_student_data():
    students = []
    while True:
        name = input("Enter student name (or type 'done' to stop): ")
        if name.lower() == "done":
            break
        grades_input = input("Enter grades separated by commas: ")
        grades = [int(g) for g in grades_input.split(",")]
        student = Student(name, grades)
        students.append(student)
    return students

def display_summary(students):
    print("\n=== Student Report ===")
    for s in students:
        print(f"Name: {s.name}")
        print("Grades:", s.grades)
        print("Average:", s.calc_average())
        print("Result:", s.has_passed())
        print("-----------")

def main():
    students = get_student_data()
    display_summary(students)

if __name__ == "__main__":
    main()
