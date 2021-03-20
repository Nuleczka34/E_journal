from datetime import datetime

students_dict = {}
index = 0


def date_valid(date: str) -> bool:
    try:
        datetime_get = datetime.strptime(date, '%d.%m.%Y')
        actual_date = datetime.now()
        age = actual_date.year - datetime_get.year - \
            ((actual_date.month, actual_date.day) < (datetime_get.month, datetime_get.day))

        if 18 <= age <= 25:
            return True
        else:
            print("\nStudent musi posiadać 18 lat!")
            return False

    except ValueError:
        print("\nWpisana data jest niepoprawna Wzór:[dd-mm=yyyy]!")
        return False


def name_valid(first_name):
    if first_name.istitle() and 19 >= len(first_name) > 1:
        return True
    else:
        print("\nImię(Imiona) studenta jest/są nieprawidłowe!\n"
              "Wzór:[Patryk / Patryk-Łukasz]")
        return False


def surname_valid(student_surname):
    if student_surname.istitle() and 30 >= len(student_surname) > 1:
        return True
    else:
        print("\nNazwisko(Nazwiska) studenta jest/są nieprawidłowe!\n"
              "Wzór:[Kowalski/ Kowalski-Malinowski}")
        return False


def semester_valid(sem):
    sem = int(sem)
    if 0 <= sem <= 12:
        return True
    else:
        print("\nLiczba semestru jest nieprawidłowa,wpisz liczbę z przedziału [1-12]")
        return False


def data_valid(name: str, surname: str, birthdate: str, semester: str) -> bool:
    if name_valid(name) and surname_valid(surname) and date_valid(birthdate) and semester_valid(semester):
        return True
    else:
        return False


def add_student(gen_dict) -> dict:
    global index
    index += 1

    student_name = input("Podaj imię(imiona): ")
    student_surname = input("Podaj nazwisko(nazwiska): ")
    student_birthdate = input("Podaj datę urodzenia[dd.mm.yyyy]: ")
    student_semester = input("Podaj obecny semestr: ")
    if data_valid(student_name, student_surname, student_birthdate, student_semester):
        student_data_list = [student_name, student_surname, student_birthdate, student_semester]
        gen_dict[index] = student_data_list
        return gen_dict
    else:
        print("Nie udało się stworzyć studenta!")
