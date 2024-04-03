Python - Classes and Objects


A class is a template or blueprint for creating objects. It defines the properties and behaviors that objects of that class will have.
Classes are declared using the class keyword followed by the class name and a colon.

Object (Instance):

An object is an instance of a class. It is a concrete realization of the class blueprint, with its own unique data and behavior.
You create objects (instances) of a class by calling the class as if it were a function.

Attributes:

Attributes are variables that belong to objects. They store data associated with the object.
Attributes are defined inside the class definition and accessed using dot notation (obj.attribute). They can be class attributes (shared by all instances) or instance attributes (specific to each instance).
Methods:

Methods are functions defined within a class that operate on objects of that class.
They define the behavior of the objects. Methods can access and modify the object's attributes.
The first parameter of a method is always self, which refers to the instance of the class. It allows methods to access instance attributes and other methods.
Constructor (__init__ method):

The __init__ method is a special method called when an object is created.
It initializes the object's attributes. It's commonly used to set initial values for instance variables.



Encapsulation:

Encapsulation is the bundling of data (attributes) and methods that operate on that data within a single unit (class).
It helps in organizing and controlling access to the data, preventing accidental modification from outside the class.
Inheritance:

Inheritance is a mechanism where a new class (subclass) can inherit attributes and methods from an existing class (superclass).
The subclass can extend or modify the behavior of the superclass. It promotes code reusability and enables hierarchical relationships between classes.
Polymorphism:

Polymorphism allows objects of different classes to be treated as objects of a common superclass.
It enables flexibility in method invocation, allowing methods to behave differently based on the object's type.
Polymorphism is achieved through method overriding and method overloading.
