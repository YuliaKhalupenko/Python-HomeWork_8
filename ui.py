def print_data(text=''):
    print(f"{text}")


def input_data(text=''):
    return input(f"{text}")


def add_data_pi(id_pes):
    surname = input("Фамилия: ")
    name = input("Имя: ")
    patronymic = input("Отчество: ")
    phone = input("телефон +7 :")
    return f"ID {id_pes} телефон: +7 {phone} Фамилия: {surname} Имя: {name} Отчество: {patronymic}"


def add_data_Salary(id_pes):
    salary = input("Зарплата: ")
    return f"ID {id_pes}: {salary}"


def add_data_Department(id_pes):
    department = input("Отдел: ")
    position = input("Должность: ")
    return f"ID {id_pes} Отдел: {department} Должность: {position}"
