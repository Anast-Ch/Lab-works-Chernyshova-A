def choice_type_of_print(path, type_of_r=2):
    if type_of_r == 1:
        with open(path, "r") as f:
            text = f.read()
            print(text)
    elif type_of_r == 2:
        with open(path, "r") as f:
            for i in f:
                print(i)

choice_type_of_print("example.txt")





# fl = False
# choice = 0
# while fl == False:
#     print("Как вы хотите вывести файл: построчно или целиком?")
#     ans = input("Ответ: ")
#     if ans == "построчно":
#         choice = 1
#         fl = 1
#     elif ans == "целиком":
#         choice = 2
#         fl = 1
#     else:
#         print("Ошибка. Введите ответ заново.")

