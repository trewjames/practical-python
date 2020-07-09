# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(lines, select=None, types=None, has_headers=True,
              delimiter=',', silence_errors=False) -> list:
    '''Parse a csv file into a list of records'''

    if select and not has_headers:
        raise RuntimeError('select requires column headers.')
    if not isinstance(lines, list):
        raise TypeError('Please pass a list of lines.')

    rows = csv.reader(lines, delimiter=delimiter)

    if has_headers:
        headers = next(rows)
        if select:
            indices = [headers.index(key) for key in select]
            headers = select

    records = []
    for rowNum, row in enumerate(rows):
        if not row:
            continue

        if select:
            row = [row[index] for index in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as err:
                if not silence_errors:
                    print(f"Conversion error. Reason {err}")
                    print(f"Row {rowNum}: {row}")
                continue

        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)
    return records


'''
Useful terminal commands:

python -i fileparse.py
portfolio = parse_csv('Data/portfolio.csv', select = ['name', 'shares'])

'''
