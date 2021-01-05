import numpy as np
import random
import time

def sort(array, n):
    for i in range(n):
        index = i
        for j in range (i+1, n):
            if array[j] < array[index]:
                index = j
        swap(array,index,i)

def swap(array,index,i):
    #temp = array[i]
    #array[i] = array[index]
    #array[index] = temp
    array[i],array[index] = array[index],array[i]

def Print(array,n):
    for i in range (n):
        print(array[i], end =' ')

def main():
    lent = int(input("Enter Length of the Array: "))
    array = np.random.randint(10, size = lent)
    n = len(array)
    print(f"Unsorted Array: {array}")
    print()
    #start = time.time()
    sort(array,n)
    #print(f"Time taken to sort: {time.time() - start}")
    print("Sorted Array:")
    Print(array,n)
main()
