def BubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1] , array[j]
    return array

def InsertionSort(array):
    for i in range(1, len(array)):
        j = i -1
        x = array[i]
        while(j > -1 and array[j] > x):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = x
    return array


def SelectionSort(array):
    for i in range(len(array)):
        k = i
        for j in range(i, len(array)):
            if array[j] < array[k]:
                k = j
        array[i], array[k] = array[k], array[i]
    return array


def Partition(array, start, end):
    left = start + 1
    pivot = array[start]
    for right in range(start + 1, end):
        if pivot > array[right]:
            array[left], array[right] = array[right], array[left]
            left += 1
    array[start], array[left-1] = array[left-1], array[start]
    return left - 1

def QuickSort(array, start, end):
    if len(array) == 1:
        return array
    if start < end:
        split = Partition(array, start, end)
        QuickSort(array, start, split)
        QuickSort(array, split+1, end)
    return array

def MergeSpliter(array, low, mid, high):
    Index1 = mid - low + 1
    Index2 = high - mid

    LeftList = [0 for k in range(Index1)]
    RightList = [0 for k in range(Index2)]

    for i in range(0, Index1):
        LeftList[i] = array[low + i]
    
    for i in range(0, Index2):
        RightList[i] = array[mid + i + 1]

    i, j, k = 0,0,low
    while i < Index1 and j < Index2:
        if LeftList[i] > RightList[j]:
            array[k] = RightList[j]
            j += 1
        else:
            array[k] = LeftList[i]
            i += 1

        k += 1
    
    while i < Index1:
        array[k] = LeftList[i]
        i += 1
        k += 1
    
    while j < Index2:
        array[k] = RightList[j]
        j += 1
        k += 1

def MergeSortIterative(array):
    width = 1
    n = len(array)

    while width < n:
        low = 0
        while (low < n):
            high = min(low + (width * 2 -1), n - 1)
            mid = (low + high) // 2

            if width > n //2:
                mid = high - (n % width)
            MergeSpliter(array, low, mid, high)
            low += width * 2
        width *= 2
    return array


def MergeSortRecursive(Array, low, high): 

    if low < high :
        mid = (low + high) // 2
        MergeSortRecursive(Array, low, mid)
        MergeSortRecursive(Array, mid + 1, high)
        MergeSpliter(Array, low, mid, high)
    return Array

def CountSort(array):
    Max = max(array)
    temp = [0 for k in range(Max + 1)]
    for i in range(len(array)):
        temp[array[i]] += 1
    k = 0
    for a in range(Max + 1):
        for _ in range(temp[a]):
            array[k] = a
            k += 1
    return array


def BucketBinSort(array):
    largest = max(array)
    length = len(array)
    size = largest/length

    # Create Buckets
    buckets = [[] for i in range(length)]

    # Bucket Sorting
    for i in range(length):
        index = int(array[i] / size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[length - 1].append(array[i])
        
    # Sorting Individual Buckets
    for i in range(length):
        buckets[i] = InsertionSort(buckets[i])
    
    # Flattening the array
    result = []
    for i in range(length):
        result = result + buckets[i]

    return result  


def flatten(array):
    from functools import reduce
    return reduce(lambda X, Y : X + Y, array)

def RadixSort(array):
    import math
    Radix = 10
    MaxValue = max(array)

    count = 0
    while(MaxValue > 0):
        count += 1
        MaxValue //= 10
    
    for i in range(count):
        Buckets = [[] for _ in range(Radix)]
        for values in array:
            num = int((values / (math.pow(10,i))) % 10)
            Buckets[num].append(values)
        array = flatten(Buckets)
    
    return array

def ShellSort(array):
    ListLength = len(array)
    gap = ListLength // 2

    while gap > 0:
        for i in range(gap, ListLength):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2

        



if __name__ == "__main__":
    Array = [34, 98, 54, 89, 100, 1000, 42, 1005, 1524, 1343]
    BubbleSort(array = Array)
    ShellSort(array = Array)