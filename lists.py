# Q1:.......................

ripple_list=[2,3,4,5,15,1,43,20]
total = sum(ripple_list)
print(total)

#Q2:.........................

def fint_bigest_number(numbers):
    bigest_number=numbers[0]
    for any in numbers:
        if any > bigest_number:
            bigest_number=any
    return bigest_number
   
largest_number= fint_bigest_number(ripple_list)
print(largest_number)

#Q3:.........................

odd_list=[any for any in range(1200, 2000, 125)if any % 2 == 1 ]
print(odd_list)

#Q4:.........................
new_list = ripple_list[0:5]
print(new_list)

