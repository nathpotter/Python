#/usr/bin/python

items = []

mode = input('Enter mode (q - quit, a = add, r = remove): ')

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

    for item in items:
        print(item)

    mode = input('Enter mode (q - quit, a = add, r = remove, s = sort): ')
