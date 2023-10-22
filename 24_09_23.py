with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
    for line in file.readlines():
        data = line.split(';')
        if data[5] == 'UA':
            print(data[2])
