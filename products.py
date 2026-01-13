class Product:

    def __init__(self, name, price, quantity):
        self.name = self.check_valid_name(name)
        self.price = self.check_valid_price(price)
        self.quantity = self.check_valid_quantity(quantity)
        self.active = True

    @staticmethod
    def check_valid_name(name) -> str:
        if name and name.strip():
            return name
        else:
            raise ValueError("Name cannot be empty")

    @staticmethod
    def check_valid_price(price) -> float:
        if isinstance(price, (int, float)) and price >= 0:
            return float(price)
        else:
            raise ValueError("Price must be a non-negative number")

    @staticmethod
    def check_valid_quantity(quantity) -> int:
        if isinstance(quantity, int) and quantity >= 0:
            return quantity
        else:
            raise ValueError("Quantity must be a non-negative integer")

    def set_quantity(self, quantity):
        new_quantity = self.check_valid_quantity(quantity)
        self.quantity = new_quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

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
        buy_quantity = self.check_valid_quantity(quantity)
        self.set_quantity(self.quantity + buy_quantity)
        return f"Total price: {self.price * buy_quantity}"


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
