import csv


with open('FIOandTelephone.csv', "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, ["FIO", 'Tel'])
    fio = input('Input FIO>> ')
    for i in reader:
        if fio == i['FIO']:
            print('Find!>> ', i['Tel'])
            break
    else:
        print('Not found!')
