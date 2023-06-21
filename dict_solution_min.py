#/usr/bin/python

subjects = []
grades = []

mode = input('Enter mode (q - quit, a = add): ')

while mode != 'q':
    if mode == 'a':
        subject = input('Enter subject: ')
        grade = int(input('Enter grade: '))
        
        subjects.append(subject)
        grades.append(grade)

    for subject in subjects:
        print(subject)
        
    for grade in grades:
        print(grade)

    mode = input('Enter mode (q - quit, a = add): ')
    if mode == 'q':
        res_dict = dict(zip(subjects, grades))
        print(res_dict)
        print('Subject that has minimum score: ', min(res_dict, key=res_dict.get))
        print('Subject that has maximum score: ', max(res_dict, key=res_dict.get))
