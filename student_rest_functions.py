def display_student_dict(gen_dict):
    try:
        pick_student = int(input("Podaj numer studenta, którego chcesz edytować: "))
    except ValueError:
        print("Musisz wpisać numer")
    print(f"Wybrałeś: {gen_dict[pick_student]}")