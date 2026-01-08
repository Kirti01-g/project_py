import random

num = random.randint(1, 100)
while True:
    g = int(input("Guess: "))
    if g == num:
        print("Correct")
        break
    print("Low" if g < num else "High")
