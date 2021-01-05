def partition(array, low, high):
    pi = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pi:
            i = i+1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quicksort(array, low, high):
    if low  < high:

        pi = partition(array, low, high)

        quicksort(array, low, pi-1)

        quicksort(array, pi+1,high)

def main():
    lent = int(input("Enter Length of the Array: "))
    import random
    import time
    array = []
    for i in range(0,lent):
        n = random.randint(1,1000)
        array.append(n)
    #array = np.random.randint(10, size = lent)
    #array = [7,9,4,6]
    n = len(array)
    start = time.time()
    #print("unsorted Array:", array)
    quicksort(array, 0, n-1)
    #print("Sorted Array:", array)
    print(f"Time taken to sort: {time.time() - start}")
main()
