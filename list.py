## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.

list_1 = [2, 3, 4, 5, 15, 1, 43, 20]

def items (lis_1 : list):
    total=0
    for x in lis_1:
        total+=x
    return total 
print ("the sum of the list =",items(list_1))

### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

def max_num (lis_1 : list):
    max= lis_1[0] 
    for x in lis_1:
        if x> max:
            max=x
    return max 
print ("the largest number =",max_num(list_1))

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].

odd_list=[x for x in range(1200,2000,125) if x%2!=0] 
print ("the odd numbers =",odd_list)
### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
new_list=list_1[0:5]
print(new_list)