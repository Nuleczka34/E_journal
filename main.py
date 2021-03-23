from studentfunction import json_decorator, add_student
from enum import Enum


# TODO: ZRÓB MENU GŁÓWNE
@json_decorator
def main(gen_dict: dict) -> dict:
    print(gen_dict)
    index = 1
#     Menu = Enum('Menu', {"1. Wyświetlanie listy": "display_student_dict" "2. Dodawanie studenta": "add_student",
#                             "3. Usuwanie studenta": "student_delete", "4. Edycja studenta": "student_edit",
#                             "5. Wyświetlanie ocen": "display_student_note",
#                             "6. Dodawanie ocen": "student_note_add", "7. Edycja ocen": "student_note_edit",
#                             "8. Zakończ": False})
#
#     # for check_menu in Menu:
#     #     print(check_menu)
#     gen_question = input("\nWybierz opcję z listy: ")
#
#     # for elem in Menu:
#     #     refactor_elem = str(elem).removeprefix("Menu.")
#     #     if gen_question == "1":
#     #         Menu.name
#
#     # TODO: NA KOŃCU ZWRÓĆ SŁOWNIK DO JSON
    adding = add_student()
    if adding:
        gen_dict[index] = adding

    return gen_dict


if __name__ == '__main__':
    main()
