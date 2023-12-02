"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]


def whitch_dep(lst: list) -> list:
    dep_names = []
    for depart in departments:
        dep_names.append(depart['title'])
    return dep_names


def print_dep_name(lst: list) -> None:
    for i in lst:
        print(i)


def what_name(lst: list) -> list:
    emploers = []
    for i in departments:
        for employee in i["employers"]:
            full_name = f"Полное имя: {employee['first_name']} {employee['last_name']}"
            emploers.append(full_name)
    return emploers


def print_names_all_emp(lst: list) -> None:
    for i in lst:
        print(i)


def get_employees_with_departments(lst: list) -> list:
    employees = []
    for department in departments:
        department_name = department["title"]
        for employer in department["employers"]:
            full_name = f"{employer['first_name']} {employer['last_name']}"
            employee_with_department = f'{full_name} - Отдел: {department_name}'
            employees.append(employee_with_department)
    return employees


def print_dep_with_name(lst: list) -> None:
    for i in lst:
        print(i)


def get_high_salary_employees(lst: list) -> list:
    high_salary_employees = []
    for department in departments:
        for employee in department["employers"]:
            if employee["salary_rub"] > 100000:
                high_salary_employees.append(f"{employee['first_name']} {employee['last_name']}")
    return high_salary_employees


def get_hi(lst: list) -> None:
    for i in lst:
        print(i)


def get_low_salary_positions(lst: list) -> list:
    low_salary_positions = []
    for department in departments:
        for employee in department["employers"]:
            if employee["salary_rub"] < 80000:
                low_salary_positions.append(employee["position"])
    return low_salary_positions


def get_low(lst: list) -> None:
    for i in lst:
        print(i)


def sum_per_mounth(lst: list) -> dict:
    total_salary = {}

    for department in departments:
        department_title = department["title"]
        total_salary[department_title] = 0

        for employee in department["employers"]:
            total_salary[department_title] += employee["salary_rub"]

    return total_salary


def ggg(dic: dict) -> None:
    for i in dic:
        zp = dic[i]
        dp = i
        print(dp, zp)


def main():
    print(f'Название всех отделов: ')
    print_dep_name(whitch_dep(departments))
    print('\n')

    print(f'Имена всех сотрудников: ')
    print_names_all_emp(what_name(departments))
    print('\n')

    print(f'Имена сотрудников и названия отделов в которых они работают: ')
    print_dep_with_name(get_employees_with_departments(departments))
    print(f'\n')

    print(f"Имена всех сотружников с зп больше 100: ")
    get_hi(get_high_salary_employees(departments))
    print(f"\n")

    print(f"Позиции с самой маленькой зп: ")
    get_low(get_low_salary_positions(departments))
    print(f"\n")

    print(f"сколько тратится на один отдел: ")
    ggg(sum_per_mounth(departments))


if __name__ == '__main__':
    main()
