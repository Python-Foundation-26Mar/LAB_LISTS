
#1
sum_list=[2,3,4,5,15,1,43,20]
total = 0
for x in sum_list:
        total += x
print('Total sum is=',total)
#2
print('The largest number is=',max(sum_list))
#3
odd_list=[x   for x in range(1200,2000)if x%2 ==1]   
print(odd_list)
#4
new_list=sum_list[0:5]
print(new_list)


