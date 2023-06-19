list=[]
dict={'subject':'unknown','credit':0,'grade':0}
Ask=input("Add for subject?(Yes/No):")
while(Ask=="Yes"):
    subject=input("select your subject")
    credit=int(input('Your credict:'))
    grade=int(input('your grade:'))
    dict['subject']=subject
    dict['credit']=credit
    dict['grade']=grade
    list.append(dict)
    Ask=input("Do you want to add more subject?(Yes/No):")
    list2={'subject':subject,'credit':credit,'grade':grade}
    list.append(list2)
Change=input("Do you want to change your grade?(Yes/No):")
while(Change=="Yes"):
   Subject=input('Enter your subject:')
   dict['subject']=Subject
   Grade=int(input("Your new grade?:"))
   dict['grade']=Grade
   print("Subject",dict['subject'])
   print("Grade",dict['grade'])
