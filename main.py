from studentfunction import *


# TODO: ZRÓB MENU GŁÓWNE
@json_decorator
def main(gen_dict) -> dict and int:
    flag = True
    index = gen_dict.get("index", 1)
    if "index" in gen_dict:
        gen_dict.pop("index")
    while flag:
        student_adding = add_student(gen_dict, index)
        if student_adding:
            index += 1
            gen_dict["index"] = index
            break

    return gen_dict


if __name__ == '__main__':
    main()
