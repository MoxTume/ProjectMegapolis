import csv
with open('history_mirror.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=','))[1:]
    for row in reader:
        print(f"{row['date']}, {row['username']}, {row['verdict']}")
