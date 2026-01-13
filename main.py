import store
import products


def start(best_buy):
    """Starts the user interface for the store."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = int(input("Please enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            all_products = best_buy.get_all_products()
            print("\n------ Products ------")
            for product in all_products:
                product.show()
            print("----------------------")

        elif choice == 2:
            total_quantity = best_buy.get_total_quantity()
            print(f"\nTotal amount in store: {total_quantity}")

        elif choice == 3:
            shopping_list = []
            all_products = best_buy.get_all_products()

            print("\n------ Products ------")
            for i, product in enumerate(all_products):
                print(
                    f"{i + 1}. {product.name} (Price: {product.price}, Qty: {product.quantity})"
                )
            print("----------------------")

            print("\nWhen you are finished, enter empty text.")

            while True:
                product_index_input = input("Which product # do you want? ")

                if product_index_input == "":
                    break

                try:
                    product_index = int(product_index_input) - 1
                    if 0 <= product_index < len(all_products):
                        qty_input = input("What amount do you want? ")
                        qty = int(qty_input)

                        # Add validation if needed, or rely on Store/Product to handle invalid logic
                        # But simpler validation here is better for UI experience
                        if qty > 0:
                            shopping_list.append((all_products[product_index], qty))
                            print("Product added to list!")
                        else:
                            print("Invalid quantity. Must be positive.")
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Error adding product. Please enter valid numbers.")

            if shopping_list:
                try:
                    result = best_buy.order(shopping_list)
                    print(f"\n{result}")
                except Exception as exc:
                    print(f"Error processing order: {exc}")
            else:
                print("Order cancelled (empty list).")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-4.")


def main():
    """setup initial stock of inventory"""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
