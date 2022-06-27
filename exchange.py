class Currency:

    currencies = {'CHF': 0.930023,  # swiss franc
                  'CAD': 1.264553,  # canadian dollar
                  'GBP': 0.737414,  # british pound
                  'JPY': 111.019919,  # japanese yen
                  'EUR': 0.862361,  # euro
                  'USD': 1.0}  # us dollar

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        self.value = (
            self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    # add magic methods here
    def __repr__(self):
        return Currency.__str__(self)
    # This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.

    def __str__(self):
        # This method returns the same value as __repr__(self).
        return f'{self.value} {self.unit}'

    def __add__(self, other):
        # Defines the '+' operator. If other is a Currency object, the currency values are added and the result will be the unit of self. If other is an int or a float,
        # other will be treated as a USD value.
        return Currency.__radd__(self, other)

    def __iadd__(self, other):
        return Currency.__add__(self, other)

    def __radd__(self, other):
        
        if isinstance(other, Currency) and other.unit == self.unit:
            return Currency(self.value + other.value, self.unit)
        elif isinstance(other, Currency) and other.unit != self.unit:
            convert_other = (
                other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
            return Currency(convert_other + self.value, self.unit)
        elif isinstance(other, int) or isinstance(other, float):
            other_intial = Currency(other, 'USD')
            convert_initial = (other_intial.value / 
                Currency.currencies[other_intial.unit] *
                Currency.currencies[self.unit])
            return Currency(self.value + convert_initial, self.unit), 'other is a num'
        
        else:
            print('must be number or another currency to add')
            return self.value, self.unit

    def __sub__(self, other):
        if isinstance(other, Currency):
            return Currency(self.value - other.value, self.unit)
        elif isinstance(other, int) or isinstance(other, float):
            return Currency(self.value - other, self.unit)
        else:
            print('must be number or another currency to add')
            return self.value, self.unit

    def __rsub__(self, other_num):
        return Currency(other_num - self.value, self.unit)


v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print('1', v1 + v2)
print('2', v2 + v1)
print('3', v1 + 3)
# an int or a float is considered to be a USD value
print('4', 3 + v1)
print('5', v1 - 3)
# print(v1 - v2)
#  # an int or a float is considered to be a USD value
print('6', 30 - v2)

# print(type(1.1))
