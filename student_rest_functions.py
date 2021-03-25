def student_edit(gen_dict, chosen_student_number) -> None:
    if chosen_student_number in gen_dict:
        print(f"Wybrałeś: {gen_dict[chosen_student_number]}")
    else:
        print("Student o podanym numerze nie znajduje się na liście!")


def display_student_dict(gen_dict) -> None:
    for student_number in gen_dict:
        print(f"{student_number}. Imię: {gen_dict[student_number][0]}, Nazwisko: {gen_dict[student_number][1]}, "
              f"Data Urodzenia: {gen_dict[student_number][2]}, Numer semestru: {gen_dict[student_number][3]}")
