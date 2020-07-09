# pcost.py
#
# # Exercise 1.27
# import csv
from report import read_portfolio


def portfolio_cost(fname):
    ''' Returns the cost of a portfolio '''

    portfolio = read_portfolio(fname)
    cost = sum([row['shares'] * row['price'] for row in portfolio])

    # with open(fname, "rt") as f:
    #     lines = csv.reader(f)
    #     header = next(lines)

    #     data = [line for line in lines]

    # cost = 0
    # for index, field in enumerate(data, start=1):
    #     record = dict(zip(header, field))
    #     try:
    #         nshares = int(record['shares'])
    #         price = float(record['price'])
    #         cost += nshares * price
    #     except ValueError:
    #         print(f"Row {index}: Couldn't convert: {field}")
    return round(cost, 2)


def main(args):
    if len(args) != 2:
        raise SystemExit(f"Usage: {args[0]} filename")
    fname = args[1]
    print(f"Total cost: ${portfolio_cost(fname)}")


if __name__ == "__main__":
    import sys
    main(sys.argv)
