from student_add_function import name_valid, surname_valid, date_valid, semester_valid


def display_student_dict(gen_dict: dict, chosen_student_number=False) -> None:
    for student_number in gen_dict:
        if chosen_student_number:
            if chosen_student_number == student_number:
                print(f"{student_number}. Imię: {gen_dict[student_number][0]}, Nazwisko: {gen_dict[student_number][1]},"
                      f"Data Urodzenia: {gen_dict[student_number][2]}, Numer semestru: {gen_dict[student_number][3]}")
        else:
            print(f"{student_number}. Imię: {gen_dict[student_number][0]}, Nazwisko: {gen_dict[student_number][1]}, "
                  f"Data Urodzenia: {gen_dict[student_number][2]}, Numer semestru: {gen_dict[student_number][3]}")


def student_edit(gen_dict: dict, data_for_change: str, new_data: str, student_number: str) -> bool:
    chosen_dict = {"Imię": gen_dict[student_number][0], "Nazwisko": gen_dict[student_number][1],
                   "Data Urodzenia": gen_dict[student_number][2], "Numer semestru": gen_dict[student_number][3]}

    student_data = chosen_dict.get(data_for_change, False)

    if student_data in gen_dict[student_number]:

        data_index = gen_dict[student_number].index(student_data)

        valid_func_dict = {0: name_valid, 1: surname_valid, 2: date_valid, 3: semester_valid}

        if data_index in valid_func_dict:
            if data_index <= 2:
                new_data_validate = valid_func_dict[data_index](new_data)
                if new_data_validate:
                    gen_dict[student_number][data_index] = new_data
                    print(f"Zmieniłeś wartość z {student_data} na: {new_data}")
                    return True
            elif data_index == 3:
                date_validate = date_valid(gen_dict[student_number][2])
                new_data_validate = valid_func_dict[data_index](new_data, date_validate)
                if new_data_validate:
                    gen_dict[student_number][data_index] = new_data
                    print(f"Zmieniłeś wartość z '{student_data}' na: '{new_data}'")
                    return True

    else:
        print("\nPodana wartość nie znajduję się w danych studenta!")
        return False
