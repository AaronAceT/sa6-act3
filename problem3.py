def find_maximum(numbers, compare):
    maximum = numbers[0]
    
    for num in numbers[1:]:
        maximum = compare(maximum, num)
    
    return maximum

numbers_list = [5, 3, 9, 2, 7]

greater = lambda x, y: x if x > y else y


print(find_maximum(numbers_list, greater))
