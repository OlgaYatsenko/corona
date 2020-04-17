from bs4 import BeautifulSoup

#parse through html of worldometers website (html is a separate document as direct parse is forbidden;extact table with yesterday's data and cpy into table.xml file
f=open('worldometers.txt',"r")
t=open('tables.xml','w')
#Delete data from the day before
t.truncate()

soup = BeautifulSoup(f, 'html.parser')
# Retrieve all of the anchor table
tags = soup('table')

t.write(str(tags[1]))

f.close()
t.close()