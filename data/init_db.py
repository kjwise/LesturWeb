import csv, json

json_data = {}
with open('ISLEX.csv', 'rb') as csvfile:
    file_names = csv.reader(csvfile, delimiter=';', quotechar='"')
    for file_name in file_names:
        json_data[file_name[1]] = file_name[0];

with open('../static/data/data.json', 'w+') as outfile:
    json.dump(json_data, outfile)
