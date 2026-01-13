import products


class Store:

    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        """Adds a product to the store."""
        self.product_list.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        if product in self.product_list:
            self.product_list.remove(product)

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
            if product.active == True:
                active_list.append(product)
        return active_list

    def order(self, shopping_list) -> float:
        """Receives a list of tuples, each tuple containing two elements:
        Product (product class) and quantity (int).
        Purchases the products and returns the total price of the order."""
        total_price = 0.0
        for product, quantity in shopping_list:
            product.buy(quantity)
            total_price += product.price * quantity
        return f"Order cost: {total_price} dollars."


product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print([(products[0], 1), (products[1], 2)])
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))
print(best_buy.get_total_quantity())
