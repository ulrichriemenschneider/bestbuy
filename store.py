class Store:
    """Class for initializing a store with some example functions and methods"""

    def __init__(self, product_list):
        """Initializes a new Store instance."""
        self.product_list = product_list

    def add_product(self, product):
        """Adds a product to the store."""
        self.product_list.append(product)
        print("Product added to the store.")

    def remove_product(self, product):
        """Removes a product from the store."""
        if product in self.product_list:
            self.product_list.remove(product)
            print("Product removed from the store.")
        else:
            print("Product could not be found!!!")

    def get_total_quantity(self) -> int:
        """Returns the total number of items available in the store."""
        count = 0
        for product in self.product_list:
            count += product.quantity
        return count

    def get_all_products(self):
        """Returns all products in the store that are active."""
        active_list = []
        for product in self.product_list:
            if product.active:
                active_list.append(product)
        return active_list

    @staticmethod
    def order(shopping_list) -> float:
        """Receives a list of tuples, each tuple containing two elements:
        Product (product class) and quantity (int).
        Purchases the products and returns the total price of the order."""
        total_price = 0.0
        for product, quantity in shopping_list:
            product.buy(quantity)
            total_price += product.price * quantity
        return f"Order made! Order cost: ${total_price:.2f}."
