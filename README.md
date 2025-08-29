# OOP Assignment in Python

This repository contains the solution to the OOP assignment, completed step-by-step with clear explanations and beginner-friendly code.

## Description

The project demonstrates core Object-Oriented Programming (OOP) concepts such as classes, objects, inheritance, and polymorphism through a series of assignments.

## Installation

To run this project, you need Python installed on your system. No external libraries are required.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mokwathedeveloper/python_wk5_assigment.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd python_wk5_assigment
   ```

## Usage

You can run the Python script directly from your terminal:

```bash
python assignment.py
```

This will execute the code and display the output from the different assignment parts.

### Example Output

```
--- Smartphone Example ---
My new phone is a Samsung Galaxy S23.
Initial battery level: 100%
Calling Mokwa... Your battery is now 90%.
Charging complete. Your Samsung Galaxy S23 is fully charged.

--- Gaming Smartphone Example ---
My new gaming phone is a Asus ROG Phone 8.
Gaming mode activated! Active Cooling is now running.
Cannot make calls while in gaming mode.

--- Polymorphism Example ---
Driving 🚗
Flying ✈️
```

## OOP Concepts Explained

This project demonstrates the following Object-Oriented Programming principles:

### 1. Encapsulation

Encapsulation is the bundling of data (attributes) and methods that operate on the data into a single unit (a class). It restricts direct access to some of an object's components, which is a means of preventing accidental interference and misuse of the methods.

- **In this project:** The `GamingSmartphone` class encapsulates the `_is_gaming_mode` attribute. It is marked with a leading underscore to indicate that it is intended for internal use. The `activate_gaming_mode` method provides controlled access to modify this attribute.

### 2. Inheritance

Inheritance is a mechanism where a new class (subclass or derived class) inherits attributes and methods from an existing class (superclass or base class). This promotes code reusability.

- **In this project:** The `GamingSmartphone` class inherits from the `Smartphone` class. It automatically gains the `brand`, `model`, `battery` attributes and the `charge_battery` method from its parent, and then adds its own unique features.

### 3. Polymorphism

Polymorphism means "many forms," and it allows objects of different classes to be treated as objects of a common superclass. It is the ability to present the same interface for differing underlying forms (data types).

- **In this project:** The `Car` and `Plane` classes both have a method called `move()`. Although the method has the same name, its implementation is different in each class. When we call `move()` on a `Car` object, it prints "Driving 🚗", and when called on a `Plane` object, it prints "Flying ✈️". This is a clear example of polymorphism.
