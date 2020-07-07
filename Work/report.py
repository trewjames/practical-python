# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        next(lines)

        for line in lines:
            line_dict = {
                'name': line[0],
                'shares': int(line[1]),
                'price': float(line[2])
            }
            portfolio.append(line_dict)

    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        lines = csv.reader(f)

        for line in lines:
            try:
                prices[line[0]] = float(line[1])
            except IndexError:
                continue
    return prices


def make_report(buy, sell):
    total_cost = 0
    total_value = 0
    report = []
    for item in buy:
        total_cost += item['shares'] * item['price']
        total_value += item['shares'] * sell[item['name']]
        price_change = round(sell[item['name']] - item['price'], 2)
        summary = [item['name'], item['shares'], item['price'], price_change]
        report.append(tuple(summary))

    header = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % header)
    print(('-' * 10 + ' ') * len(header))
    for line in report:
        print("%10s %10d %10.2f %10.2f" % line)
    return round(total_value - total_cost, 2)


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

print(make_report(portfolio, prices))
