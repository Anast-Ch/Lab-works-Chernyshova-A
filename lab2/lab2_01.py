#Напишите функцию greet, которая принимает имя пользователя
# в качестве аргумента и выводит приветствие с этим именем.

def greet(name):
    print("Привет,", name)

Name = input("Введите имя: ")
greet(Name)


#Создайте функцию square, которая возвращает квадрат переданного ей числа.
def square(number):
    number *= number
    return number

num = int(input("Введите число: "))
print("Квадрат числа равен: ", square(num))

#Реализуйте функцию max_of_two, которая принимает два
# числа в качестве аргументов и возвращает большее из них.
def max_of_two(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "equal"

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

max_num = max_of_two(num1, num2)
if max_num == "equal":
    print("Числа равны")
else:
    print("Большее число: ", max_num)