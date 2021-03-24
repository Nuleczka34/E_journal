from student_add_function import json_decorator, student_add
from student_rest_functions import display_student_dict
from logging import basicConfig, DEBUG, exception

basicConfig(filename="logging.log", level=DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


# TODO: ZRÓB MENU GŁÓWNE
@json_decorator
def main(gen_dict: dict) -> dict:
    index = gen_dict.get("index", 1)
    if "index" in gen_dict:
        gen_dict.pop("index")

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

        chose_option = input("Wybierz numer operacji z listy: ").strip()
        try:
            if 0 < int(chose_option) <= 7:
                menu_dict = {'1': ("Wyświetlanie listy", display_student_dict),  # TODO: WYŚWIETLANIE LISTY
                             '2': ("Dodawanie studenta", student_add),
                             '3': ("Usuwanie studenta", "student_delete"),  # TODO: USUWANIE STUDENTA
                             '4': ("Edycja studenta", "student_edit"),  # TODO: EDYTUJ DANE STUDENTA
                             '5': ("Wyświetlanie ocen", "display_student_note"),  # TODO: WYŚWIETLANIE OCEN
                             '6': ("Dodawanie ocen", """student_note_add"""),  # TODO: DODAWANIE OCEN
                             '7': ("Edycja ocen", "student_note_edit")}  # TODO: EDYCJA OCEN

                menu_result, menu_chosen_func = menu_dict.get(chose_option)

                try:
                    print(f"\nWybrałeś '{menu_result}'\n")
                    if menu_result == "Dodawanie studenta":
                        student_name = input("Podaj imię(imiona): ").strip()
                        student_surname = input("Podaj nazwisko(nazwiska): ").strip()
                        student_birthdate = input("Podaj datę urodzenia[dd.mm.yyyy]: ").strip()
                        student_semester = input("Podaj obecny semestr: ").strip()

                        adding_student = menu_chosen_func(gen_dict, index, student_name, student_surname,
                                                          student_birthdate, student_semester)
                        if adding_student:
                            index += 1

                except Exception as func_except:
                    print("Wystąpił nieznany błąd")
                    exception(str(func_except))

            elif int(chose_option) == 8:
                flag = False

            else:
                print("\nWybierz numer operacji z listy!")

        except ValueError:
            print("\nWybierz prawidłową operację!")

    gen_dict["index"] = index
    return gen_dict


if __name__ == '__main__':
    main()
