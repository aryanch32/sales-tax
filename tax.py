import math
from models import BasketItem

class TaxCalculator:
    BASIC_TAX_RATE = 0.10
    IMPORT_DUTY = 0.05

    def __init__(self):
        pass

    def calculate_tax(self, item: BasketItem) -> float:
        tax = 0.0
        if not item.product.is_exempt:
            tax += item.shelf_price * self.BASIC_TAX_RATE
        if item.product.is_imported:
            tax += item.shelf_price * self.IMPORT_DUTY
        return self._round_tax(tax)

    def _round_tax(self, tax: float) -> float:
        return math.ceil(tax * 20) / 20.0