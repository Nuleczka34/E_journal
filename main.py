from student_add_function import json_decorator, student_add
from student_rest_functions import student_edit, display_student_dict, student_search_engine
from logging import basicConfig, DEBUG, exception

basicConfig(filename="logging.log", level=DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


@json_decorator
def main(students_dict: dict) -> dict:
    index = students_dict.get("index", 1)
    if "index" in students_dict:
        students_dict.pop("index")

    flag = True

    while flag:
        print('''\n1. Wyświetl Listę
2. Dodaj studenta
3. Usuń studenta
4. Edytuj studenta
5. Wyświetl oceny
6. Dodaj oceny
7. Edytuj oceny
8. Zakończ program
              ''')

        chosen_option = input("Wybierz numer operacji z listy: ").strip()
        try:
            if int(chosen_option) in range(1, 8):
                menu_dict = {'1': ("Wyświetlanie listy", display_student_dict),
                             '2': ("Dodawanie studenta", student_add),
                             '3': ("Usuwanie studenta", "student_delete"),  # TODO: USUWANIE STUDENTA
                             '4': ("Edycja studenta", student_edit),
                             '5': ("Wyświetlanie ocen", "display_student_note"),  # TODO: WYŚWIETLANIE OCEN
                             '6': ("Dodawanie ocen", """student_note_add"""),  # TODO: DODAWANIE OCEN
                             '7': ("Edycja ocen", "student_note_edit")}  # TODO: EDYCJA OCEN

                menu_result, menu_chosen_func = menu_dict.get(chosen_option)

                try:
                    print(f"\nWybrałeś '{menu_result}'\n")

                    if menu_result == "Wyświetlanie listy":
                        menu_chosen_func(students_dict)

                    elif menu_result == "Dodawanie studenta":
                        student_name = input("Podaj imię(imiona) [Imię/ Imię Imię]: ")
                        student_surname = input("Podaj nazwisko(nazwiska) [Nazwisko/ Nazwisko Nazwisko]: ")
                        student_birthdate = input("Podaj datę urodzenia[dd.mm.yyyy]: ")
                        student_semester = input("Podaj obecny semestr [1 - 12]: ")

                        adding_student = menu_chosen_func(students_dict, index, student_name, student_surname,
                                                          student_birthdate, student_semester)
                        if adding_student:
                            index += 1

                    elif menu_result == "Usuwanie studenta":
                        pass
                        # menu_chosen_func()

                    elif menu_result == "Edycja studenta":
                        pick_student_name = input("Wpisz imię/ imiona studenta którego szukasz[WZÓR: Imię Imię]: ")
                        pick_student_surname = input("Wpisz nazwisko/ nazwiska studenta którego szukasz"
                                                     "[WZÓR: Nazwisko Nazwisko]: ")

                        pick_student_number = student_search_engine(students_dict,
                                                                    pick_student_name, pick_student_surname)
                        if pick_student_number:
                            display_chosen_student = display_student_dict(students_dict,
                                                                          chosen_student_number=pick_student_number)

                            data_for_edit = input("Wybierz którą daną chcesz edytować[Np. Imię]: ")

                            new_data = input(f"Wpisz nową wartość dla '{display_chosen_student[data_for_edit]}': ")

                            menu_chosen_func(students_dict, data_for_edit, new_data, pick_student_number)

                    elif menu_result == "Wyświetlanie ocen":
                        menu_chosen_func()

                    elif menu_result == "Dodawanie ocen":
                        menu_chosen_func()

                    elif menu_result == "Edycja ocen":
                        menu_chosen_func()

                except Exception as func_except:
                    print("Wystąpił nieznany błąd")
                    exception(str(func_except))

            elif int(chosen_option) == 8:
                flag = False

            else:
                print("\nWybierz numer operacji z listy!")

        except ValueError:
            print("\nWybierz prawidłową operację!")

    students_dict["index"] = index
    return students_dict


if __name__ == '__main__':
    main()
