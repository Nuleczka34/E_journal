from student_add_function import name_valid, surname_valid, date_valid, semester_valid


def display_student_dict(gen_dict: dict, chosen_student_number=False) -> dict:
    for student_number in gen_dict:
        split_surname = gen_dict[student_number][1].split()

        if chosen_student_number:
            if chosen_student_number == student_number:
                if len(split_surname) == 1:
                    print(f"{student_number}. Imię: {gen_dict[student_number][0]}, Nazwisko: "
                          f"{gen_dict[student_number][1]},Data Urodzenia: {gen_dict[student_number][2]},"
                          f" Numer semestru: {gen_dict[student_number][3]}")

                else:
                    print(f"{student_number}. Imię: {gen_dict[student_number][0]},"
                          f" Nazwisko: {split_surname[0]}-{split_surname[1]}, Data Urodzenia: {gen_dict[student_number][2]},"
                          f" Numer semestru: {gen_dict[student_number][3]}")

                return {"Imię": gen_dict[student_number][0], "Nazwisko": gen_dict[student_number][1],
                        "Data Urodzenia": gen_dict[student_number][2], "Numer semestru": gen_dict[student_number][3]}

        else:
            if len(split_surname) == 1:
                print(f"{student_number}. Imię: {gen_dict[student_number][0]}, Nazwisko: {gen_dict[student_number][1]}"
                      f", Data Urodzenia: {gen_dict[student_number][2]}, Numer semestru: {gen_dict[student_number][3]}")

            else:
                print(f"{student_number}. Imię: {gen_dict[student_number][0]},"
                      f" Nazwisko: {split_surname[0]} - {split_surname[1]}, Data Urodzenia:"
                      f" {gen_dict[student_number][2]}, Numer semestru: {gen_dict[student_number][3]}")


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


def student_search_engine(gen_dict: dict, chose_student_name: str, chose_student_surname: str):
    if chose_student_name and chose_student_surname:

        split_chosen_student_name = chose_student_name.split()
        split_chosen_student_surname = chose_student_surname.split()

        for student_number, student_data_list in gen_dict.items():

            split_student_name = student_data_list[0].split()
            split_student_surname = student_data_list[1].split()

            if len(split_chosen_student_name) == len(split_student_name) \
                    and len(split_chosen_student_surname) == len(split_student_surname):

                for name_index in range(len(split_student_name)):
                    if len(split_student_name) == 1 and split_student_name[name_index] == \
                            split_chosen_student_name[name_index]:

                        for surname_index in range(len(split_student_surname)):
                            if len(split_student_surname) == 1 and split_student_surname[surname_index] == \
                                    split_chosen_student_surname[surname_index]:

                                return student_number

                            elif len(split_student_surname) == 2 and split_student_surname[surname_index - 1] == \
                                    split_chosen_student_surname[surname_index - 1] and \
                                    split_student_surname[surname_index] == split_chosen_student_surname[surname_index]:

                                return student_number

                    elif len(split_student_name) == 2 and split_student_name[name_index - 1] == \
                            split_chosen_student_name[name_index - 1] and split_student_name[name_index] == \
                            split_chosen_student_name[name_index]:

                        for surname_index in range(len(split_student_surname)):
                            if len(split_student_surname) == 1 and split_student_surname[surname_index] == \
                                    split_chosen_student_surname[surname_index]:

                                return student_number

                            elif len(split_student_surname) == 2 and split_student_surname[surname_index - 1] == \
                                    split_chosen_student_surname[surname_index - 1] \
                                    and split_student_surname[surname_index] == \
                                    split_chosen_student_surname[surname_index]:

                                return student_number

        print("\nPodany student nie znajduję się na liście!")
        return False

    else:
        print("\nPodane wartości są błędne!")
        return False
