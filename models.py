class Product:
    def __init__(self, name: str, is_imported: bool, is_exempt: bool):
        self.name = name
        self.is_imported = is_imported
        self.is_exempt = is_exempt


class BasketItem:
    def __init__(self, quantity: int, product: Product, shelf_price: float):
        self.quantity = quantity
        self.product = product
        self.shelf_price = shelf_price