def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter_even_numbers(numbers)
odd_numbers = filter_odd_numbers(numbers)

print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
