# pcost.py
#
# # Exercise 1.27
# import csv
from report import read_portfolio


def portfolio_cost(fname):
    ''' Returns the cost of a portfolio '''

    portfolio = read_portfolio(fname)
    cost = sum([s.shares * s.price for s in portfolio])
    return round(cost, 2)


def main(args):
    if len(args) != 2:
        raise SystemExit(f"Usage: {args[0]} filename")
    fname = args[1]
    print(f"Total cost: ${portfolio_cost(fname)}")


if __name__ == "__main__":
    import sys
    main(sys.argv)
