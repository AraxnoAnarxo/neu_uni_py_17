from bs4 import BeautifulSoup
import requests
import re

import pysqlite3 as lite
import sys


connect = None

try:
    connect = lite.connect('site_parser.db')
    cur = connect.cursor()



except lite.Error as e:
    print(f'Error {e.args[0]}:')
    sys.exit(1)


def parsing_for_sql():

    max_page = 20
    pages = []



    for x in range(1, max_page + 1):
        pages.append(requests.get('https://auto.drom.ru/chevrolet/tahoe/page' + str(x)))

    for n in pages:
        soup = BeautifulSoup(n.text, 'html.parser')

        car_name = soup.find_all('div', class_="b-advItem__title")

        for rev in car_name:
            a = str(rev.text)
            #car_list_len.append(a)
            car = re.split(r',', a)
            #car_name_list.append(car[0])
            car_year = re.sub(r'[ ]', '', car[1])
            car_year = int(car_year)

            cur.execute("INSERT INTO chevrolet_tahoe VALUES(car_name, car_year)")




cur.execute("CREATE TABLE chevrolet_tahoe(car_name TEXT, car_year INT)")
parsing_for_sql()


sqlite_select_query = """SELECT * from chevrolet_tahoe"""
cur.execute(sqlite_select_query)

records = cur.fetchall()


for row in records:
    print(row)