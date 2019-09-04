
class PlayerResources():
    def __init__(self, cash, purchases=None):
        self.cash = cash
        if purchases is None:
            self.purchases = []
        else:
            self.purchases = purchases
