class ShoppingCart:
    def __init__(self):
        self.prices = []

    def add(self, price):
        self.prices.append(price)

    def calculate_total_price(self):
        print("prices", self.prices)
        return sum(self.prices)

    def has_discount(self):
        return sum(self.prices) >= 100

    def number_of_products(self):
        return len(self.prices)


class SomeConsumer():
    def do_stuff():
        shoppingCart = ShoppingCart()
        shoppingCart.add(100)
        print("other consumer", shoppingCart.calculate_total_price())


if __name__ == "__main__":
    shoppingCart = ShoppingCart()
    shoppingCart.add(10)
    print("number of products:", shoppingCart.number_of_products())
    print("total price:", shoppingCart.calculate_total_price())
    print("has discount:", shoppingCart.has_discount())
