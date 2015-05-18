import sqlite3, csv

conn = sqlite3.connect('file_names.sqlite')
conn.text_factory = str
c = conn.cursor()

try:
	c.execute('''CREATE TABLE file_names
             (file_name text, word text, classification text)''')
	conn.commit()
except:
	c.execute('''delete from file_names''')
	conn.commit()

data = []
with open('ISLEX.csv', 'rb') as csvfile:
	file_names = csv.reader(csvfile, delimiter=';', quotechar='"')
	for file_name in file_names:
		data.append(tuple(file_name))

print data[0]

c.executemany('insert into file_names values (?,?,?)', data)
conn.commit()