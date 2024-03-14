import time
import math

number = int(input("Enter the number: "))
milliseconds = int(input("Enter the delay in milliseconds: "))

time.sleep(milliseconds / 1000)
result = math.sqrt(number)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
