import sqlite3 as lite
import sys

connect = None

try:
    connect = lite.connect('test.db')
    cur = connect.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()[0]

    print(f'SQLite version: {data}')



except lite.Error as e:
    print(f'Error {e.args[0]}:')
    sys.exit(1)

#cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")

# cur.execute("INSERT INTO cars VALUES(1, 'AUDI', 373849)")
# cur.execute('INSERT INTO cars VALUES(?,?,?)', (2, "Mercedes", 5719204))
#
#
# cur.execute('INSERT INTO cars VALUES(3, "Skoda", 163738)')
# cur.execute('INSERT INTO cars VALUES(4, "Volvo", 8937263)')
# cur.execute('INSERT INTO cars VALUES(5, "Bentley", 848399)')
# cur.execute('INSERT INTO cars VALUES(6, "Citroen", 8376353)')
# cur.execute('INSERT INTO cars VALUES(7, "Hummer", 837453)')
# cur.execute('INSERT INTO cars VALUES(8, "Volkswagen", 7665333)')
#
# car_list = [[9, 'Lada', 5000], [10, 'Renault', 9000]]
#
#
# for car in car_list:
#     cur.execute("INSERT INTO cars VALUES(?,?,?)", (car[0], car[1], car[2]))

# Выгружаем данные полностью

# sqlite_select_query = """SELECT * from cars"""
# cur.execute(sqlite_select_query)
#
# records = cur.fetchall()
#
# print(len(records))
#
# for row in records:
#     print(row)

# При большом объеме данных выгружать полностью бывает нецелесообразно.
# В таком случае выгрузим данные построчно.

# with connect:
#     cur = connect.cursor()
#     cur.execute("SELECT * FROM cars")
#
#     while True:
#         row = cur.fetchone()
#         if row == None:
#             break
#         print(row[0], row[1], row[2])

# Иногда неудобно получать tuple в качестве данных, а удообнее работать со словарем по ключам.

# with connect:
#     connect.row_factory = lite.Row
#     cur = connect.cursor()
#     cur.execute("SELECT * FROM cars")
#
#     rows = cur.fetchall()
#
#     for row in rows:
#         print(f"{row['id']}, {row['name']}, {row['price']}")


# Редактирование данных (UPDATE и WHERE)

# with connect:
#
#     cur = connect.cursor()
#     uPrice = 5000
#     uId = 2
#     cur.execute("UPDATE cars SET price = ? WHERE id > ?", (uPrice, uId))
#     print(f'Number of rows updated: {cur.rowcount}')

# Редактирвоание данных (DELETE и WHERE)

# with connect:
#     cur = connect.cursor()
#     uId = 2
#     cur.execute(f"DELETE FROM cars WHERE id = {uId}")
#     print(f'Number of rows updated: {cur.rowcount}')


# Подсчет рядов с определенным условием (Count)

# with connect:
#
#     cur = connect.cursor()
#     uId = 5
#     rowQuery = f"SELECT Count() FROM cars WHERE id > {uId}"
#     cur.execute(rowQuery)
#     numberOfRows = cur.fetchone() [0]
#     print(numberOfRows)

# Сортировка Order By

# with connect:
#
#     cur = connect.cursor()
#     #row_group = f"SELECT * FROM cars ORDER BY cars.price"
#     row_group = f"SELECT * FROM cars ORDER BY cars.price DESC" #обратный порядок
#     cur.execute(row_group)
#
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)

# Объединение таблиц JOIN

#cur.execute("CREATE TABLE cars_year(name TEXT, year INT)")
#
cur.execute("INSERT INTO cars_year VALUES(?,?)", ('Volvo', 2018))
cur.execute("INSERT INTO cars_year VALUES('Bentley', 2011)")
cur.execute("INSERT INTO cars_year VALUES('Citroen', 1937)")
cur.execute("INSERT INTO cars_year VALUES('Lada', 1945)")


with connect:
    cur = connect.cursor()

    #rows_join = f'SELECT * FROM cars JOIN cars_year ON cars.name = cars_year.name'
    #rows_join = f'SELECT * FROM cars INNER JOIN cars_year ON cars.name = cars_year.name' # пересечение
    rows_join = f'SELECT * FROM cars LEFT JOIN cars_year ON cars.name = cars_year.name'
    #rows_join = f'SELECT * FROM cars RIGHT JOIN cars_year ON cars.name = cars_year.name'

    cur.execute(rows_join)
    rows = cur.fetchall()
    for row in rows:
        print(row)
