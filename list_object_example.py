#/usr/bin/python

# Class #######################################################################
class GradeItem:
    # Call automatically when object is created
    def __init__(self, subject, credit, grade):
        self.subject = subject
        self.credit = credit
        self.grade = grade

    # Call automatically when print() is called
    def __str__(self):
        return 'Subject: %s, Credit: %d, Grade: %d' % (self.subject, self.credit, self.grade)

# Sort function ###############################################################
def sort_dict_by_subject(item):
    return item['subject']

def sort_obj_by_subject(item):
    return item.subject
###############################################################################

items = []

dataType = input('Enter data type (d - dictionary, o - object):')
mode = input('Enter mode (q - quit, a = add, r = remove, s = sort): ')

while mode != 'q':
    if mode == 'a':
        subject = input('Enter subject: ')
        credit = int(input('Enter credit: '))
        grade = int(input('Enter grade: '))

        if dataType == 'd':
            item = { 'subject': subject, 'credit': credit, 'grade': grade } # Dictionary
        else:
            item = GradeItem(subject, credit, grade) # Object

        items.append(item)

    elif mode == 'r':
        subject = input('Enter subject: ')

        if dataType == 'd':
            for item in items:
                if item['subject'] == subject:
                    items.remove(item)
        else:
            for item in items:
                if item.subject == subject:
                    items.remove(item)

    elif mode == 's':
        directon = input('Enter direction (a - ascending, d - descending): ')

        if dataType == 'd':
            items.sort(key=sort_dict_by_subject, reverse=(directon == 'd'))
        else:
            items.sort(key=sort_obj_by_subject, reverse=(directon == 'd'))

    for item in items:
        print(item)

    mode = input('Enter mode (q - quit, a = add, r = remove, s = sort): ')
