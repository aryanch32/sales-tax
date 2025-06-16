from typing import List
from models import BasketItem
from tax import TaxCalculator

class Receipt:
    def __init__(self, items: List[BasketItem]):
        self.items = items
        self.tax_calculator = TaxCalculator()
        self.total_tax = 0.0
        self.total_price = 0.0

    def generate(self):
        lines = []
        for item in self.items:
            tax = self.tax_calculator.calculate_tax(item)
            total_price = (item.shelf_price + tax) * item.quantity
            self.total_tax += tax * item.quantity
            self.total_price += total_price
            name = f"{item.quantity} {'imported ' if item.product.is_imported else ''}{item.product.name}"
            lines.append(f"{name}: {total_price:.2f}")
        return lines

    def print_receipt(self):
        lines = self.generate()
        for line in lines:
            print(line)
        print(f"Sales Taxes: {self.total_tax:.2f}")
        print(f"Total: {self.total_price:.2f}")