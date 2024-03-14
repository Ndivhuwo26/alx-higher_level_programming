Python - import & modules

Modules: A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py. Modules can contain variables, functions, and classes. They allow for code organization and reusability.

Importing Modules:

You can import an entire module using the import statement followed by the module name.
For example: import math, import random, import os.
Using Imported Modules:

After importing a module, you can use its functions, classes, and variables by referencing them using dot notation.
For example: math.sqrt(25), random.randint(1, 10), os.getcwd().
Importing Specific Objects:

You can import specific objects from a module using the from keyword.
For example: from math import sqrt, from random import randint.
Aliasing Modules and Objects:

You can use the as keyword to alias modules and objects, providing shorter names or avoiding naming conflicts.
For example: import numpy as np, from math import sqrt as square_root.
Importing All Objects from a Module:

You can import all objects from a module using the * wildcard.
For example: from math import *.
Custom Modules:

You can create your own modules by organizing related code into a .py file and importing it into other scripts.
For example: Create a file my_module.py containing Python code and import it using import my_module.
Standard Library:

Python comes with a rich set of standard libraries/modules that provide various functionalities, such as math operations, file I/O, networking, etc.
These modules can be imported and used in your Python scripts without additional installations.
Using import and modules allows you to leverage existing code, organize your codebase, and build upon the functionality provided by Python's standard library or third-party packages. It promotes code reusability and maintainability in Python projects.

