from parsers import InputParser
from receipt import Receipt


def run_shopping_basket(raw_lines):
    parser = InputParser()
    items = parser.parse_input(raw_lines)
    receipt = Receipt(items)
    receipt.print_receipt()


if __name__ == "__main__":
    print("\nOutput 1:")
    run_shopping_basket([
        "1 book at 12.49",
        "1 music CD at 14.99",
        "1 chocolate bar at 0.85"
    ])

    print("\nOutput 2:")
    run_shopping_basket([
        "1 imported box of chocolates at 10.00",
        "1 imported bottle of perfume at 47.50"
    ])

    print("\nOutput 3:")
    run_shopping_basket([
        "1 imported bottle of perfume at 27.99",
        "1 bottle of perfume at 18.99",
        "1 packet of headache pills at 9.75",
        "1 box of imported chocolates at 11.25"
    ])