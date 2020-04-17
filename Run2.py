import xml.etree.ElementTree as ET
from datetime import date, timedelta
import sqlite3

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

tree = ET.parse('tables.xml')
root = tree.getroot()


#function return values for the countiries
def data_for_country(country):
    check = False
    result=[]
    for tr in root[1]:
        for td in tr:
            if check==True:
                try:
                    a=int(td.text.replace(',', ''))
                except (AttributeError, ValueError):
                    a=0
                result.append(a)
            for a in td:
                if a.text==country:
                    check=True
            if len(result)==11:
                return result

yesterday = date.today() - timedelta(days=1)

#update SQL database with countires and their data
f=open('Countries.txt','r')
for line in f:
    country=line.split('\n')
    value=data_for_country(country[0])
    try:
        cur.execute('INSERT INTO countries (Date, Country, Cases,Deaths,Recovered,Cases_per_1M_pop,Deaths_per_1M_pop,Total_tests, Tests_per_1M_pop) VALUES (?,?,?, ?, ?, ?, ?,?,?)',
            (yesterday,country[0],value[0],value[2],value[4],value[7],value[8],value[9],value[10]))
    except TypeError:
        continue
conn.commit()
f.close()

conn.close()




