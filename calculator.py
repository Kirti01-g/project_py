def calc(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

a = float(input("A: "))
b = float(input("B: "))
op = input("Operator (+ - * /): ")
print("Result:", calc(a, b, op))
