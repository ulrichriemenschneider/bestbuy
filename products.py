class Product:
    """Class for initializing products with some example functions and methods"""

    def __init__(self, name, price, quantity):
        """Initializes a new Product instance."""
        self.name = self.check_valid_name(name)
        self.price = self.check_valid_price(price)
        self.quantity = self.check_valid_quantity(quantity)
        self.active = True

    @staticmethod
    def check_valid_name(name) -> str:
        """Validates the product name."""
        if name and name.strip():
            return name
        else:
            raise ValueError("Name cannot be empty")

    @staticmethod
    def check_valid_price(price) -> float:
        """Validates the product price."""
        if isinstance(price, (int, float)) and price >= 0:
            return float(price)
        else:
            raise ValueError("Price must be a non-negative number")

    @staticmethod
    def check_valid_quantity(quantity) -> int:
        """Validates the product quantity."""
        if isinstance(quantity, int) and quantity >= 0:
            return quantity
        else:
            raise ValueError("Quantity must be a non-negative integer")

    def set_quantity(self, quantity):
        """Sets the quantity of the product."""
        new_quantity = self.check_valid_quantity(quantity)
        self.quantity = new_quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def is_active(self):
        """Checks if the product is active."""
        return self.active

    def show(self):
        """Prints the details of the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """Buys a given quantity of the product.
        Updates the total quantity and returns the total price of the added items."""
        buy_quantity = self.check_valid_quantity(quantity)
        self.set_quantity(self.quantity + buy_quantity)
        return f"Total price: {self.price * buy_quantity}"
