def raise_to_power(numbers, n):
    powered_numbers = list(map(lambda x: x ** n, numbers))
    return powered_numbers

numbers_list = [1, 2, 3, 4, 5]
constant_n = 3

print("Given numbers raised to the power of", constant_n, ":", raise_to_power(numbers_list, constant_n))