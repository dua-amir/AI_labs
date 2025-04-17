num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Error: Factorial is not defined for negative numbers.")
else:
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    result = factorial
    print(f"The factorial of {num} is: {result}")

