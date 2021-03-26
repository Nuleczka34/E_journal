from student_add_function import name_valid, surname_valid, date_valid, semester_valid


def display_student_dict(gen_dict: dict, chosen_student_number=False) -> None:
    for student_number in gen_dict:
        if chosen_student_number:
            if chosen_student_number == student_number:
                print(f"{student_number}. Imię: {gen_dict[student_number][0]}, Nazwisko: {gen_dict[student_number][1]}, "
                      f"Data Urodzenia: {gen_dict[student_number][2]}, Numer semestru: {gen_dict[student_number][3]}")
        else:
            print(f"{student_number}. Imię: {gen_dict[student_number][0]}, Nazwisko: {gen_dict[student_number][1]}, "
                  f"Data Urodzenia: {gen_dict[student_number][2]}, Numer semestru: {gen_dict[student_number][3]}")


def student_edit(gen_dict: dict, chosen_data_for_change: str, new_data: str, student_number: str) -> dict or bool:
    if student_number in gen_dict:
        for student_data_list in gen_dict.values():
            if chosen_data_for_change in student_data_list:
                data_index = student_data_list.index(chosen_data_for_change)
                valid_func_dict = {0: name_valid, 1: surname_valid, 2: date_valid, 3: semester_valid}

                for func_number in valid_func_dict:
                    if func_number <= 2 and func_number == data_index:
                        new_data_validate = valid_func_dict[func_number](new_data)
                        if new_data_validate:
                            gen_dict[student_number][data_index] = new_data

                    elif func_number == 3 and func_number == data_index:
                        date_validate = date_valid(student_data_list[2])

                        new_data_validate = valid_func_dict[func_number](new_data, date_validate)

                        if new_data_validate:
                            gen_dict[student_number][data_index] = new_data

                            return gen_dict

                        else:
                            return False

    else:
        print("\nPodana wartość nie znajduję się w danych studenta!")
        return False




