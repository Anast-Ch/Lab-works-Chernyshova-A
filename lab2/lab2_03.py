#Напишите функцию is_prime, которая определяет,
#является ли число простым, и возвращает True или False соответственно.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**(1/2)+1)):
        if number % i == 0:
            return False
    return True

num = int(input("Введите число: "))
if is_prime(num):
    print("Число простое")
else:
    print("Число не является простым")