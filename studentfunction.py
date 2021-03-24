import json
import re
from datetime import datetime
from math import ceil
from logging import debug, basicConfig, DEBUG

basicConfig(filename="logging.log", level=DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def date_valid(date: str) -> bool:
    try:
        datetime_get = datetime.strptime(date, '%d.%m.%Y')
        actual_date = datetime.now()
        age = actual_date.year - datetime_get.year - \
            ((actual_date.month, actual_date.day) < (datetime_get.month, datetime_get.day))

        if 18 <= age:
            return age

        else:
            print("\nStudent musi posiadać 18 lat!")
            return False

    except ValueError:
        print("\nWpisana data jest niepoprawna!\nWzór:[dd-mm-yyyy]")
        return False


def name_valid(first_name: str) -> bool:
    if re.match(r"^[A-Ż][a-ż]{1,18}|[A-Ż][a-ż]{1,18}[ ][A-Ż][a-ż]{1,18}$", first_name):
        return True

    else:
        print("\nImię(Imiona) studenta jest/są nieprawidłowe!\n"
              "Wzór:[Patryk / Patryk Łukasz]")
        return False


def surname_valid(surname: str) -> bool:
    if re.match(r"^[A-Ż][a-ż]{1,13}|[A-Ż][a-ż]{1,13}[ \-][A-Ż][a-ż]{1,13}$", surname):
        return True

    else:
        print("\nNazwisko(Nazwiska) studenta jest/są nieprawidłowe!\n"
              "Wzór:[Kowalski/ Kowalski-Malinowski}")
        return False


# TODO: POPRAW TEN MAKARON
def semester_valid(sem: str, date_validate, when_birth: str) -> bool:
    if sem.isnumeric():
        sem = int(sem)
        check_age = date_validate(when_birth)
        actual_student_year = ceil(sem / 2)

        if actual_student_year == 1 and check_age >= 18:
            return True

        elif actual_student_year == 2 and check_age >= 19:
            return True

        elif actual_student_year == 3 and check_age >= 20:
            return True

        elif actual_student_year == 4 and check_age >= 21:
            return True

        elif actual_student_year == 5 and check_age >= 22:
            return True

        elif actual_student_year == 6 and check_age >= 23:
            return True

        else:
            print("\nLiczba semestru jest nieprawidłowa,wpisz liczbę z przedziału [1-12]\n"
                  "Oraz sprawdź czy wiek studenta pozwala na umieszczenie go na danym semestrze")

            return False

    else:
        print("\nMusisz wpisać numer semestru!")

        return False


def data_valid(name: str, surname: str, birthdate: str, semester: str) -> bool:
    name_validate = name_valid(name)
    surname_validate = surname_valid(surname)
    date_validate = date_valid(birthdate)
    semester_validate = semester_valid(semester, date_valid, birthdate)

    if name_validate and surname_validate and date_validate and semester_validate:

        return True

    else:

        return False


def student_add(gen_dict, index) -> list or bool:
    student_name = input("Podaj imię(imiona): ").strip()
    student_surname = input("Podaj nazwisko(nazwiska): ").strip()
    student_birthdate = input("Podaj datę urodzenia[dd.mm.yyyy]: ").strip()
    student_semester = input("Podaj obecny semestr: ").strip()

    if data_valid(student_name, student_surname, student_birthdate, student_semester):
        student_data_list = [student_name, student_surname, student_birthdate, student_semester]
        gen_dict[index] = student_data_list

        print("\nUdało się stworzyć studenta!")

        return gen_dict

    else:
        print("\nNie udało się stworzyć studenta!")

        return False


def json_decorator(func):
    def wrapper():
        with open("students.json", encoding="UTF=8") as students_json:
            read_json = students_json.read()

            if read_json:
                try:
                    students_json.seek(0)
                    loaded_json = json.load(students_json)
                except ValueError as json_except:
                    debug(json_except)
                    return print("Błąd JSON, Napraw lub wyczyść plik")

            else:
                loaded_json = {}

        final_dict = func(loaded_json)

        # TODO: ZAPYTAJ CZY DODAĆ OBSŁUGĘ WYJĄTKU
        with open("students.json", "w", encoding="UTF-8") as students_json:
            json.dump(final_dict, students_json)

    return wrapper
