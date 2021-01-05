import time
import random
def shellSort(input_list,n):
    gap = 1
    y = int(n / 3)
    while gap < y:
        gap = int((3 * gap) + 1)
    #gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
# Sort the sub list for this gap

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp

# Reduce the gap for the next element

        gap = int(gap/3)

#list = [10,4,7,3,7,3,6,8,0,7,5,3,1,4,5,7]
lent = int(input("Enter Length of the Array: "))
import random
array = []
for i in range(0,lent):
    n = random.randint(1,10)
    array.append(n)
n=len(array)
start = time.time()
#print("original",list)
shellSort(array,n)
#print("sorted",list)
print(f"Time taken to sort: {time.time() - start}")
