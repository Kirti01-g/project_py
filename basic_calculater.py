def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    return x / y if y != 0 else "Error! Division by zero."

print("Select Operation: 1.Add, 2.Subtract, 3.Multiply, 4.Divide")
choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
# ... and so on for multiply and divide
