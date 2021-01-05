import numpy as np
import random
import time

def merge_sort(array,n):
    merge_sort2(array , 0 , n - 1)

def merge_sort2(array,first ,last):
    if first < last :
        middle = (first + last) // 2
        merge_sort2(array, first, middle)
        merge_sort2(array, middle + 1, last)
        merge(array, first , middle, last)

def merge(array, first , middle, last):
    l = array[first:middle+1]
    r = array[middle+1:last+1]
    l.append(11)
    r.append(11)
    i = j = 0

    for k in range (first, last+1):
        if l[i] <= r[j]:
            array[k] = l[i]
            i += 1
        else:
            array[k] = r[j]
            j += 1

def Print(array,n):
    #print(array)
    for i in range (n):
        print(array[i], end =' ')

def main():
    times_n=[100,200,500,1000,5000,10000,1000000]
    #lent = int(input("Enter Length of the Array: "))

    for t in times_n:
        import random
        array = []
        for i in range(0,t):
            n = random.randint(1,10)
            array.append(n)
        #array = np.random.randint(10, size = lent)
        #array = [7,9,4,6]
        n = len(array)
        #print(f"Unsorted Array: {array}")
        #print()
        start = time.time()
        merge_sort(array,n)
        #print("Sorted Array:")
        #Print(array,n)
        print(t)
        print(f"Time taken to sort: {time.time() - start}")
main()


"""
7 9 4 6 9 1 4 2 3 5  7  2  4
0 1 2 3 4 5 6 7 8 9 10 11 12 """
