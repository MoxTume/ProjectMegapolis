import csv
with open('history_mirror.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=','))
    mn_age = 10000
    pred = []
    for row in reader:
        if row['verdict'] == 'Победа над смертью':
            surname, name, otch = row['username'].split(' ')
            age = row['date'].split('-')[0]
            pred.append(f"{row['date']}, {row['username']}")
            if int(age) < mn_age:
                mn_age = int(age)
                mn_date = row['date']
                mn_fullname = f"{surname} {name[0]}.{otch[0]}."
    print(f"Сообщение было зафиксировано: {mn_date} у пользователя {mn_fullname}")
with open('mirror_error.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['date', 'username'])
    for i in pred:
        writer.writerows([i.split(',')])
