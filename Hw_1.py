# 1. Создать класс Person с атрибутами full_name, age, is_married
# 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
# 3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.
# 4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
# 5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
# 6. Добавить в класс Teacher атрибут уровня класса base_salary.
# 7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к базовой зарплате прибавляется бонус 5% за каждый год опыта свыше 3-х лет.
# 8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
# 9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.
# 10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.

class Person:
    def __init__(self, full_name, age, is_married):
        self.ful_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Full_name:{self.ful_name} Age:{self.age} Is_married:{self.is_married}')

class Student(Person):
    def __init__(self,full_name, age, is_married,marks:dict):
        super().__init__(full_name,age,is_married)
        self.marks = marks
    def average_ratings(self,):
        return sum(self.marks.values())/len(self.marks)

class Teacher(Person):
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name,age,is_married)
        self.experience = experience
    base_salary = 30000
    def calculator(self):
        bonus_year = max(0,self.experience - 3)
        return self.base_salary + (self.base_salary * bonus_year * 0.05)

Maria = Teacher('Maria Ivanovna', 35,'Yes',10)
Maria.introduce_myself()
print(f'Experience:{Maria.experience}')
print(f'Salary:{Maria.calculator()}')

def create_students():
    student_1 = Student('Atay','15',"No",{'Physics':3,'Math':3,'Music':5})
    student_2 = Student('Tanay', '15', "No", {'Physics': 5, 'Math': 5, 'Music': 4})
    student_3 = Student('Daremet', '15', "No", {'Physics': 4, 'Math': 5, 'Music': 3})
    return [student_1,student_2,student_3]
students = create_students()
for student in students:
    student.introduce_myself()
    print("Оценки:")
    for subject, mark in student.marks.items():
        print(f"{subject}: {mark}")
    print(f"Средний балл: {round(student.average_ratings(),2)}")