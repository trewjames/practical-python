class Stock:
    ''' An stock object with name, shares, and price'''

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = int(shares)
        self.price = float(price)

    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt
