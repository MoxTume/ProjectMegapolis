import csv
with open('songs.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=','))[1:]
    for row in reader:
        print(row['name'], row['artist'], row[''])
