class Product:
    """Represents a product in the inventory."""

    def __init__(self, product_id, name, category, price, quantity, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def add_stock(self, amount):
        """Add stock to the product."""
        if amount > 0:
            self.quantity += amount
            print("Stock added successfully.")
        else:
            print("Invalid quantity.")

    def remove_stock(self, amount):
        """Remove stock from the product."""
        if amount <= 0:
            print("Invalid quantity.")
        elif amount > self.quantity:
            print("Not enough stock available.")
        else:
            self.quantity -= amount
            print("Stock removed successfully.")

    def display(self):
        """Display product information."""
        print(
            f"{self.product_id:<10}"
            f"{self.name:<20}"
            f"{self.category:<15}"
            f"{self.price:<12.2f}"
            f"{self.quantity:<10}"
            f"{self.supplier:<20}"
        )


class Inventory:
    """Manages all products in the inventory."""

    def __init__(self):
        self.products = []

    def add_product(self):
        """Add a new product."""
        try:
            product_id = int(input("Enter Product ID: "))

            if self.find_product(product_id):
                print("Product ID already exists.")
                return

            name = input("Enter Product Name: ")
            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))
            supplier = input("Enter Supplier Name: ")

            if price < 0 or quantity < 0:
                print("Price and quantity cannot be negative.")
                return

            product = Product(
                product_id,
                name,
                category,
                price,
                quantity,
                supplier
            )

            self.products.append(product)
            print("Product added successfully.")

        except ValueError:
            print("Invalid input. Please enter the correct data type.")

    def display_products(self):
        """Display all products."""
        if not self.products:
            print("\nNo products available.")
            return

        print("\n" + "=" * 87)
        print("                         INVENTORY")
        print("=" * 87)

        print(
            f"{'ID':<10}"
            f"{'Name':<20}"
            f"{'Category':<15}"
            f"{'Price':<12}"
            f"{'Quantity':<10}"
            f"{'Supplier':<20}"
        )

        print("-" * 87)

        for product in self.products:
            product.display()

    def find_product(self, product_id):
        """Find a product using its ID."""
        for product in self.products:
            if product.product_id == product_id:
                return product

        return None

    def search_product(self):
        """Search for a product."""
        try:
            product_id = int(input("\nEnter Product ID to search: "))
            product = self.find_product(product_id)

            if product:
                print("\nProduct Found")
                print("-" * 40)
                print(f"Product ID: {product.product_id}")
                print(f"Product Name: {product.name}")
                print(f"Category: {product.category}")
                print(f"Price: {product.price:.2f}")
                print(f"Quantity: {product.quantity}")
                print(f"Supplier: {product.supplier}")
            else:
                print("Product not found.")

        except ValueError:
            print("Invalid Product ID.")

    def update_product(self):
        """Update product information."""
        try:
            product_id = int(input("\nEnter Product ID to update: "))
            product = self.find_product(product_id)

            if not product:
                print("Product not found.")
                return

            name = input("Enter new Product Name: ")
            category = input("Enter new Category: ")
            price = float(input("Enter new Price: "))
            supplier = input("Enter new Supplier: ")

            if price < 0:
                print("Price cannot be negative.")
                return

            product.name = name
            product.category = category
            product.price = price
            product.supplier = supplier

            print("Product updated successfully.")

        except ValueError:
            print("Invalid input.")

    def delete_product(self):
        """Delete a product."""
        try:
            product_id = int(input("\nEnter Product ID to delete: "))
            product = self.find_product(product_id)

            if product:
                self.products.remove(product)
                print("Product deleted successfully.")
            else:
                print("Product not found.")

        except ValueError:
            print("Invalid Product ID.")

    def add_stock(self):
        """Increase product stock."""
        try:
            product_id = int(input("\nEnter Product ID: "))
            product = self.find_product(product_id)

            if product:
                amount = int(input("Enter quantity to add: "))
                product.add_stock(amount)
            else:
                print("Product not found.")

        except ValueError:
            print("Invalid input.")

    def remove_stock(self):
        """Decrease product stock."""
        try:
            product_id = int(input("\nEnter Product ID: "))
            product = self.find_product(product_id)

            if product:
                amount = int(input("Enter quantity to remove: "))
                product.remove_stock(amount)
            else:
                print("Product not found.")

        except ValueError:
            print("Invalid input.")

    def low_stock_report(self):
        """Display products with low stock."""
        low_stock_limit = 5
        found = False

        print("\n========== LOW STOCK REPORT ==========")

        for product in self.products:
            if product.quantity <= low_stock_limit:
                print(
                    f"ID: {product.product_id} | "
                    f"Name: {product.name} | "
                    f"Quantity: {product.quantity}"
                )
                found = True

        if not found:
            print("No products have low stock.")

    def calculate_inventory_value(self):
        """Calculate total value of inventory."""
        total_value = 0

        for product in self.products:
            total_value += product.price * product.quantity

        print(f"\nTotal Inventory Value: ${total_value:.2f}")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 45)
    print("       INVENTORY MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Product")
    print("2. Display All Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Add Stock")
    print("7. Remove Stock")
    print("8. Low Stock Report")
    print("9. Calculate Inventory Value")
    print("10. Exit")
    print("=" * 45)


def main():
    """Main program."""
    inventory = Inventory()

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                inventory.add_product()

            elif choice == 2:
                inventory.display_products()

            elif choice == 3:
                inventory.search_product()

            elif choice == 4:
                inventory.update_product()

            elif choice == 5:
                inventory.delete_product()

            elif choice == 6:
                inventory.add_stock()

            elif choice == 7:
                inventory.remove_stock()

            elif choice == 8:
                inventory.low_stock_report()

            elif choice == 9:
                inventory.calculate_inventory_value()

            elif choice == 10:
                print("\nThank you for using the Inventory Management System.")
                break

            else:
                print("Invalid choice. Please select 1-10.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
