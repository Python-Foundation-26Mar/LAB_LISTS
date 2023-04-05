def get_list_sum(input_list):
    return sum(input_list)


my_list = [2, 3, 4, 5, 15, 1, 43, 20]
list_sum = get_list_sum(my_list)
print("Sum of list elements:", list_sum)

#2
def get_largest_number(input_list):
    return max(input_list)


my_list = [2, 3, 4, 5, 15, 1, 43, 20]
largest_number = get_largest_number(my_list)
print("Largest number in the list:", largest_number)

#Q 3
odd_numbers = [num for num in range(1200, 2001, 125) if num % 2 != 0]

#Q4
print("Odd numbers list:", odd_numbers)

my_list = [2, 3, 4, 5, 15, 1, 43, 20]
new_list = my_list[:5]


print("New list using list slicing:", new_list)
