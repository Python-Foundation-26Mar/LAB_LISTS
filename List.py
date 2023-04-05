#Rahaf Saleh
#Q1: Here is a  function that takes a list as a parameter and returns the sum of all the items in that list:

def sum_list(ll):
    return sum(ll)
my_list =  [2, 3, 4, 5, 15, 1, 43, 20]
print(sum_list(my_list))


#Q2: Here is a function that takes a list as a parameter and returns the largest number from a list of numbers:

def max_list(lst):
    return max(lst)
my_list = [2, 3, 4, 5, 15, 1, 43, 20]
print(max_list(my_list))


#Q3: Here is a  list comprehension that creates an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125:

odd_list=[num for num in range(1200, 2000, 125)if num % 2 == 1 ]
print(odd_list)
#Q4: Here is the code to use list slicing to get a new list from the previous list starting from the start to the 5th element in the list:

my_list = [2, 3, 4, 5, 15, 1, 43, 20]
new_list = my_list[:4]
print(new_list)


