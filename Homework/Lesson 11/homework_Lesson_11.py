# Разработать модель предметной области в соответствии с вариантом:
# Предметная область - предприятие. Разработать класс Enterprise, описывающий работу с предприятием.
# Разработать класс People, описывающий человека, человек характеризуется параметрами:
# фамилия, имя, отчество, дата рождения, телефон. Разработать класс Employees на базе класса People, сотрудник
# характеризуется следующими параметрами: уникальный идентификатор сотрудника, код отдела, заработная плата.

class Enterprise:

    def get_salary(self):
        pass

    def employment(self):
        pass

    def dismissal(self):
        pass


class People(Enterprise):
    def __init__(self, surname, name, patronymic, birthday_data, tel_number):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthday_data = birthday_data
        self.tel_number = tel_number


class Employees(People):
    def __init__(self, surname, name, patronymic, birthday_data, tel_number, unique_id, salary):
        super().__init__(surname, name, patronymic, birthday_data, tel_number)
        self.unique_id = unique_id
        self.salary = salary

    def employment(self):
        print(f'{self.surname} {self.name} {self.patronymic} принят на работу')

    def dismissal(self):
        print(f"{self.surname} {self.name} {self.patronymic} уволен с работы")

    def drink_vodka(self):
        print("Выпьешь с нами водочки? yes/no")
        a = input()
        if a == "yes":
            self.salary = self.salary * 0.5
            print("Тебя спалили, получай штраф 50% зарплаты")
        else:
            print("Теперь ты нам не товарищ!")

    def check_salary(self):
        print(f"{self.surname} {self.name} {self.patronymic} ты заработал {self.salary}")

    def get_salary(self):
        print(f"{self.surname} {self.name} {self.patronymic} ты получил {self.salary}")