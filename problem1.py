
sum_of_digits = lambda n: sum(int(digit) for digit in str(n))
number = int(input("Enter a number: "))

result = sum_of_digits(number)


print(result)
