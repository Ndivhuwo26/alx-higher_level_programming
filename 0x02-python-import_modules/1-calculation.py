#!/usr/bin/python3

if __name__ == "__main__":
from calculator_1 import add, subtract, multiply, divide

a = 10
b = 5

print("Addition of {} and {} = {}".format(a, b, add(a, b)))
print("Subtraction of {} from {} = {}".format(b, a, subtract(a, b)))
print("Multiplication of {} and {} = {}".format(a, b, multiply(a, b)))
print("Division of {} by {} = {}".format(a, b, divide(a, b)))
