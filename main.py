from studentfunction import add_student


students_dict = {}
flag = True
index = 1

# TODO: ZRÓB MENU GŁÓWNE
while flag:
    student_adding = add_student(students_dict, index)
    if student_adding:
        index += 1
        print(students_dict)
