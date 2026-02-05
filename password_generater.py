import random
import string

def generate_password(length):
    # Combine lowercase, uppercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly pick characters from the pool
    password = ''.join(random.choice(characters) for i in range(length))
    return password

size = int(input("How many characters do you want in your password? "))
print("Your new password is:", generate_password(size))
