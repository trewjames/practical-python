#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
from fileparse import parse_csv
import tableformat
from portfolio import Portfolio


def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries of Stock objects
    with keys name, shares, and price
    '''

    with open(filename) as lines:
        port = Portfolio.from_csv(lines, **opts)
    return port


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''

    types = [str, float]
    with open(filename) as lines:
        dictlist = dict(parse_csv(lines, types=types, has_headers=False))
    return dictlist


def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''

    report = []
    for item in portfolio:
        current_price = prices[item.name]
        price_change = round(current_price - item.price, 2)
        summary = (item.name, item.shares, current_price, price_change)
        report.append(summary)
    return report


def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''

    formatter.headings(['Name', 'Shares', 'Price', 'Change'])

    for name, shares, price, change in reportdata:
        rowdata = [name, shares, price, change]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
    print()


def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} portfile pricefile')
    portfolio_report(args[1], args[2])


if __name__ == "__main__":
    import sys
    main(sys.argv)


# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
