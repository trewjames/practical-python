from typedproperty import *


class Stock:
    ''' An stock object with name, shares, and price'''

    name = string('name')
    shares = integer('shares')
    price = float_('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def sell(self, amt):
        self.shares -= amt

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
