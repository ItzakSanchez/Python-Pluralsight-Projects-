from abs_strategy import AbstractStrategy

class PostalServiceStrategy(AbstractStrategy):

    def calculate(self,order):
        return 5.00