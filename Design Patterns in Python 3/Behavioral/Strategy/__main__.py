from order import Order
from fedex_strategy import FedExStrategy
from ups_strategy import UPSStrategy
from postal_service_strategy import PostalServiceStrategy
from shipping_calculator import ShippingCalculator

def main():

    order1 = Order()
    fedex_strategy_1 = FedExStrategy()
    fedex_calculator = ShippingCalculator(fedex_strategy_1)
    order1_cost = fedex_calculator.calculate_shipping_cost(order1)

    assert order1_cost == 3.00

    order2 = Order()
    usp_strategy_1 = UPSStrategy()
    ups_calculator = ShippingCalculator(usp_strategy_1)
    order2_cost = ups_calculator.calculate_shipping_cost(order2)

    assert order2_cost == 4.00

    order3 = Order()
    postal_service_strategy = PostalServiceStrategy()
    postal_service_calculator = ShippingCalculator(postal_service_strategy)
    order3_cost = postal_service_calculator.calculate_shipping_cost(order3)

    assert order3_cost == 5.00

    print("Tests passed")

if __name__ == "__main__":
    main()
