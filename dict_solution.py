#/usr/bin/python

items = []

mode = input('Enter mode (q - quit, a = add, r = remove, s = sort): ')

while mode != 'q':
    if mode == 'a':
        subject = input('Enter subject: ')
        credit = int(input('Enter credit: '))
        grade = int(input('Enter grade: '))

        item = { 'subject': subject, 'credit': credit, 'grade': grade } # Dictionary

        items.append(item)

    elif mode == 'r':
        subject = input('Enter subject: ')

        for item in items:
            if item['subject'] == subject:
                items.remove(item)

    elif mode == 's':
        directon = input('Enter direction (a - ascending, d - descending): ')
        items.sort(key=sort_dict_by_subject, reverse=(directon == 'd'))

    for item in items:
        print(item)

    mode = input('Enter mode (q - quit, a = add, r = remove, s = sort): ')
