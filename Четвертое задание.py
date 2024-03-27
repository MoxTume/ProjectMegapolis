import csv
with open('history_mirror.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=','))
    use_date = {}
    for row in reader:
            year = row['date'].split('-')[0]
            use_date[year] = use_date.get(year, 0) + 1
for i in range(2000, 2024):
    print(f"В {i} году зеркало было использовано {use_date[str(i)]}.")
