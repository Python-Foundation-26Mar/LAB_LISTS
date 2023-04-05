numbers =  [2, 3, 4, 5, 15, 1, 43, 20]

#sum of all numbers

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print("the sum is ",sum(numbers))
#The largest number
def largest_num(numbers:list):
    largest_number = 0

    for y in numbers:
        if y > largest_number:
            largest_number = y
    
    return largest_number

print("largest number: ",  largest_num(numbers))

#Create an odd numbers list from the elements of a range from 1200 to 2000 

odd_numbers_list = [number for number in range(1200, 2000, 125) if number%2 != 0]

print(odd_numbers_list)

#use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
new_list = numbers[:5]
print(new_list)

