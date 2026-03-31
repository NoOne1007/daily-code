# class Cake:
#     def __init__(self, flavor, layers):
#         self.flavor = flavor
#         self.layers = layers

#     def describe(self):
#         return f"This is a {self.flavor} cake with {self.layers} layers."
    
# if __name__ == "__main__":
#     cake = Cake("chocolate", 3)
#     print(cake.describe())

#     cake_2 = Cake("vanilla", 2)
#     print(cake_2.describe())


from Arithmetic import *
class Calculator:
    def __init__(self):
        self.addition = Arithmetic.add()
        self.subtraction = Arithmetic.subtract()
        self.multiplication = Arithmetic.multiply()
        self.division = Arithmetic.divide()

    def perform_addition(self, a, b):
        return self.addition.add(a, b)
    def perform_subtraction(self, a, b):
        return self.subtraction.subtract(a, b)
    def perform_multiplication(self, a, b):
        return self.multiplication.multiply(a, b)
    def perform_division(self, a, b):
        return self.division.divide(a, b)
    

if __name__ == "__main__":
    calculator = Calculator()
    print("Addition:", calculator.perform_addition(10, 5))
    print("Subtraction:", calculator.perform_subtraction(10, 5))
    print("Multiplication:", calculator.perform_multiplication(10, 5))
    print("Division:", calculator.perform_division(10, 5))
