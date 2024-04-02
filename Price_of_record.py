class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.code] = product

    def display_menu(self):
        print("Product Menu:")
        for code, product in self.products.items():
            print(f"{code}: {product.name} - ${product.price}")

    def generate_bill(self, quantities):
        total_amount = 0
        print("\n\nBill:")
        print("---------------------")
        for code, quantity in quantities.items():
            if code in self.products:
                product = self.products[code]
                amount = product.price * quantity
                total_amount += amount
                print(f"{product.name} x {quantity}: ${amount}")
        print("---------------------")
        print(f"Total Amount: ${total_amount}")


def main():
    inventory = Inventory()


    inventory.add_product(Product("001", "T-Shirt", 15.99))
    inventory.add_product(Product("002", "Jeans", 29.99))
    inventory.add_product(Product("003", "Sneakers", 49.99))

  
    inventory.display_menu()

    quantities = {}
    for code in inventory.products.keys():
        quantity = int(input(f"Enter quantity for product {code}: "))
        quantities[code] = quantity


    inventory.generate_bill(quantities)


if __name__ == "__main__":
    main()
