# Created by Tom R.
# Displays examples of Mod 

# Define two numbers
num1 = 10
num2 = 3

# Example 1: Modulo of two numbers
result1 = num1 % num2
print(f"{num1} divided by {num2} gives a quotient of {num1 // num2} with a remainder of {result1}")

# Define two more numbers
num3 = 15
num4 = 7

# Example 2: Modulo with a larger dividend
result2 = num3 % num4
print(f"{num3} divided by {num4} gives a quotient of {num3 // num4} with a remainder of {result2}")

# Example 3: Modulo with negative numbers
num5 = -10
result3 = num5 % num2
print(f"{num5} divided by {num2} gives a quotient of {num5 // num2} with a remainder of {result3}")

# Example 4: Modulo with a divisor larger than the dividend
result4 = num2 % num1
print(f"{num2} divided by {num1} gives a quotient of {num2 // num1} with a remainder of {result4}")

# Example 5: Modulo with zero (handled by exception)
try:
    num6 = 20
    result5 = num6 % 0
    print(f"{num6} divided by 0 gives a quotient of {num6 // 0} with a remainder of {result5}")
except ZeroDivisionError:
    print("Cannot perform modulo by zero.")
