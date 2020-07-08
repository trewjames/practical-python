# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None) -> list:
    '''Parse a csv file into a list of records'''

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)

        if select is None:
            select = header
        indices = [header.index(key) for key in select]

        records = []
        for row in rows:
            if not row:
                continue
            record = {key: row[index] for key, index in zip(select, indices)}
            records.append(record)
        return records


portfolio = parse_csv('Data/portfolio.csv', select=['name'])
print(portfolio)

'''
Useful terminal commands:

python -i fileparse.py
portfolio = parse_csv('Data/portfolio.csv', select = ['name', 'shares'])

'''
