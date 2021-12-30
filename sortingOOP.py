class Sort:
    def __init__(self, Array):
        self.array = Array

    @staticmethod
    def Swap(array,a, b):
        array[a], array[b] = array[b], array[a]

    def BubbleSort(self):
        for i in range(len(self.array) - 1):
            for j in range(len(self.array) - 1 - i):
                if self.array[j] > self.array[j+1]:
                    Sort.Swap(self.array,j, j+1)
        return self.array

    def InsertionSort(self):
        for i in range(1, len(self.array)):
            j = i-1
            x = self.array[i]
            while(j > -1 and self.array[j] > x):
                self.array[j+1] = self.array[j]
                j -= 1
            self.array[j+1] = x
        return self.array

    def SelectionSort(self):
        for i in range(len(self.array)):
            k = i
            for j in range(i,len(self.array)):
                if self.array[k] > self.array[j]:
                    k = j
            Sort.Swap(self.array,i,k)
        return self.array

    def QuickSortHelper(self, start, end):
        left  = start + 1
        pivot = self.array[start]
        for right in range(start + 1, end):
            if pivot > self.array[right]:
                Sort.Swap(self.array,left,right)
                left += 1
        Sort.Swap(self.array,start, left-1)
        return left-1
        
    def QuickSort(self, start, end):
        if len(self.array) == 1:
            return self.array
        if start < end:
            splitPoint = self.QuickSortHelper(start, end)
            self.QuickSort(start, splitPoint)
            self.QuickSort(splitPoint + 1, end)
        return self.array
    
    def MergeSortHelper(self, low, mid, high):
        Index1 = mid - low + 1
        Index2 = high - mid

        LeftList = [0 for k in range(Index1)]
        RightList = [0 for k in range(Index2)]

        for i in range(0, Index1):
            LeftList[i] = self.array[low + i]
        
        for i in range(0, Index2):
            RightList[i] = self.array[mid + i + 1]
        
        i, j, k = 0, 0, low
        while i < Index1 and j < Index2:
            if LeftList[i] < RightList[j]:
                self.array[k] = LeftList[i]
                i += 1
            else:
                self.array[k] = RightList[j]
                j += 1
            k += 1

        while i < Index1:
            self.array[k] = LeftList[i]
            i += 1
            k += 1
        
        while j < Index2:
            self.array[k] = RightList[j]
            j += 1
            k += 1
    
    def IterativeMergeSort(self):
        width = 1
        n = len(self.array)

        while width < n:
            low = 0
            while (low < n):
                high = min(low + (width * 2 -1), n - 1)
                mid = (low + high) // 2

                if width > n //2:
                    mid = high - (n % width)
                self.MergeSortHelper(low, mid, high)
                low += width * 2
            width *= 2
        return self.array

    def RecursiveMergeSort(self,low, high):
        if low < high:
            mid = (low + high) // 2
            self.RecursiveMergeSort(low, mid)
            self.RecursiveMergeSort(mid + 1, high)
            self.MergeSortHelper(low, mid, high)
        return self.array
    
    def MergeSort(self, flag = True, low = None, high = None):
        if flag == True:
            return self.IterativeMergeSort()
        return self.RecursiveMergeSort(low, high)

    def CountSort(self):
        temp = [0 for _ in range(max(self.array) + 1)]
        for i in range(len(self.array)):
            temp[self.array[i]] += 1
        
        k = 0
        for j in range(max(self.array) + 1):
            for _ in range(temp[j]):
                self.array[k] = j
                k += 1
        return self.array
    
    def BucketBinSort(self):
        MaxValue = max(self.array)
        length = len(self.array)
        size = MaxValue / length

        # Create Buckets
        Buckets = [[] for i in range(length)]

        # Bucket Sorting
        for i in range(length):
            index = int(self.array[i] / size)
            if index != length:
                Buckets[index].append(self.array[i])
            Buckets[length - 1].append(self.array[i])
        
        # Sorting Individual Buckets
        for i in range(len(self.array)):
            Buckets[i] = sorted(Buckets[i])
        
        # Flattening the array
        result = []
        for i in range(length):
            result = result + Buckets[i]
                   
        return result
    
    @staticmethod
    def flatten(array):
        from functools import reduce
        return reduce(lambda X, Y : X + Y, array)
    
    def RadixSort(self):
        import math
        RadixListLength = 10
        MaxValue = max(self.array)

        count = 0
        while(MaxValue > 0):
            count += 1
            MaxValue //= 10
        
        for i in range(count):
            Buckets = [[] for _ in range(RadixListLength)]
            for values in self.array:
                num = int((values / (math.pow(10,i))) % 10)
                Buckets[num].append(values)
            self.array = Sort.flatten(Buckets)
        
        return self.array
    
    def ShellSort(self):
        ListLength = len(self.array)
        gap = ListLength // 2

        while gap > 0:
            for i in range(gap, ListLength):
                temp = self.array[i]
                j = i
                while j >= gap and self.array[j - gap] > temp:
                    self.array[j] = self.array[j - gap]
                    j -= gap
                self.array[j] = temp
            gap //= 2



if __name__ == "__main__":
    Array = [34, 98, 54, 89, 100, 1000, 42, 1005, 1524, 1343]
    S = Sort(Array = Array)
    S.BubbleSort()
    S.ShellSort()