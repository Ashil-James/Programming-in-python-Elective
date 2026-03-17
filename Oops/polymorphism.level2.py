class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def display(self):
        print(f"{self.name}'s salary: ₹{self.calculate_salary()}")


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)  # ✅ parent handles name & salary
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus


class Intern(Employee):
    def calculate_salary(self):
        return super().calculate_salary() * 0.5


class Contractor(Employee):
    def __init__(self, name, base_salary, hourly_rate, hours_worked):
        super().__init__(name, base_salary)  # ✅ parent handles name & salary
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return super().calculate_salary() + (self.hourly_rate * self.hours_worked)


emp        = Employee("Ash", 50000)
manager    = Manager("Rahul", 80000, 5000)
intern     = Intern("Priya", 30000)
contractor = Contractor("Dev", 20000, 500, 160)

for person in [emp, manager, intern, contractor]:
    person.display()