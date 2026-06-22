
#example of if and else statement

'''marks = int(input("enter your marks: "))
if marks>=35:
    print("you got passing grades")
else:
    print("Sorry you got fail")'''

#example of nested if statement
name_1='Raj'
name_2='Chakilam'
course='ISTQB'
marks_1=int(input('enter the marks :'))
marks_2=int(input('enter the marks :'))
if course == 'ISTQB':
    if name_1 == 'Raj':
        print('Raj of course marks got :', marks_1)
    if name_2 == 'Chakilam':
        print('Chakilam got the marks :',marks_2)
