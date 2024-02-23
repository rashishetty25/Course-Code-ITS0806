import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Check if the number is even or odd
if random_number % 2 == 0:
    print(f"{random_number} is an even number.")
else:
    print(f"{random_number} is an odd number.")
