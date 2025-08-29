# OOP Assignment - Step-by-Step

# This file will contain the Python code for the assignment.
# Each part of the assignment will be added here sequentially.

# --- Assignment 1: Design Your Own Class! ---

# We are creating a class called `Smartphone` to represent a mobile phone.
# A class is a blueprint for creating objects.

class Smartphone:
    # This is the constructor method, called when a new object is created.
    # It initializes the attributes of the object.
    def __init__(self, brand, model, battery=100):
        # These are the attributes (or properties) of a Smartphone object.
        self.brand = brand  # The brand of the smartphone (e.g., "Apple")
        self.model = model  # The model of the smartphone (e.g., "iPhone 14")
        self.battery = battery  # The battery level, with a default value of 100

    # This is a method that simulates making a phone call.
    def make_call(self, contact_name):
        # It checks if the battery is sufficient to make a call.
        if self.battery > 10:
            self.battery -= 10  # Decrease battery by 10% after a call
            print(f"Calling {contact_name}... Your battery is now {self.battery}%.")
        else:
            print("Battery too low to make a call. Please charge your phone.")

    # This method simulates charging the phone.
    def charge_battery(self):
        self.battery = 100  # Reset battery level to 100%
        print(f"Charging complete. Your {self.brand} {self.model} is fully charged.")

# --- Example Usage ---
# We create an instance (object) of the Smartphone class.
my_phone = Smartphone("Samsung", "Galaxy S23")

# We can access the attributes of the object.
print(f"My new phone is a {my_phone.brand} {my_phone.model}.")
print(f"Initial battery level: {my_phone.battery}%")

# We can call the methods of the object.
my_phone.make_call("Mokwa")
my_phone.charge_battery()