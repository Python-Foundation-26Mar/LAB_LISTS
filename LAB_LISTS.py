
## Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
my_list = [2, 3, 4, 5, 15, 1, 43, 20]

### Q1: Write a function that takes a list as a parameter,
#and then returns  the sum  of all the items in that list.
def items_summation(the_list:list):
    total=0
    for item in the_list:
        total+=item
    return total
print(items_summation(my_list))


### Q2: Write a function that takes a list as a parameter,
#and then returns the largest number from a list of numbers.
def largest_num (the_list:list):
    max=the_list[0]
    for item in the_list:
        if item > max:
            max=item
    return max
print(largest_num(my_list))


### Q3: Create an odd numbers list from the elements of a range
#from 1200 to 2000 with steps of 125, using [ list comprehension ].
### Q4: use list slicing to get a new list from the previous list
#starting from the start to the 5th element in the list.
main_list=[]
odd_list=[]
for i in range(0, 800):
    main_list.append(i+1200)
for item in main_list:
    if item %2==1 and len(odd_list)<5:
        odd_list.append(item)      
print(odd_list)
