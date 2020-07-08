import csv

with open('Work/Data/dowstocks.csv', 'rt') as f:
    rows = csv.reader(f)
    header = next(rows)
    types = [
        str, float, tuple, str, float,
        float, float, float, int
    ]
    for row in rows:
        row[2] = map(int, row[2].split('/'))
        converted = {
            name: func(val) for name, func, val
            in zip(header, types, row)
        }
        print(converted)
