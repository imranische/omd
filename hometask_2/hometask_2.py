import csv

# имя файла, который будет использоваться в программе
filename = './Corp_Summary.csv'
# имя файла, который будет записан в одном из случаев
file_result = './Result.csv'
# разделитель в csv-файле
delim = ';'


def main_menu() -> None:
    """Главное меню, пользователю предстоит выбрать одну из трёх возможных опций.
    В зависимости от выбора пользователя будет вызвана функция option_1(), option_2() или option_3()"""
    option = 0
    while option not in {'1', '2', '3'}:
        option = input(
            'Введите 1, 2 или 3, где:\n' +
            '1) Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него\n' +
            '2) Вывести сводный отчёт по департаментам:' +
            ' название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату\n' +
            '3) Сохранить сводный отчёт из предыдущего пункта в виде csv-файла.' +
            ' При этом необязательно вызывать сначала команду из п.2\n')
        if option not in {'1', '2', '3'}:
            print('Некорректный ввод!')
    if option == '1':
        option_1()
    elif option == '2':
        option_2()
    elif option == '3':
        option_3()


def get_dict_from_csv(filename: str, delim: str = ',', q_char: str = '"', enc='utf-8') -> list:
    """Функция получает список словарей из CSV-файла, где ключи - названия столбцов, значения - элементы стобца"""
    with open(filename, encoding=enc) as file:
        rows = list(csv.DictReader(file, delimiter=delim, quotechar=q_char))
    return rows


def option_1() -> None:
    """Функция выполняет опцию 1 из главного меню"""
    # считываем данные из csv-файла и записываем в переменную csv-list как список из словарей
    csv_list = get_dict_from_csv(filename, delim)
    csv_list.sort(key=lambda row: (row['Департамент'], row['Отдел']))
    # Создаём словарь со множеством департаментов
    department_dict = {}
    for row in csv_list:
        department_dict.setdefault(row['Департамент'], set()).add(row['Отдел'])
    print(
        '\nНаша компания состоит из следующих департаментов, каждый из которых представлен из команд, указанных ниже:')
    for key in department_dict:
        print(key, end=': ')
        print(*department_dict[key], sep=', ', end='.\n')


def get_salary_dict() -> dict:
    """Функция возвращает словарь, который пригодится для реализации опций 2 и 3"""
    # считываем данные из csv-файла и записываем в переменную csv-list как список из словарей
    csv_list = get_dict_from_csv(filename, delim)
    csv_list.sort(key=lambda row: (row['Департамент'], row['Отдел']))
    # Создаём словарь со списком зарплат для компаний
    salary_dict = {}
    for row in csv_list:
        salary_dict.setdefault(row['Департамент'], []).append(int(row['Оклад']))
    # меняем список зарплат на численность департамента, "вилку" зарплат и среднюю зарплату в департаменте
    for department in salary_dict:
        salary_dict[department] = {
            'Численность': len(salary_dict[department]),
            'Минимальная зарплата': min(salary_dict[department]),
            'Максимальная зарплата': max(salary_dict[department]),
            'Средняя зарплата': round(sum(salary_dict[department]) / len(salary_dict[department]), 2)
            }
    return salary_dict


def option_2() -> None:
    """Функция выполняет опцию 2 из главного меню"""
    salary_dict = get_salary_dict()
    print('\nОтчёт по зарплатам в департаментах нашей компании:')
    for key in salary_dict:
        print(f'{key}:'.ljust(18), end=' ')
        print(*[f'{key}: {value}' for key, value in salary_dict[key].items()], sep=';\t')


def option_3() -> None:
    """Функция выполняет опцию 3 из главного меню"""
    salary_dict = get_salary_dict()
    # меняем данные, чтобы их было удобно записать в файл
    list_to_csv = []
    for key in salary_dict:
        row = {}
        row['Департамент'] = key
        for k in salary_dict[key]:
            row[k] = salary_dict[key][k]
        list_to_csv.append(row)
    columns = [key for key in list_to_csv[0]]
    # записывает нужный файл
    with open(file_result, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=delim, quoting=csv.QUOTE_NONNUMERIC)
        # запись заголовков
        writer.writeheader()
        # запись строк
        for row in list_to_csv:
            writer.writerow(row)
    print('Отчёт по зарплатам в департаментах нашей компании записан в файл', file_result)


if __name__ == '__main__':
    main_menu()