try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Multiplication:", x * y)
except ValueError:
    print("Invalid input")
