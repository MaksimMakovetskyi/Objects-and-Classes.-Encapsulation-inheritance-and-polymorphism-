class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

def rate_lecturer(self, lecturer, course, grade):
    if isinstance (lecturer, Lecturer) \
            and course in lecturer.courses_attached \
            and course in self.courses_in_progress and grade <= 10:
                lecturer.grades += [grade]
            else:
                return 'Oшибкa'

    def get_avg_grade(self):
        if self.grades:
        sum_hw = 0
        count = 0
        for grades in self.grades.values():
            sum_hw += sum(grades)
            count += len(grades)
        return round(sum_hw / count, 2)
    else:


    def __str(self):
        res = f'Имя: {self.name} \n'\
              f' Фамилия: {self.surname} \n'\
              f'Средняя оценка sа дз: {(self.get_avg_grade()} \n'
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print(' Такого студента нет ')
            return
        else:
            compare = self.get_avg_grade() < other_student.get_avg_grade()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{other_student.name} {other_student.surname} учится хуже, чem {self.name} {self.surname}')
        return compare


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []


    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f' Фамилия: {self.surname} \n' \
              f'Средняя оценка sа дз: {sum(self.grades) / len(self.grades) :.2f} \n'
        return res

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(coll_lecturer > next_lecturer)

def get_avg_hw_grade(student_list, course):
    total_sum = 0

    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
            total_sum += sum(grades) / len(grades)
    return round(total_sum / len(student_list), 2)

print(get_avg_hw_grade([best_student, next_student], 'Python'))

def get_avg_lect_grade(list_lect):
    total_sum = 0
    for lecturer in list_lect:
        total_sum += sum(lecturer.grades) / len(lecturer.grades)
        return total_sum / len(list_lect)


print (get_avg_lect_grade([cool_lecturer, next_lecturer])