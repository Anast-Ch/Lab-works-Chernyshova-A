class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        print(f"Марка машины: {self.make}. Модель машины: {self.model}")


class Car(Vehicle):

    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        print(f"Марка машины: {self.make}. Модель машины: {self.model}. Тип топлива: {self.fuel_type}")


v1 = Car("Kia", "Rio", "Бензин")
v1.get_info()
