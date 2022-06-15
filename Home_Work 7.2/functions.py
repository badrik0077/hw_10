import json


def load_json(filename):
    with open(filename) as f:
        return json.load(f)


def load_students():
    """загружает студентов из файла 'students.json' в список """
    return load_json('students.json')


def load_professions():
    """" загружает навыки из файла 'professions.json' в список"""
    return load_json('professions.json')


def get_student_by_pk(pk):
    """получает словарь с данными студента по его pk"""
    for student in load_students():
        if student["pk"] == pk:
            return student


def get_profession_by_title(title):
    """ Получает словарь с инфо о профе по названию"""
    for profession in load_professions():
        if profession["title"] == title:
            return profession


def check_fitness(student, profession):
    """получив студента и профессию, возвращает словарь типа"""
    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])
    has_skill = student_skills.intersection(profession_skills)   #В обеих множествах  является общим элементом. То же самое может быть достигнуто при использовании метода intersection():
    laks_skill = profession_skills.difference((has_skill))     #Для определения разницы между множествами в Python, мы можем использовать как функцию difference()
    has_percent = round(len(has_skill)/len(profession_skills)*100)
    student_professional_skill = {"has": list(has_skill), "laks": list(laks_skill), "fit_percent": has_percent}
    return student_professional_skill
