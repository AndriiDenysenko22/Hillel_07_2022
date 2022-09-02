import csv
import json


with open('task_16.json', 'r') as old_file:
    file_content = old_file.read()
    templates = json.loads(file_content)
    keys = templates.keys()
    values = templates.values()
    studs_id = list(keys)

    data = list(values)

    phone_numbers = ['phone', '0991112233', '0661122233', '0675151819', '0441874359', '0952139711', '0635436819']
    row_0 = ['id   ', 'Name', 'Age']
    row_1 = [studs_id[0], data[0][0], str(data[0][1])]
    row_2 = [studs_id[1], data[1][0], str(data[1][1])]
    row_3 = [studs_id[2], data[2][0], str(data[2][1])]
    row_4 = [studs_id[3], data[3][0], str(data[3][1])]
    row_5 = [studs_id[4], data[4][0], str(data[4][1])]
    row_6 = [studs_id[5], data[5][0], str(data[5][1])]

    row_0.append(phone_numbers[0])
    row_1.append(phone_numbers[1])
    row_2.append(phone_numbers[2])
    row_3.append(phone_numbers[3])
    row_4.append(phone_numbers[4])
    row_5.append(phone_numbers[5])
    row_6.append(phone_numbers[6])
    print(row_0)
    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)
    print(row_5)
    print(row_6)

    with open('task_17.csv', mode='w', encoding='utf-8', newline='') as new_file:
        file_writer = csv.writer(new_file)
        for item in (row_0, row_1, row_2, row_3, row_4, row_5, row_6):
            file_writer.writerow(item)
