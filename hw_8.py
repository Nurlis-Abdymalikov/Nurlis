import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS countries (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL)")
cursor.execute("INSERT INTO countries (title) VALUES ('Киргизия'), ('Германия'), ('Китай')")

cursor.execute(
    "CREATE TABLE IF NOT EXISTS cities (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, area REAL DEFAULT 0, country_id INTEGER, FOREIGN KEY (country_id) REFERENCES countries(id))")
cursor.execute(
    "INSERT INTO cities (title, area, country_id)"
    " VALUES ('Бишкек', 200.5, 1), ('Ош', 150.3, 1),"
    " ('Берлин', 891.8, 2), ('Мюнхен', 310.7, 2), "
    "('Пекин', 16410.5, 3), ('Шанхай', 6340.5, 3),"
    " ('Гуанчжоу', 7434.6, 3)")

cursor.execute(
    "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "first_name TEXT NOT NULL, "
    "last_name TEXT NOT NULL, "
    "city_id INTEGER, FOREIGN KEY"
    " (city_id) REFERENCES cities(id))")
cursor.execute(
    "INSERT INTO students (first_name, last_name, city_id)"
    " VALUES ('Иван', 'Иванов', 1),"
    " ('Алексей', 'Петров', 2), "
    "('Михаил', 'Смирнов', 3), "
    "('Ольга', 'Дмитриева', 4), "
    "('Мария', 'Кузнецова', 5), "
    "('Петр', 'Попов', 6), "
    "('Елена', 'Васильева', 7),"
    " ('Анна', 'Федорова', 1),"
    " ('Сергей', 'Андреев', 2),"
    " ('Дмитрий', 'Михайлов', 3),"
    "('Виктор', 'Козлов', 4), "
    "('Ирина', 'Соколова', 5),"
    " ('Анатолий', 'Яковлев', 6),"
    " ('Наталья', 'Григорьева', 7),"
    " ('Юлия', 'Лебедева', 1)")

print(
    "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

cursor.execute("SELECT id, title FROM cities")
cities = cursor.fetchall()
for city in cities:
    print(f"{city[0]}. {city[1]}")

city_id = int(input("Введите id города: "))

if city_id == 0:
    print("Выход из программы.")
else:
    cursor.execute("""
    SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
    FROM students
    JOIN cities ON students.city_id = cities.id
    JOIN countries ON cities.country_id = countries.id
    WHERE cities.id = ?
    """, (city_id,))

    students = cursor.fetchall()

    if students:
        print("\nСписок учеников:")
        for student in students:
            print(
                f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]} км²")
    else:
        print("В этом городе нет учеников.")

conn.close()
