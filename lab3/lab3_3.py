def choice_type_of_print(path, type_of_r):
    try:
        if type_of_r == 1:
            with open(path, "r") as f:
                text = f.read()
                print(text)
        elif type_of_r == 2:
            with open(path, "r") as f:
                for i in f:
                    print(i)
    except FileNotFoundError:
        print("Файл не найден.")

# path1 = "example.txt"
# path2 = "exxample.txt"
#
# choice_type_of_print(path1, 2)
#
# choice_type_of_print(path2, 2)