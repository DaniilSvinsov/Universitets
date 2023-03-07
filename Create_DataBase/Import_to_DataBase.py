import sqlite3 as sq
import json
traffic_vuz = json.load(open('Universitets.json', encoding='utf-8-sig'))
traffic_grades = json.load(open('grades.json', encoding='utf-8-sig'))
traffic_facult = json.load(open('facult.json', encoding='utf-8-sig'))

main_data, data_vuz, data_grades, data_facult = [], [], [], []
# Данные для таблицы Universitets и для Foreign key
for elem in traffic_vuz:
    data_about_vuz = []
    for small_data in elem.values():
        data_about_vuz.append(small_data)
    data_vuz.append(tuple(data_about_vuz)[0])
    main_data.append(tuple(data_about_vuz))
# Для выгрузки данных и
def table_link(data):
    structured_data = []
    for dicts in data:
        local_list = []
        for note in dicts.items():
            if note[0] != "Вуз":
                local_list.append(note[1])
        local_list.append(data_vuz.index(dicts.get("Вуз", local_list))+1)
        structured_data.append(tuple(local_list))
    return structured_data

data_grades = table_link(traffic_grades)

data_facult = table_link(traffic_facult)

data_facult = set(data_facult)
data_facult = list(data_facult)

with sq.connect("qwe.db") as connect:
    cur = connect.cursor()
    # Создание таблицы Universitets
    cur.execute('''CREATE TABLE IF NOT EXISTS Universitets(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Название TEXT,
            Средний_балл TEXT,
            Количество_мест INTEGER,
            Количество_образовательных_программ INTEGER,
            Город TEXT)''')
    # Заполнение таблицы Universitets
    for vuz in main_data:
        cur.execute("INSERT INTO Universitets VALUES(NULL, ?, ?, ?, ?, ?)", vuz)

    cur.execute('''CREATE TABLE IF NOT EXISTS Grades(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Общая_оценка_вуза TEXT,
            Состояние_и_оснащение_корпусов_вуза TEXT,
            Удобство_расположения_корпусов_вуза TEXT,
            Качество_образования TEXT,
            Качество_работы_административного_аппарата TEXT,
            Дополнительные_активности_в_вузе TEXT,
            Качество_общепита TEXT,
            Средняя_стоимость_обеда_в_столовой TEXT,
            Средние_затраты_на_дорогу_в_месяц TEXT,
            vuz_id INTEGER,
            FOREIGN KEY (vuz_id) REFERENCES Universitets(ID)
            )''')

    for grade in data_grades:
        cur.execute("INSERT INTO Grades VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", grade)

    cur.execute('''CREATE TABLE IF NOT EXISTS Facultets(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        "Направление_подготовки_програм" TEXT,
        "Балл" INTEGER,
        "Балл(2021)" INTEGER,
        "Форма_обучения" TEXT,
        "Экзамены_ЕГЭ" TEXT,
        "Уровень_программы" TEXT,
        "Бюджетных_мест" INTEGER,
        "Профиль_программы" TEXT,
        "Код_программы" TEXT,
        "Стоимость" INTEGER,
        "Олимпиадники" INTEGER,
        "Подразделение" TEXT,
        vuz_id INTEGER,
        FOREIGN KEY (vuz_id) REFERENCES Universitets(ID)
        )''')
    
    for facult in data_facult:
        cur.execute('INSERT INTO Facultets VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', facult)
