class ShippingCalculator:

    def __init__(self, strategy):
        self._strategy = strategy

    def calculate_shipping_cost(self, order):
        return self._strategy.calculate(order)