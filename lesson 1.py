class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(f"Имя: {self.full_name}\nВозраст: {self.age}\nЖенат/Замужем: {self.is_married}")

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks.values()) / len(self.marks) if self.marks else 0

class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus_years = max(0, self.experience - 3)
        return self.base_salary + (self.base_salary * 0.05 * bonus_years)

teacher = Teacher("Зуура Самудировна", 40, True, 10)
teacher.introduce_myself()
print(f"Опыт работы: {teacher.experience} лет")
print(f"Зарплата: {teacher.calculate_salary()} руб.\n")

def create_students():
    student1 = Student("Атай Амангельдиев", 16, False, {"Математика": 3, "История": 4, "Физика": 3})
    student2 = Student("Танай Акматилиев", 17, False, {"Математика": 5, "История": 2, "Физика": 5})
    student3 = Student("Даремет Дербишев", 16, False, {"Математика": 5, "История": 5, "Физика": 5})
    return [student1, student2, student3]
students = create_students()
for student in students:
    student.introduce_myself()
    print("Оценки:")
    for subject, mark in student.marks.items():
        print(f"{subject}: {mark}")
    print(f"Средний балл: {student.calculate_average()}\n")