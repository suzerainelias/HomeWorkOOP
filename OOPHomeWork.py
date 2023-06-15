class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grades(self):
        giga_result = []
        for a in self.grades:
            result = sum(self.grades[a]) / len(self.grades[a])
            giga_result += [result]
        if len(self.grades) == 0:
            print('На нуль делить нельзя!')
            return
        giga_result_sum = sum(giga_result) / len(self.grades)
        return giga_result_sum
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {round(self.avg_grades(), 1)} ' \
              f'\nКурсы в процессе: {self.courses_in_progress} \nЗавершённые курсы:{self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.avg_grades() < other.avg_grades()
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия = {self.surname}'
        return res


class Lecturer(Mentor):
    grades = {}

    def avg_grades(self):
        giga_result = []
        for a in self.grades:
            result = sum(self.grades[a]) / len(self.grades[a])
            giga_result += [result]
        if len(self.grades) == 0:
            print('На нуль делить нельзя!')
            return
        giga_result_sum = sum(giga_result) / len(self.grades)
        return giga_result_sum


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.avg_grades() < other.avg_grades()


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname} \nСредняя оценка за пройденный курс: {self.avg_grades()}'
        return res

def global_rate_hw(students, course):
    new_list=[]
    for a in students:
        if course in a.grades:
            result = sum(a.grades[course]) / len(a.grades[course])
            new_list.append(result)
    if len(new_list) == 0:
        print('На нуль делить нельзя!')
        return
    avg_new_list = sum(new_list) / len(new_list)
    return avg_new_list

def global_rate_lecturer(lecturers, course):
    new_list=[]
    for a in lecturers:
        if course in a.grades:
            result = sum(a.grades[course]) / len(a.grades[course])
            new_list.append(result)
    if len(new_list) == 0:
        print('Ошибка ввода')
        return
    avg_new_list = sum(new_list) / len(new_list)
    return avg_new_list


students = [Student('Joffrey', 'Bombita', 'your_gender'), Student('Jandarm', 'Makuta', 'your_gender')]
students[0].courses_in_progress += ['Python', 'Git']
students[1].courses_in_progress += ['HandMade', 'ValheimBuildings']
students[0].finished_courses += ['GigaChad', 'MegaGigaChad']
students[1].finished_courses += ['YellowLeavesHouse', 'RacismForDevelopers']


lecturers = [Lecturer('Antonio', 'Margaretti'), Lecturer('SpongeBob', 'SquarePants')]
lecturers[0].courses_attached += ['Python', 'Git', 'HandMade']
lecturers[1].courses_attached += ['HandMade', 'ValheimBuildings', 'Python']

reviewers = [Reviewer('Bibigul', 'Grossmaster'), Reviewer('Hookah', 'NoNirvana')]
reviewers[0].courses_attached += ['Python', 'Git']
reviewers[1].courses_attached += ['HandMade', 'ValheimBuildings']

mentors = [Mentor('Stephano', 'Adagio'), Mentor('Sosageo', 'Lolita Grossman')]
mentors[0].courses_attached += ['Python', 'Git']
mentors[1].courses_attached += ['HandMade', 'ValheimBuildings']

students[1].rate_lecturer(lecturers[0], 'HandMade', 3)
students[0].rate_lecturer(lecturers[1], 'Python', 4)
students[1].rate_lecturer(lecturers[1], 'ValheimBuildings', 5)

reviewers[0].rate_hw(students[0], 'Python', 4)
reviewers[1].rate_hw(students[1], 'HandMade', 5)



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']



some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(best_student, 'Python', 9)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)



some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(some_lecturer, 'Python', 5)
best_student.rate_lecturer(some_lecturer, 'Python', 4)
best_student.rate_lecturer(some_lecturer, 'Python', 2)
best_student.rate_lecturer(some_lecturer, 'Python', 6)
best_student.rate_lecturer(some_lecturer, 'Python', 1)

students.append(best_student)
reviewers.append(some_reviewer)
lecturers.append(some_lecturer)

print(global_rate_hw(students, 'Python'))

print(global_rate_lecturer(lecturers, 'Python'))

print(some_lecturer < some_lecturer)

print(best_student.grades)
print('-------------')
print(some_reviewer)
print('-------------')
print(some_lecturer)
print('-------------')
print(best_student)
print(best_student < best_student)