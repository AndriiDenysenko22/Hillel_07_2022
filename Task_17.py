import csv
import json

with open('task_16.json', 'r') as old_file:
    file_content = old_file.read()
    templates = json.loads(file_content)
    keys = templates.keys()
    values = templates.values()
    studs_id = list(keys)
    studs_id.insert(0, 'id')
    data = list(values)
    data.insert(0, ['Name', 'Age'])
phone_numbers = ['phone', '0991112237', '0661122233', '0675151819', '0441874359', '0952139711', '0635436819']

with open('task_17.csv', mode='w', encoding='utf-8', newline='') as new_file:
    file_writer = csv.writer(new_file)
    for i, element in enumerate(data):
        row_i = [studs_id[i], data[i][0], str(data[i][1]), phone_numbers[i]]
        file_writer.writerow(row_i)
        print(row_i)
