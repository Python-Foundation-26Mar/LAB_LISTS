#A
lists=[2,3,4,5,15,1,43,20]
def sum_function(S_list):
    return sum(S_list)

print("ths sum of the list is :",(sum_function(lists)))

#B
def largest_num(list):
    return max (list)
print("ths largest num of the list is :",(largest_num(lists)))

#C 
odd_list=[j for j in range(1200,2001,125) if j%2 != 0]
print("the odds numbers are :",odd_list)

#D 
new_lists= lists[:5]
print(new_lists)

