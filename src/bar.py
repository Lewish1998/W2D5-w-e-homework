class Bar:

    def __init__(self, till):
        self.till = till
        self.drinks = {
            'Tennents': 4.50,
            'Buckfast': 1.00,
            'Magners': 3.75
            }

    def sell_drink(self, drink, customer):
        self.till += self.drinks[drink]
        customer.cash -= self.drinks[drink]
