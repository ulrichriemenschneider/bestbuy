class Product:

    def __init__(self, name, price, quantity):
        self.name = Product.check_valid_name(name)
        self.price = Product.check_valid_price(price)
        self.quantity = Product.check_valid_quantity(quantity)
        self.active = True

    def check_valid_name(name) -> str:
        if name != "":
            return name
        else:
            raise ValueError("NameError")

    def check_valid_price(price) -> float:
        try:
            if type(price) is float and price > 0:
                return price
            elif type(price) is int and price > 0:
                return float(price)
            else:
                raise ValueError("PriceError")
        except ValueError:
            print("ValueError for price!")

    def check_valid_quantity(quantity) -> int:
        try:
            if type(quantity) is int and quantity >= 0:
                return int(quantity)
            else:
                raise ValueError("QuantityError")
        except ValueError:
            print("ValueError for quantity!")

    def set_quantity(self, quantity):
        try:
            if quantity == 0:
                self.deactivate()
                self.quantity = 0
            if quantity > 0 and self.is_active():
                self.quantity = quantity
            else:
                self.quantity = quantity
                self.active = True
        except:
            raise ValueError("Wrong type of value")

    def get_quantity(self) -> int:
        return self.quantity

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def is_active(self):
        return self.active

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        Product.check_valid_quantity(quantity)
        self.set_quantity(self.quantity + quantity)
        return f"Total price: {self.price * quantity}"


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
