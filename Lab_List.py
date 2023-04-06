numbers_list = [2, 3, 4, 5, 15, 1, 43, 20]


def sum_numbers(numbers:list):
    total = 0
    for number in numbers:
        total += number

    return total


print(sum_numbers(numbers_list))


def find_largest(numbers:list):
    largest_number = 0

    for number in numbers:
        if number > largest_number:
            largest_number = number
    
    return largest_number


print("largest number: ", find_largest([9,50,3]))
print("largest number: ", find_largest(numbers_list))



        
odd_numbers_list = [number for number in range(1200, 2000, 125) if number%2 != 0]

print(odd_numbers_list)




new_list = numbers_list[:5]
print(new_list)