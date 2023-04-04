

ORGlist = [2, 3, 4, 5, 15, 1, 43, 20]

### Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.

def SumFun (my_list):
    Totalsum = 0
    for number in my_list:
        Totalsum = Totalsum + number

    return Totalsum

print(SumFun(ORGlist))


### Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.

def LargestFun (my_list):
    LargestNum = my_list[0]
    for number in my_list:
        if number > LargestNum:
            LargestNum = number

    return LargestNum

print(LargestFun(ORGlist))


### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ list comprehension ].

rng = range(1200, 2000, 125)
OddList = [num for num in rng if num % 2 != 0]

print(OddList)


### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

NewList = ORGlist[:5]

print(NewList)

