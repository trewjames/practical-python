#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
from fileparse import parse_csv


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    select = ['name', 'shares', 'price']
    types = [str, int, float]

    portfolio = parse_csv(filename, select=select, types=types)

    # with open(filename, 'rt') as f:
    #     lines = csv.reader(f)
    #     header = next(lines)

    #     for line in lines:
    #         record = dict(zip(header, line))
    #         converted_record = {
    #             'name': record['name'],
    #             'shares': int(record['shares']),
    #             'price': float(record['price'])
    #         }
    #         portfolio.append(converted_record)
    return portfolio


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''

    types = [str, float]
    prices = parse_csv(filename, types=types, has_headers=False)

    # prices = {}
    # with open(filename, 'rt') as f:
    #     lines = csv.reader(f)

    #     for line in lines:
    #         try:
    #             prices[line[0]] = float(line[1])
    #         except IndexError:
    #             continue
    return dict(prices)


def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''

    report = []
    for item in portfolio:
        current_price = prices[item['name']]
        price_change = round(current_price - item['price'], 2)
        summary = (item['name'], item['shares'], current_price, price_change)
        report.append(summary)
    return report


def print_report(reportdata):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''

    header = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % header)
    print(('-' * 10 + ' ') * len(header))
    for line in reportdata:
        print("%10s %10d %10.2f %10.2f" % line)


def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    print_report(report)
    print()


def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} portfile pricefile')
    portfolio_report(args[1], args[2])


if __name__ == "__main__":
    import sys
    main(sys.argv)
