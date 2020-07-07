# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(fname):
    with open(fname, "rt") as f:
        lines = csv.reader(f)
        next(lines)

        data = [line for line in lines]

    cost = 0
    for field in data:
        try:
            cost += int(field[1]) * float(field[2])
        except ValueError:
            print("Missing data")
    return round(cost, 2)


if len(sys.argv) == 2:
    fname = sys.argv[1]
else:
    fname = "Data/portfolio.csv"

print(f"Total cost: {portfolio_cost(fname)}")
