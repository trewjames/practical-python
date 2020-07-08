# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(fname):
    with open(fname, "rt") as f:
        lines = csv.reader(f)
        header = next(lines)

        data = [line for line in lines]

    cost = 0
    for index, field in enumerate(data, start=1):
        record = dict(zip(header, field))
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            cost += nshares * price
        except ValueError:
            print(f"Row {index}: Couldn't convert: {field}")
    return round(cost, 2)


if len(sys.argv) == 2:
    fname = sys.argv[1]
else:
    fname = "Data/portfoliodate.csv"

print(f"Total cost: {portfolio_cost(fname)}")
