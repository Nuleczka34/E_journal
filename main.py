from studentfunction import json_decorator, add_student

from enum import Enum


# TODO: ZRÓB MENU GŁÓWNE
@json_decorator
def main(gen_dict: dict) -> dict:
    print('''\n1. Wyświetl Listę
2. Dodaj studenta
3. Usuń studenta
4. Edytuj studenta
5. Wyświetl oceny
6. Dodaj oceny
7. Edytuj oceny
8. Zakończ program
              ''')
    index = gen_dict.get("index", 1)
    while index <= 3:
        if index == 3:
            gen_dict["index"] = index
            print(gen_dict)
            break
        add_student(gen_dict, index)
        index += 1


'''DODAWANIE STUDENTA
index = gen_dict.get("index", 1)
while index <= 3:
    if index == 3:
        gen_dict["index"] = index
        print(gen_dict)
        break
    add_student(gen_dict, index)
    index += 1
'''
# TODO: NA KOŃCU ZWRÓĆ SŁOWNIK DO JSON



if __name__ == '__main__':
    main()
