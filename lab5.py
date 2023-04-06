'''
Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.


'''
# Q1
mylist1=[2, 3, 4, 5, 15, 1, 43, 20]

def result(list1):
    return print("SUM: ", sum(list1))

result(mylist1)  

# Q2
def largest(list1):
    return print("Largest element is:", max(list1))

largest(mylist1)

# Q3
number_list = [x for x in range(1200,2000,+125) if x % 2 != 0]
print(number_list)

# Q4
new_list = mylist1[0:5]
print(new_list)