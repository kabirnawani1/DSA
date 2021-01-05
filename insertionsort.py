import numpy as np
import random
import time

def sort(array,n):
    for i in range(1,n):
        for j in range(i,0,-1):
            if array[j] < array[j-1] :
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp

#def Print(array,n):
    #for i in range (n):
        #print(array[i], end =' ')

def main():
    lent = int(input("Enter Length of the Array: "))
    array = np.random.randint(10, size = lent)
    n = len(array)
    #print(f"Unsorted Array: {array}")
    #print()
    #print("Sorted Array:")
    #Print(array,n)
    start = time.time()
    sort(array,n)
    print(f"Time taken to sort: {time.time() - start}")
main()
