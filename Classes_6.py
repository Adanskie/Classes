class IcecreamStand:
    def __init__(self,*flavors):
        self.flavors = flavors


class Restaurant(IcecreamStand):
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant's name and cuisine type."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.customers_served = 0  # Initializing the number of customers served
        self.flavors = IcecreamStand("chocolate","banana","apple")

    def describe_restaurant(self):
        """Print the restaurant's name and cuisine type."""
        print(f"{self.name} offers {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.name} is now open!")

    def set_number(self, number):
        """Set the number of customers served."""
        self.customers_served = number

    def print_customers_served(self):
        """Print the number of customers served."""
        print(f"{self.name} has served {self.customers_served} customers.")

    def Ice_cream(self):
        print(f"The flavors of ice cream is {self.flavors.flavors}")

# Create a restaurant instance
my_restaurant = Restaurant("Tasty Bites", "Italian")
my_restaurant.Ice_cream()
