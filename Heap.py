import sys

class Heap:
    """Heap Class"""
    def __init__(self, MaxSize):
        """Consturctor of Heap class"""
        self.MaxSize = MaxSize
        self.size = 0
        self.HeapMax = [0 for _ in range(self.MaxSize + 1)]
        self.HeapMin = [0 for _ in range(self.MaxSize + 1)]
        self.HeapMax[0] = sys.maxsize
        self.HeapMin[0] = -1 * sys.maxsize
        self.FRONT = 1

    def Root(self, pos):
        """PARENT NODE"""
        return pos // 2
    
    def Left(self, pos):
        """LEFT CHILD NODE"""
        return 2 * pos
    
    def Right(self, pos):
        """RIGHT CHILD NODE"""
        return (2 * pos) + 1
    
    def IsLeaf(self, pos):
        """METHOD RETURN TRUE IF PASSED NODE IS LEAF NODE"""
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False
    
    def SwapMax(self,a,b):
        """METHOD TO SWAP THE NODES OF THE HEAP"""
        self.HeapMax[a], self.HeapMax[b] = (self.HeapMax[b], self.HeapMax[a])
    
    def SwapMin(self,a,b):
        """METHOD TO SWAP THE NODES OF THE HEAP"""
        self.HeapMin[a], self.HeapMin[b] = self.HeapMin[b], self.HeapMin[a]
     
    def MaxHeapify(self, pos):
        """METHOD TO MAX HEAPIFY THE NODE AT POSTITON(pos)"""
        if not self.IsLeaf(pos):
            if (self.HeapMax[pos] < self.HeapMax[self.Left(pos)] or 
                self.HeapMax[pos] < self.HeapMax[self.Right(pos)]):

                if self.HeapMax[self.Left(pos)] > self.HeapMax[self.Right(pos)]:
                    self.SwapMin(pos, self.Left(pos))
                    self.MaxHeapify(self.Left(pos))
                else:
                    self.SwapMin(pos, self.Right(pos))
                    self.MaxHeapify(self.Right(pos))

    def MinHeapify(self,pos):
        """METHOD TO MIN HEAPIFY THE NODE AT POSTITON(pos)"""
        if not self.IsLeaf(pos):
            if (self.HeapMin[pos] > self.HeapMin[self.Left(pos)] or 
                self.HeapMin[pos] > self.HeapMin[self.Right(pos)]):

                if self.HeapMin[self.Left(pos)] < self.HeapMin[self.Right(pos)]:
                    self.SwapMin(pos, self.Left(pos))
                    self.MinHeapify(self.Left(pos))
                else:
                    self.SwapMin(pos, self.Right(pos))
                    self.MinHeapify(self.Right(pos))

    
    def InsertMaxHeap(self, Key):
        """METHOD TO INSERT IN A MAX HEAP"""
        if self.size >= self.MaxSize:
            return 
        self.size += 1
        self.HeapMax[self.size] = Key

        current = self.size
        while self.HeapMax[current] > self.HeapMax[self.Root(current)]:
            self.SwapMax(current, self.Root(current))
            current = self.Root(current)
    
    def InsertMinHeap(self, Key):                 
        """METHOD TO INSERT IN A MIN HEAP"""
        if self.size >= self.MaxSize:
            return 
        self.size += 1
        self.HeapMin[self.size] = Key

        current = self.size
        while self.HeapMin[current] < self.HeapMin[self.Root(current)]:
            self.SwapMin(current, self.Root(current))
            current = self.Root(current)

    def DisplayMax(self):
        """METHOD TO DISPLAY THE MAX HEAP"""
        for i in range(1, (self.size // 2) + 1):
            print(f"Root :- {self.HeapMax[i]}    Left Child :- {self.HeapMax[2 * i]}    Right Child :- {self.HeapMax[(2 * i) + 1]}")
    
    def DisplayMin(self):
        """METHOD TO DISPLAY THE MIN HEAP"""
        for i in range(1, (self.size // 2) + 1):
            print(f"Root :- {self.HeapMin[i]}    Left Child :- {self.HeapMin[2 * i]}    Right Child :- {self.HeapMin[(2 * i) + 1]}")

    
    def DeleteMax(self):
        """METHOD TO DELETE THE MAX VALUE FROM HEAP"""
        popped = self.HeapMax[self.FRONT]
        self.HeapMax[self.FRONT] = self.HeapMax[self.size]
        self.size -= 1
        self.MaxHeapify(self.FRONT)
        return print(f"Max Value is :- {popped}")

    def MinHeap(self):
        """METHOD TO BUILD MIN HEAP USING MIN HEAPIFY FUNCTION"""
        for pos in range(self.size // 2, 0, -1):
            self.MinHeapify(pos)
        
    def DeleteMin(self):
        """METHOD TO DELETE THE MIN VALUE FROM HEAP"""
        popped = self.HeapMin[self.FRONT]
        self.HeapMin[self.FRONT] = self.HeapMin[self.size]
        self.size -= 1
        self.MinHeapify(self.FRONT)
        return print(f"Min Value is :- {popped}")


if __name__ == "__main__":
    H = Heap(15)
    H.InsertMaxHeap(10)
    H.InsertMaxHeap(19)
    H.InsertMaxHeap(11)
    H.InsertMaxHeap(1)
    H.InsertMaxHeap(21)
    H.InsertMaxHeap(100)
    H.InsertMaxHeap(120)
    H.InsertMaxHeap(0)
    H.InsertMaxHeap(-3)
    H.InsertMaxHeap(40)
    H.InsertMaxHeap(30) 
    H.DisplayMax()
    H.DeleteMax()
    H.DisplayMax()
    H.DeleteMax()
    H.DisplayMax()


