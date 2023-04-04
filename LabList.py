numbers =  [2, 3, 4, 5, 15, 1, 43, 20]
print("the list is ",numbers)

 # sum of all  number in list 

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print("the sum of all number is ",sum(numbers))


# largest number from a list of numbers.
print("the max number is ",max(numbers))


newlist=[]
for newlist in range(1200,2000,125):
 if newlist%2 !=0:
  print( "the number is odd in list =  ",[newlist])


new_list = numbers[0:5]
print(numbers[0:5])