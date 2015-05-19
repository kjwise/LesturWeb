import sqlite3, csv, json

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
json_data = {}
with open('ISLEX.csv', 'rb') as csvfile:
    file_names = csv.reader(csvfile, delimiter=';', quotechar='"')
    for file_name in file_names:
        data.append(tuple(file_name))
        json_data[file_name[1]] = file_name[0];

with open('data.json', 'w+') as outfile:
    json.dump(json_data, outfile)


c.executemany('insert into file_names values (?,?,?)', data)
conn.commit()