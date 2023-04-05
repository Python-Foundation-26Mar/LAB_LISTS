# q1
thisNumber = [2, 3, 4, 5, 15, 1, 43, 20]
print(thisNumber)
Sum = sum(thisNumber)
print(Sum)
# q2

def maxelement(thisNumber_2):
    print(max(thisNumber_2))
 
thisNumber_2 = [2, 3, 4, 5, 15, 1, 43, 20]

maxelement(thisNumber_2)

# q3 
def ODD_NUMBERS(num):
    ODD = [1200-2000]
    for i in range(num):
        if i % 2 == 1:
            ODD.append(i)
    return ODD

num = 1200

print("ODD Number: ",ODD_NUMBERS(num))


# q4
thisNumber_4 = [2, 3, 4, 5, 15, 1, 43, 20]
 
print("\nSliced Lists: ")
 

print(thisNumber_4[0:5])
 


