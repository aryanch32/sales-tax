import re
from models import BasketItem, Product

EXEMPT_KEYWORDS = ['book', 'chocolate', 'chocolates', 'pill', 'pills']

class InputParser:
    def parse_line(self, line: str) -> BasketItem:
        match = re.match(r'(\d+)\s(.+)\sat\s([\d.]+)', line.strip())
        if not match:
            raise ValueError(f"Invalid input line: {line}")
        quantity = int(match.group(1))
        name = match.group(2)
        price = float(match.group(3))

        is_imported = 'imported' in name
        is_exempt = any(word in name for word in EXEMPT_KEYWORDS)
        cleaned_name = name.replace("imported", "").strip()

        product = Product(cleaned_name, is_imported, is_exempt)
        return BasketItem(quantity, product, price)

    def parse_input(self, lines: list[str]) -> list[BasketItem]:
        return [self.parse_line(line) for line in lines if line.strip()]