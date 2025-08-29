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
            print(f"Calling {contact_name}... Your battery is now {self.battery}%")
        else:
            print("Battery too low to make a call. Please charge your phone.")

    # This method simulates charging the phone.
    def charge_battery(self):
        self.battery = 100  # Reset battery level to 100%
        print(f"Charging complete. Your {self.brand} {self.model} is fully charged.")

# --- Inheritance and Encapsulation ---

# We create a `GamingSmartphone` that inherits from `Smartphone`.
# This is an example of Inheritance, where a new class derives properties from an existing class.
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery=100, cooling_system="Active Cooling"):
        # `super()` calls the constructor of the parent class (`Smartphone`).
        super().__init__(brand, model, battery)
        # This is a new attribute specific to the GamingSmartphone.
        self.cooling_system = cooling_system
        # This attribute is "private" to demonstrate encapsulation.
        self._is_gaming_mode = False

    # This method is specific to the GamingSmartphone.
    def activate_gaming_mode(self):
        self._is_gaming_mode = True
        print(f"Gaming mode activated! {self.cooling_system} is now running.")

    # This method overrides the parent's `make_call` method.
    def make_call(self, contact_name):
        # It first checks if gaming mode is on.
        if self._is_gaming_mode:
            print("Cannot make calls while in gaming mode.")
        else:
            # If not in gaming mode, it uses the parent's `make_call` logic.
            super().make_call(contact_name)

# --- Example Usage ---
print("\n--- Smartphone Example ---")
my_phone = Smartphone("Samsung", "Galaxy S23")
print(f"My new phone is a {my_phone.brand} {my_phone.model}.")
print(f"Initial battery level: {my_phone.battery}%")
my_phone.make_call("Mokwa")
my_phone.charge_battery()

print("\n--- Gaming Smartphone Example ---")
my_gaming_phone = GamingSmartphone("Asus", "ROG Phone 8", battery=80)
print(f"My new gaming phone is a {my_gaming_phone.brand} {my_gaming_phone.model}.")
my_gaming_phone.activate_gaming_mode()
my_gaming_phone.make_call("Friend") # This call will be blocked
