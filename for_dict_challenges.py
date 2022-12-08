# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

from collections import Counter

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
list_of_students = [
    person['first_name']
    for person in students
]
list_of_quantity_student_names = Counter(list_of_students)
for student in list_of_quantity_student_names:
    print(f'{student}: {list_of_quantity_student_names[student]}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
list_of_students = [
    person['first_name']
    for person in students
]
most_common_name = Counter(list_of_students).most_common(1)
print(f'Самое частое имя среди учеников: {most_common_name[0][0]}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for number, student_class in enumerate(school_students, start=1):
    list_of_students = [
        person['first_name']
        for person in student_class
    ]
    most_common_name = Counter(list_of_students).most_common(1)    
    print(f'Самое частое имя в классе {number}: {most_common_name[0][0]}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for student_class in school:
    class_name = student_class['class']
    list_of_students = [
        person['first_name']
        for person in student_class['students']
    ]
    boys_in_class = [
        name for name in list_of_students
        if name in is_male and is_male[name]
    ]
    girls_in_class = [
        name for name in list_of_students
        if name in is_male and not is_male[name]
    ]
    print(f'Класс {class_name}: девочки {len(girls_in_class)}, мальчики {len(boys_in_class)}')


# Задание 5
# По информации об учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

MALE = 0    #Илья, я применил тут глобальные переменные. Насколько это здесь уместно? 
FEMALE = 0  #Я привык работать со сдвиговыми регистрами (логика ПЛИСов, например), поэтому подход с глобальной переменной мне понятен
            #Но может есть более правильный способ решения?
for student_class in school:
    class_name = student_class['class']
    quantity_male = 0
    quantity_female = 0
    list_of_students = [
        person['first_name']
        for person in student_class['students']
    ]
    quantity_male = 0
    quantity_female = 0
    for person in list_of_students:
        if person in is_male and is_male[person]:
            quantity_male += 1
        elif person in is_male and not is_male[person]:
            quantity_female += 1
        if quantity_male > MALE:
            MALE = quantity_male
            class_male = class_name
        if quantity_female > FEMALE:
            FEMALE = quantity_female
            class_female = class_name
print(f'Больше всего девочек в классе {class_female}')
print(f'Больше всего мальчиков в классе {class_male}')