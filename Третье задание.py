import csv
with open('history_mirror.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=','))
    user_input = input('Введите имя+отчество или команду stop\n')
    while user_input != 'stop':
        naideno = 0
        for row in reader:
            if user_input.split(' ')[0] in row['username'] and user_input.split(' ')[1] in row['username']:
                surname, name, otch = row['username'].split(' ')
                fullname = f"{surname} {name[0]}.{otch[0]}."
                print(f"Предсказание для {fullname} - {row['verdict']}")
                naideno = 1
        if naideno == 0:
            print("Вас не нашлось в записях")
        user_input = input('Введите фамилию+имя или команду stop')
