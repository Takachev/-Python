tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(next(gen))
print(type(gen))

from itertools import zip_longest

for gen_list in zip_longest(tutors, klasses, fillvalue='None'):
    print(gen_list)
    print(type(gen_list))