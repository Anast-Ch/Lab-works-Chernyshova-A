class Employee:

    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        print(f"Идентификационный номер сотрудника {self.name} - {self.emp_id}")


class Manager (Employee):

    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_project(self):
        print(f"{self.name} - менеджер отдела {self.department}")

    def get_role(self):
        print(f"Отдел: {self.department}")

class Technician(Employee):

    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        print(f"Cотрудник {self.name} - выполняет техническое обслуживание по специализации {self.specialization}")

    def get_role(self):
        print(f"Специализация: {self.specialization}")

class TechManager(Manager , Technician):

    def __init__(self, name, emp_id, department, specialization, list_of_emp):
        Manager .__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.list_of_emp = list_of_emp

    def add_employee(self, name, emp_id, department=None, specialization=None):

        for emp in self.list_of_emp:
            if emp.emp_id == emp_id:
                print(f"Ошибка: Сотрудник с ID {emp_id} уже существует.")
                return

        if department:
            emp = Manager(name, emp_id, department)
            self.list_of_emp.append(emp)

        elif specialization:  
            emp = Technician(name, emp_id, specialization)
            self.list_of_emp.append(emp)

        else:
            print("Ошибка. Необходимо ввести род деятельности.")
            return

    def get_team_info(self):
        if self.list_of_emp:
            print("Информация о сотрудниках:")
            for emp in self.list_of_emp:
                print(f"Имя: {emp.name}. Идентификационный номер: {emp.emp_id}", end=". ")
                emp.get_role()
        else:
            print("Сотрудников нет.")


emp1 = Employee("Иван", "001")
emp2 = Manager("Алексей", "002", "IT")
emp3 = Technician("Марина", "003", "Сетевой администратор")
a = []
tm1 = TechManager("Ольга", "004", "HR", "Управление проектами", a)

emp1.get_info()
emp2.get_info()
emp3.get_info()
print()

emp2.manage_project()
emp3.perform_maintenance()
print()

tm1.add_employee("Сергей", "005", department="Маркетинг")
tm1.add_employee("Елена", "006", specialization="Программирование")
tm1.add_employee("Петр", "005", department="Продажи")

tm1.get_team_info()

