class UserAccount:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        if len(new_password) < 8:
            return print("Минимальная длина пароля - 8 символов.")

        self.__password = new_password

    def check_password(self, password):
        if password == self.__password:
            return True
        return False


acc = UserAccount("alex", "al@gmail.com", "78H9tt9yd")
acc.set_password("lskad")
acc.set_password("cl1sk3l543!djf")

if acc.check_password("cl1sk3l543!djf") == True:
    print("Пароли совпадают.")
else:
    print("Пароли не совпадают.")


if acc.check_password("oasj001") == True:
    print("Пароли совпадают.")
else:
    print("Пароли не совпадают.")