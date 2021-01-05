def heapsort(array, n ,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest  = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapsort(array, n ,largest)

def isSorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

def main():
    lent = int(input("Enter Length of the Array: "))
    import random
    import time
    array = []
    for i in range(0,lent):
        n = random.randint(1,10)
        array.append(n)
    #array = np.random.randint(10, size = lent)
    #array = [7,9,4,6]
    n = len(array)
    #start = time.time()
    print(f"Unsorted Array", array)
    #print()
    #Building Max heap
    for i in range (n//2, -1 , -1):
        heapsort(array, n ,i)

        # Sorting

    for i in range (n-1, 0 , -1):
        array[i], array[0] = array [0], array[i]
        heapsort(array, i , 0)

    print("Sorted Array:", array)
    isSorted(array)

    #Print(array,n)


    #print(f"Time taken to sort: {time.time() - start}")
main()
