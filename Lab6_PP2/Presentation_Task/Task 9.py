from functools import reduce
import operator

def multiply_numbers(numbers):
    if not numbers:
        return None
    return reduce(operator.mul, numbers)

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
result = multiply_numbers(numbers)
if result is not None:
    print("Result of multiplying all numbers:", result)
else:
    print("The list is empty.")
