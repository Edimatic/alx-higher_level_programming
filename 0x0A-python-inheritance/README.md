			================Python - Inheritance=============

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit properties and behaviors (attributes and methods) from another class. The class that is being inherited from is called the "parent" or "base" class, and the class that inherits is called the "child" or "derived" class.

Here are key points about inheritance in Python:


Syntax for Inheritance:
In Python, the syntax for inheritance is straightforward. When defining a class, you can specify its parent class in parentheses after the class name.


Code Reusability:
Inheritance promotes code reusability by allowing the child class to inherit the attributes and methods of the parent class. This means that common functionalities can be defined in a base class, and subclasses can reuse or override them as needed.


Method Overriding:
A child class can override methods inherited from the parent class. This allows the child class to provide its own implementation for a specific method while still benefiting from other methods of the parent class.


Access to Parent Class Members:
The child class has access to both the public and protected members of the parent class. However, private members are not directly accessible in the child class.


Multiple Inheritance:
Python supports multiple inheritance, allowing a class to inherit from more than one parent class. This can lead to complex class hierarchies and should be used with caution.


Super() Function:
The super() function is often used in child classes to call methods from the parent class. It provides a way to invoke methods from the superclass in a clean and maintainable manner.
