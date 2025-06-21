""" Домашнее задание к лекции «Объекты и классы. Инкапсуляция, наследование и полиморфизм»
"""

from statistics import mean


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}
        self.avr_grades = {}
        self.overall_avr_grade = 0

    def rate_lecture(self, lecturer, course, grade):
        """ Метод выставления оценок лекторам (по 10-балльной шкале) """
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in
                self.courses_in_progress and (1 <= grade <= 10)):
            lecturer.grades.setdefault(course, []).append(grade)
            lecturer.avr_grades.update({course: mean(lecturer.grades[course])})
            lecturer.overall_avr_grade = mean(list(lecturer.avr_grades.values()))
        else:
            return 'Ошибка'

    def finish_course(self, course):
        """ Метод, завершающий изучение курса """
        if course not in self.courses_in_progress:
            return 'Ошибка'
        self.courses_in_progress.remove(course)
        self.finished_courses.append(course)
        return f'Студент {self.name} {self.surname} завершил(а) курс {course}\n'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.overall_avr_grade}\n'
                f'Курсы в процессе изучения: '
                f'{', '.join(self.courses_in_progress) if self.courses_in_progress else 'нет'}\n'
                f'Завершенные курсы: '
                f'{', '.join(self.finished_courses) if self.finished_courses else 'нет'}\n')

    def __eq__(self, other):
        return self.overall_avr_grade == other.overall_avr_grade

    def __ne__(self, other):
        return self.overall_avr_grade != other.overall_avr_grade

    def __lt__(self, other):
        return self.overall_avr_grade < other.overall_avr_grade

    def __le__(self, other):
        return self.overall_avr_grade <= other.overall_avr_grade

    def __gt__(self, other):
        return self.overall_avr_grade > other.overall_avr_grade

    def __ge__(self, other):
        return self.overall_avr_grade >= other.overall_avr_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avr_grades = {}
        self.overall_avr_grade = 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.overall_avr_grade}\n')

    def __eq__(self, other):
        return self.overall_avr_grade == other.overall_avr_grade

    def __ne__(self, other):
        return self.overall_avr_grade != other.overall_avr_grade

    def __lt__(self, other):
        return self.overall_avr_grade < other.overall_avr_grade

    def __le__(self, other):
        return self.overall_avr_grade <= other.overall_avr_grade

    def __gt__(self, other):
        return self.overall_avr_grade > other.overall_avr_grade

    def __ge__(self, other):
        return self.overall_avr_grade >= other.overall_avr_grade


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """ Метод выставления оценок студентам за домашние задания по 5-балльной шкале (от 2 до 5) """
        if (isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress
                and 2 <= grade <= 5):
            student.grades.setdefault(course, []).append(grade)
            student.avr_grades.update({course: mean(student.grades[course])})
            student.overall_avr_grade = mean(list(student.avr_grades.values()))
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')


def avr_students_grade(students, course):
    """ Функция подсчета средней оценки по всем студентам в рамках конкретного курса """
    if not all(map(lambda x: isinstance(x, Student), students)):
        return 'Ошибка'
    grades = [person.avr_grades[course] for person in students
              if course in (person.courses_in_progress + person.finished_courses) and course in person.avr_grades]
    return f'{course}, студенты: {f'средняя оценка {mean(grades)}' if grades else 'оценок нет'}'


def avr_lecturers_grade(lecturers, course):
    """ Функция подсчета средней оценки по всем лекторам в рамках конкретного курса """
    if not all(map(lambda x: isinstance(x, Lecturer), lecturers)):
        return 'Ошибка'
    grades = [person.avr_grades[course] for person in lecturers
              if course in person.courses_attached and course in person.avr_grades]
    return f'{course}, лекторы: {f'средняя оценка {mean(grades)}' if grades else 'оценок нет'}'


# Блок тестов
# ==================================================================================================

lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Василий', 'Васильев')
reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Геннадий', 'Кочкин')
student_1 = Student('Ольга', 'Алёхина')
student_2 = Student('Александр', 'Пушкин')

print(f'Проверка наследования:\n'
      f'----------------------')
print(isinstance(lecturer_1, Mentor))  # True
print(isinstance(reviewer_2, Mentor))  # True
print(lecturer_2.courses_attached)  # []
print(reviewer_1.courses_attached)  # []
print()

print(f'Проверка атрибутов, методов и взаимодействия классов:\n'
      f'-----------------------------------------------------')
student_1.courses_in_progress += ['C++', 'Python', 'Java']
student_2.courses_in_progress += ['Python']
lecturer_1.courses_attached += ['C++', 'Python']
lecturer_2.courses_attached += ['Java']
reviewer_1.courses_attached += ['Python', 'C++']
reviewer_2.courses_attached += ['Java', 'Python']
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)

print(student_1.rate_lecture(lecturer_1, 'Python', 7))  # None
print(lecturer_1.avr_grades)  # {'Python': 7}
print(student_2.rate_lecture(lecturer_2, 'Java', 8))  # Ошибка
print(student_1.rate_lecture(lecturer_1, 'Java', 8))  # Ошибка
print(student_1.rate_lecture(lecturer_2, 'C++', 5))  # Ошибка
print(student_1.rate_lecture(lecturer_1, 'C++', 3))  # None
print(student_1.rate_lecture(lecturer_2, 'Java', 4))  # None
print(student_2.rate_lecture(lecturer_1, 'Python', 6))  # None
print(lecturer_1.grades)  # {'Python': [7, 6], 'C++': [3]}
print(lecturer_1.avr_grades)  # {'Python': 6.5, 'C++': 3}
print(student_1.rate_lecture(lecturer_2, 'С++', 11))  # Ошибка
print(lecturer_2.grades)  # {'Java': [4]}
print(lecturer_2.avr_grades)  # {'Java': 4}
print(student_1.rate_lecture(reviewer_1, 'Python', 6))  # Ошибка
print(reviewer_1.rate_hw(student_1, 'Python', 10))  # Ошибка
print(reviewer_1.rate_hw(student_1, 'Python', 5))  # None
print(reviewer_1.rate_hw(student_1, 'Java', 4))  # Ошибка
print(reviewer_2.rate_hw(student_1, 'Java', 4))  # None
print(reviewer_2.rate_hw(student_1, 'Python', 4))  # None
print(reviewer_2.rate_hw(student_2, 'Python', 2))  # None
print(student_1.grades)  # {'Python': [5, 4], 'Java': [4]}
print(student_1.avr_grades)  # {'Python': 4.5, 'Java': 4}
print(student_2.grades)  # {'Python': [2]}
print(student_2.avr_grades)  # {'Python': 2}
print()

print(avr_students_grade([student_1, student_2], 'Python'))  # Python: средняя оценка 3.25
print(student_1.finish_course('Java'))  # Студент Ольга Алёхина завершил(а) курс Java
# После завершения курса средняя оценка должна остаться прежней:
print(avr_students_grade([student_1, student_2], 'Python'))  # Python: средняя оценка 3.25
print(avr_students_grade([student_2], 'JavaJava'))  # JavaJava, студенты: оценок нет
print(avr_students_grade([student_1], 'C++'))  # C++, студенты: оценок нет
print(avr_students_grade([student_1, student_2], 'Java'))  # Java, студенты: средняя оценка 4
print(avr_lecturers_grade([lecturer_2], 'Java'))  # Java, лекторы: средняя оценка 4
print(avr_students_grade([lecturer_1], 'Java'))  # Ошибка
print(avr_lecturers_grade([lecturer_2, student_2], 'Java'))  # Ошибка
print()

print(f'Проверка перегрузки dunder-методов (Ad-hoc полиморфизм):\n'
      f'--------------------------------------------------------')
print(f'Студенты:\n'
      f'---------', student_2, student_1, sep='\n')
print(student_1.finish_course('Python'))  # Студент Ольга Алёхина завершил(а) курс Python
print(student_1)
print(f'Проверяющие:\n'
      f'------------', reviewer_1, reviewer_2, sep='\n')
print(f'Лекторы:\n'
      f'--------', lecturer_1, lecturer_2, sep='\n')

print(f'Сравнение оценок:\n'
      f'-----------------')
print(f'{student_1.overall_avr_grade} == {student_2.overall_avr_grade} {student_1 == student_2}')  # False
print(f'{student_1.overall_avr_grade} > {student_2.overall_avr_grade} {student_1 > student_2}')  # True
print(f'{student_1.overall_avr_grade} >= {student_2.overall_avr_grade} {student_1 >= student_2}')  # True
print(f'{student_1.overall_avr_grade} < {student_2.overall_avr_grade} {student_1 < student_2}')  # False
print(f'{student_1.overall_avr_grade} <= {student_2.overall_avr_grade} {student_1 <= student_2}')  # False
print(f'{student_1.overall_avr_grade} != {student_2.overall_avr_grade} {student_1 != student_2}')  # True
print()
print(f'{lecturer_1.overall_avr_grade} == {lecturer_2.overall_avr_grade} {lecturer_1 == lecturer_2}')  # False
print(f'{lecturer_1.overall_avr_grade} > {lecturer_2.overall_avr_grade} {lecturer_1 > lecturer_2}')  # True
print(f'{lecturer_1.overall_avr_grade} >= {lecturer_2.overall_avr_grade} {lecturer_1 >= lecturer_2}')  # True
print(f'{lecturer_1.overall_avr_grade} < {lecturer_2.overall_avr_grade} {lecturer_1 < lecturer_2}')  # False
print(f'{lecturer_1.overall_avr_grade} <= {lecturer_2.overall_avr_grade} {lecturer_1 <= lecturer_2}')  # False
print(f'{lecturer_1.overall_avr_grade} != {lecturer_2.overall_avr_grade} {lecturer_1 != lecturer_2}')  # True
print()

# Также можно сравнить оценки студента и лектора. И хотя это не совсем правильно, я не стал добавлять проверку на
# соответствие типов объектов во все магические методы.
print(f'{student_1.overall_avr_grade} == {lecturer_1.overall_avr_grade} {student_1 == lecturer_1}')  # False

# А вот такое сравнение не пройдет, потому что у проверяющих нет оценок и соответствующего атрибута
# для их среднего значения:
# print(student_1 == reviewer_2)
