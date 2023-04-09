
def sum_of_numbers (number_list):
    result = 0
    for i in number_list:
        sum (number_list)
        result+=i
    return result

number_list=[2, 3, 4, 5, 15, 1, 43, 20]
print(sum_of_numbers(number_list))


def largest_number (number_list):
    i = max(number_list)
    return i
number_list=[2, 3, 4, 5, 15, 1, 43, 20]
max_num = largest_number(number_list)
print(max_num)

odd_numbers = [n for n in range(1200,2000,125) if n%2 != 0]
print(odd_numbers)

new_slicing_list = number_list[:5]
print(new_slicing_list)