class Stock:
    ''' An stock object with name, shares, and price'''

    __slots__ = ('name', '_shares', '_price')

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

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Expected a float or int")
        self._price = float(value)

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
