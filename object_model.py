class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._subjects = []

    def add_subject(self, subject):
        self._subjects.append(subject)

    def get_info(self):
        return f"Имя ученика: {self._name}\nВозраст: {self._age}"

    def get_subjects(self):
        return [subject.get_info() for subject in self._subjects]


class Subject:
    def __init__(self, name):
        self._name = name
        self._grades = []

    def add_grade(self, grade):
        self._grades.append(grade)

    def get_info(self):
        return f"Предмет: {self._name}\nОценка(и): {', '.join(map(str, self._grades))}\n"


class Diary:
    def __init__(self, student):
        self._student = student

    def add_grade(self, subject_name, grade):
        subject = next((s for s in self._student._subjects if s._name == subject_name), None)
        if subject is None:
            subject = Subject(subject_name)
            self._student.add_subject(subject)
        subject.add_grade(grade)

    def get_diary_info(self):
        student_info = self._student.get_info()
        subjects_info = "\n".join(self._student.get_subjects())
        return f"{student_info}\n{subjects_info}"



pupil_1 = Student("Хожиакбар", 17)
pupil_2 = Student("Эльдияр", 18)
pupil_3 = Student("Адиль", 17)

diary_1 = Diary(pupil_1)
diary_2 = Diary(pupil_2)
diary_3 = Diary(pupil_3)

diary_1.add_grade("Системный Инжиниринг", 5)
diary_2.add_grade("Веб-Разработка", 3)
diary_3.add_grade("Машинное обучение", 2)


print(diary_1.get_diary_info())
print(diary_2.get_diary_info())
print(diary_3.get_diary_info())