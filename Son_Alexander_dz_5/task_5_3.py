from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

pupils = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses, fillvalue=None))

for i in pupils:
    print(i)
