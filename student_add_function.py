import json
from re import match
from datetime import datetime
from math import ceil
from logging import basicConfig, DEBUG, exception

basicConfig(filename="logging.log", level=DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def date_valid(date: str) -> bool:
    try:
        datetime_get = datetime.strptime(date, '%d.%m.%Y')
        actual_date = datetime.now()
        age = actual_date.year - datetime_get.year - ((actual_date.month, actual_date.day) <
                                                      (datetime_get.month, datetime_get.day))

        if 18 <= age <= 100:
            return age

        else:
            print("\nWiek studenta musi mieścić się w zakresie 18-100 lat!")

            return False

    except ValueError:
        print("\nWpisana data jest niepoprawna!\nWzór:[dd-mm-yyyy]")

        return False


# TODO: DODAJ ABY IMIONA NIE MOGŁY BYĆ IDENTYCZNE
def name_valid(first_name: str) -> bool:
    if match(r"^[A-ZŻŹĆĄŚĘŁÓŃ][a-zżźćńółęąś]{1,18}$|^[A-ZŻŹĆĄŚĘŁÓŃ][a-zżźćńółęąś]{1,18} "
             r"[A-ZŻŹĆĄŚĘŁÓŃ][a-zżźćńółęąś]{1,18}$", first_name) and first_name:
        return True

    else:
        print("\nImię(Imiona) studenta jest/są nieprawidłowe!\n"
              "Wzór:[Patryk / Patryk Łukasz]")

        return False


# TODO: DODAJ ABY NAZWISKA NIE MOGŁY BYĆ IDENTYCZNE
def surname_valid(surname: str) -> bool:
    if match(r"^[A-ZŻŹĆĄŚĘŁÓŃ][a-zżźćńółęąś]{1,13}$|^[A-ZŻŹĆĄŚĘŁÓŃ][a-zżźćńółęąś]{1,13}[ \-][A-ZŻŹĆĄŚĘŁÓŃ]["
             r"a-zżźćńółęąś]{1,13}$", surname):
        return True

    else:
        print("\nNazwisko(Nazwiska) studenta jest/są nieprawidłowe!\n"
              "Wzór:[Kowalski/ Kowalski-Malinowski}")

        return False


def semester_valid(sem: str, date_validate) -> bool:
    student_age = date_validate

    years_list = [year for year in range(18, 101)]

    year_check = {1: years_list[0:], 2: years_list[1:], 3: years_list[2:],
                  4: years_list[3:], 5: years_list[4:], 6: years_list[5:]}

    if sem.isnumeric() and student_age:
        sem = int(sem)
        actual_student_year = ceil(sem / 2)

        if student_age in year_check[actual_student_year]:
            return True

        else:
            print("\nWiek ucznia, nie pozwala na przypisanie go to tego semestru!")
            return False

    else:
        print("\nWpisany numer semestru jest nieprawidłowy!\n"
              "Wpisz liczbę z przedziału [1 - 12]")
        return False


def data_valid(name: str, surname: str, birthdate: str, semester: str) -> bool:
    name_validate = name_valid(name)
    surname_validate = surname_valid(surname)
    date_validate = date_valid(birthdate)
    semester_validate = semester_valid(semester, date_validate)

    if name_validate and surname_validate and date_validate and semester_validate:
        return True

    else:
        return False


def student_add(gen_dict: dict, index: int, student_name: str, student_surname: str,
                student_birthdate: str, student_semester: str) -> bool:

    if data_valid(student_name, student_surname, student_birthdate, student_semester):
        student_data_list = [student_name, student_surname, student_birthdate, student_semester]
        gen_dict[index] = student_data_list

        print("\nUdało się stworzyć studenta!")

        return True

    else:
        print("\nNie udało się stworzyć studenta!")

        return False


def json_decorator(func):
    def wrapper():
        with open("students.json", "a+", encoding="UTF=8") as students_json:
            students_json.seek(0)
            read_json = students_json.read()

            if read_json:
                try:
                    students_json.seek(0)
                    loaded_json = json.load(students_json)

                except ValueError as json_except:
                    exception(str(json_except))
                    return print("Błąd JSON, Napraw lub wyczyść plik")

            else:
                loaded_json = {}

        final_dict = func(loaded_json)

        with open("students.json", "w", encoding="UTF-8") as students_json:
            try:
                json.dump(final_dict, students_json)
            except Exception as save_json_except:
                print("Nie udało zapisać się studentów!")
                exception(save_json_except)

    return wrapper
