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


def min_salary_in(lst: list) -> dict:
    min_dict = {}
    for department in departments:
        min_salary = []
        depart_name = department['title']
        for salary in department['employers']:
            min_salary.append(salary['salary_rub'])
        minimum_salary = min(min_salary)
        min_dict[depart_name] = minimum_salary
    return min_dict


def print_min() -> None:
    for k, v in min_salary_in(departments).items():
        print(f"Минимальная зарплата в отделе {k} = {v}")


def all_types_sol(lst: list) -> dict:
    new_solary = {}

    for department in departments:
        name_depart = department['title']
        employers = department['employers']
        salaries = []
        for emploer in employers:
            salaries.append(emploer['salary_rub'])
            min_salary = min(salaries)
            avg_salary = sum(salaries) / len(salaries)
            max_salary = max(salaries)
            new_solary[name_depart] = {
                "min_s": min_salary,
                "avg_s": avg_salary,
                "max_s": max_salary
            }

    return new_solary


def print_salary_stats() -> None:
    for k, v in all_types_sol(departments).items():
        print(f"отдел: {k} мин зп: {v['min_s']}, ср зп: {v['avg_s']}, макс зп: {v['max_s']}")


def average_salary(lst: list) -> float:
    count = 0
    count1 = 0
    avg_count = 0
    for departmen in departments:
        name = departmen['employers']
        for i in name:
            count += i['salary_rub']
            count1 += 1
            avg_count = count / count1
    return avg_count


def post_salary(lst: list) -> list:
    prof = []
    for dep in departments:
        name = dep['employers']
        for i in name:
            if i['salary_rub'] > 90000:
                prof.append(i['position'])
    return prof


def print_post_salary() -> None:
    for i in post_salary(departments):
        print(i)


def calculate_avg_salary(lst: list) -> dict:
    avg_salary_dict = {}

    for department in departments:
        name = department['title']
        total_salary = 0
        count = 0
        for employee in department['employers']:
            first_name = employee['first_name']
            if first_name in ["Michelle", "Nicole", "Christina", "Caitlin"]:
                total_salary += employee['salary_rub']
                count += 1
        if count > 0:
            avg_salary = total_salary / count
            avg_salary_dict[name] = avg_salary
    return avg_salary_dict


def print_avg_salary_girls() -> None:
    for k, v in calculate_avg_salary(departments).items():
        print(f"Отдел: {k}, средняя зп девушек: {v}")


def last_letter(lst: list) -> set[str | int]:
    new_set = set()
    x = 'aoeiuy'
    for dep in departments:
        name = dep['employers']
        for i in name:
            first_name = i['first_name']
            for j in x:
                if j in first_name[-1]:
                    new_set.add(first_name)
    return new_set


def print_set() -> None:
    for i in last_letter(departments):
        print(i)


def calculate_average_tax(lst: list, list: list) -> dict:
    department_tax = {}

    for dep in departments:
        name = dep['title']
        total_salary = 0
        total_tax = 0
        num_employees = 0

        for employer in dep['employers']:
            for tax in taxes:
                if tax['department'] is None or tax['department'] == name:
                    tax_amount = (employer['salary_rub'] * tax['value_percents']) / 100
                    total_tax += tax_amount

            total_salary += employer['salary_rub']
            num_employees += 1

        average_tax_per_employee = total_tax / num_employees if num_employees > 0 else 0
        department_tax[name] = average_tax_per_employee

    return department_tax


def prin_average_tax() -> None:
    for k, v in calculate_average_tax(departments, taxes).items():
        print(f"Отдел: {k} - средний налог: {v}")


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
    print(f"\n")

    print(f"Отделы с указанием минимальной зарплаты: ")
    print_min()
    print(f"\n")

    print(f"Отделы с указанием минимальной средней и максимальной зп: ")
    print_salary_stats()
    print(f"\n")

    print(f"Средняя за по всей фирме: {average_salary(departments)}")
    print(f"\n")

    print(f"Названия должностей которые получают больше 90к: ")
    print_post_salary()
    print(f"\n")

    print(f"Средняя зп по отделам среди девушек: ")
    print_avg_salary_girls()
    print(f"\n")

    print(f"Имена людей которые заканчиваются на гласную: ")
    print_set()
    print(f"\n")

    print(f"Отделы со средним налогом на сотрудников этого отдела: ")
    prin_average_tax()
    print(f"\n")


if __name__ == '__main__':
    main()
