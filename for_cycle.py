DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    for worker in DATA:
        print(worker)


if __name__=='__main__':
    run()

#Filtrado de empleados que saben python

print("Empleados que saben programar en python")

print('**********Metodo tradicional**********')
all_python_workers = []

for python_worker in DATA:
    if python_worker['language'] == 'python':
        all_python_workers.append(python_worker['name'])
print(all_python_workers)


print("**********Metodo con list comprehensions**********")
all_python_workers_2 = [worker['name'] for worker in DATA if worker['language'] == 'python']
print(all_python_workers_2)


print("**********Metodo con filter y map**********")

all_python_workers_3 = list(filter(lambda worker : worker['language'] == 'python',DATA))
all_python_workers_3 = list(map(lambda worker : worker['name'],all_python_workers_3))
print(all_python_workers_3)