from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avr_grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in
                self.courses_in_progress and 1 <= grade <= 10):
            lecturer.grades.setdefault(course, []).append(grade)
            lecturer.avr_grades.update(course=mean(lecturer.grades[course]))
        else:
            return 'Ошибка'

    def __str__(self):
        grades = list(*self.grades.values())
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {(0 if len(grades) == 0 else sum(grades) / len(grades))}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}')


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

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.avr_grades}')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress
                and 1 <= grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            grades = list(*student.grades.values())
            student.avr_grade = sum(grades) / len(grades)
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


def avr_students_grade(students, course):
    """ Функция подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
    :param students: список студентов
    :param course: название курса
    :return: средняя оценка
    """
    grades = []
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            grades.append(student.avr_grade)
        else:
            return 'Ошибка'
    return sum(grades) / len(grades)

def avr_lecturers_grade(lecturers, course):
    """ Функция подсчета средней оценки по всем лекторам в рамках конкретного курса
    :param lecturers: список лекторов
    :param course: название курса
    :return: средняя оценка
    """
    grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            grades.append(lecturer.avr_grade)
        else:
            return 'Ошибка'
    return sum(grades) / len(grades)

# Test block data
# ===================================================================================================================

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

# Проверка наследования
print(f'Task 1 results:\n'
      f'---------------')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []
print()

# Проверка атрибутов и взаимодействия классов
print(f'Task 2 results:\n'
      f'---------------')
lecturer = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Василий', 'Васильев')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Ольга', 'Алёхина', 'Ж')
student.courses_in_progress += ['Python', 'Java']
student_2 = Student('Александр', 'Пушкин', 'М')
student_2.courses_in_progress += ['Python']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student_2, 'Python', 8)
print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
print(student_2.rate_lecture(lecturer, 'Python', 6))
print(student_2.rate_lecture(lecturer_2, 'Python', 8))
print(lecturer.grades)  # {'Python': [7]}
print()

# Полиморфизм и магические методы
print(f'Task 3 results:\n'
      f'---------------')
print(student)
print()
print(lecturer)
print()
print(reviewer)
print()

# Функции подсчета средней оценки
print(f'Task 4 results:\n'
      f'---------------')
print(avr_students_grade([student, student_2], 'Python'))
print(avr_lecturers_grade([lecturer, lecturer_2], 'Python'))


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)