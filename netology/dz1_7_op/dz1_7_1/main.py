
# Исходя из квиза к предыдущему занятию,
# у нас уже есть класс преподавателей и класс студентов
# (вы можете взять этот код за основу или написать свой).
# Студентов пока оставим без изменения, а вот преподаватели бывают разные,
# поэтому теперь класс Mentor должен стать родительским классом,
# а от него нужно реализовать наследование классов Lecturer (лекторы) и
# Reviewer (эксперты, проверяющие домашние задания). Очевидно, имя, фамилия
# и список закрепленных курсов логично реализовать на уровне родительского класса.
# А чем же будут специфичны дочерние классы? Об этом в следующих заданиях.
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Lecturer):
    def __init__(self):
        self.name = name
        self.surname = surname
        self.courses_attached = []


