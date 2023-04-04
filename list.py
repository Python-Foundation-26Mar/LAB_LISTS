
### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.



sum_list=[2,3,4,5,15,1,43,20]
total = 0
for x in sum_list:
        total += x
print('Total sum is=',total)


### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.



print('The largest number is=',max(sum_list))


### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].



odd_list=[x   for x in range(1200,2000)if x%2 ==1]   
print(odd_list)


### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.


new_list=sum_list[0:5]
print(new_list)






