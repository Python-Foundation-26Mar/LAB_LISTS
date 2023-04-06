
def list_numbers (Rn:list):
    result = 0

    for num in Rn:
        result += num
        return result
Rn = [2, 3, 4, 5, 15, 1, 43, 20]
print ("Total is= ", sum (Rn))   


odd_numbers = [x for x in range (1200, 2000) if x%2 == 1]
print("\n")
print (odd_numbers)


List1 = [2, 3, 4, 5, 15, 1, 43, 20]
New_List = List1 [5:]
print ("\n")
print("New list is=",List1)


def Ln (largest: list):

     Lar = largest[0]
     for i in largest:
           if i > Lar:
               Lar = i
     return Lar

largest = [2, 3, 4, 5, 15, 1, 43, 20]
print("\n")
print(" largest Number is: ", Ln(largest)) 


