# LAB_LISTS


## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]

### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.

def getSum(list):
    return sum(list)

list = [2, 3, 4, 5, 15, 1, 43, 20]
print("The sum of the list is:" , getSum(list))

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

def getMax(list):
    return max(list)

list = [2, 3, 4, 5, 15, 1, 43, 20]
print("The maximum number in the list is:", getMax(list))

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].

my_list = []
for n in range(1200,2000,125):
    my_list.append(n)
print("The new list that starts with 1200 to 2000 with step of 125 is:", my_list, end=" ")
print()

### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
print("The first five elements using slice concept are:", my_list[0:5])
