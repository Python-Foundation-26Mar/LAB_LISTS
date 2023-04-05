# LAB_LISTS
#Q1
list_number = [2, 3, 4, 5, 15, 1, 43, 20] 

def the_sum(list_number):
    sum = 0
    for x in list_number:
        sum += x
    return sum
print("thw sum:",the_sum(list_number))


#Q2
def largest_num (the_list:list):
    max = the_list[0]
    for item in the_list:
        if item > max:
            max=item
    return max
print("the largest number:",largest_num(list_number))

#Q3
odd_list=[x for x in range(1200,2000,125) if x%2!=0] 
print ("the odd numbers =",odd_list)

#Q4
new_list=list_number[0:5]
print(new_list)




