# Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]


# Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
def list_of_numbers (random_num:list):
    result = 0
    
    for num in random_num:
        result += num
        return result
random_num = [2, 3, 4, 5, 15, 1, 43, 20]
print ("Total All Elements= ", sum (random_num))   


#Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def largest_number (largest: list):

     large = largest[0]
     for i in largest:
           if i > large:
               large = i
     return large
   
largest = [2, 3, 4, 5, 15, 1, 43, 20]
print("\n")
print("The Largest Number is: ", largest_number(largest))    
       
    
# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].
odd_numbers = [x for x in range (1200, 2000) if x%2 == 1]
print("\n")
print (odd_numbers)
    
    
# Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
the_list = [2, 3, 4, 5, 15, 1, 43, 20]
new_the_list = the_list [5:]
print ("\n")
print("The New List=",new_the_list)