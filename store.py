import products


class Store:

    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        """Fügt dem Store ein Produkt hinzu."""
        pass

    def remove_product(self, product):
        """Entfernt ein Produkt aus dem Store."""
        pass

    def get_total_quantity(self) -> int:
        """Gibt zurück, wie viele Artikel insgesamt im Store vorhanden sind."""
        count = 0
        for product in self.product_list:
            count += product.quantity
        return count

    def get_all_products(self) -> List[Product]:
        """Gibt alle Produkte im Store zurück, die aktiv sind."""
        active_list = []
        for product in self.product_list:
            if product.active == True:
                active_list.append(product)
        return active_list

    def order(self, shopping_list) -> float:
        """Erhält eine Liste von Tupeln, wobei jedes Tupel zwei Elemente enthält:
        Produkt (Produktklasse) und Menge (int).
        Kauft die Produkte und gibt den Gesamtpreis der Bestellung zurück."""
        for product in shopping_list:
            products.product[0].buy(product[1])


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
