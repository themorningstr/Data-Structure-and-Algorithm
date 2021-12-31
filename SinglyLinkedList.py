class SingleLinkedList(object):
    """Class for linked list"""

    class Node(object):
        """Class for a Node"""
        def __init__(self,Data = None, NextAdd = None):
            """Constructor"""
            self.Data = Data
            self.NextAdd = NextAdd
        
        def getData(self):
            """Method to get the data of current node"""
            return self.Data
        
        def setData(self,data):
            """Method to set the data"""
            self.Data = data
        
        def getNextAdd(self):
            """Method to get the address of next node"""
            return self.NextAdd
        
        def setNextAdd(self, NewAddress):
            """Method to set the address of the current node"""
            self.NextAdd = NewAddress
        
        def hasNextAdd(self):
            """Method to check the address of the current node"""
            return self.NextAdd != None

    def __init__(self, head = None):
        """Constructor"""
        self.head = head
        self.length = 0

    def IterativeDisplay(self,Argument):
        """Iterative approach for displaying the linked list"""
        while Argument != None:
            print(Argument.getData(), end = " ")
            Argument = Argument.getNextAdd()
    
    def Display(self,flag = True):
        """Dispaly Function for linked list"""
        if flag is True:
            return self.IterativeDisplay(Argument = self.head)
        return self.RecursiveDisplay(Argument = self.head)
    
    def RecursiveDisplay(self,Argument):
        """Recursive function for displaying the linked list using Recursion"""
        if Argument is not None:
            print(Argument.getData(), end = " ")
            self.RecursiveDisplay(Argument.getNextAdd())
        
    def IterativeLength(self, Argument):
        """Iterative Approach for calculating length of linked list"""
        count = 0
        while Argument != None:
            count += 1
            Argument = Argument.getNextAdd()    
        return count

    def RecursiveLength(self,Argument):
        """Recursive Function for calculating the length of linked list"""
        if Argument is None:
            return 0
        else:
            return self.RecursiveLength(Argument.getNextAdd()) + 1
    
    def LinkedListLength(self,flag = True):
        """Method for calculating the length of linked list"""
        if flag is True:
            return self.IterativeLength(Argument = self.head)
        return self.RecursiveLength(Argument = self.head)

    def InsertAtBeginning(self,data):
        """Method for adding element at beginning"""
        NewNode = self.Node(Data = data)
        NewNode.setData(data)

        if self.length == 0:
            self.head = NewNode
        else:
            NewNode.setNextAdd(self.head)
            self.head = NewNode
            self.length += 1

    def InsertAtEnd(self,data):
        """Method for adding an element at the end of the linked list"""
        NewNode = self.Node(Data = data)
        NewNode.setData(data)

        current = self.head
        while current.getNextAdd() != None:
            current = current.getNextAdd()
        current.setNextAdd(NewNode)
        self.length += 1
    
    def InsertAtPosition(self,pos,data):
        """Method for adding an element at a given position of a linked list"""
        NewNode = self.Node(Data = data)
        NewNode.setData(data)

        if pos > self.length or pos < 0:
            raise IndexError('Out Of Range')
        elif pos == 0:
            self.InsertAtBeginning(data)
        elif pos == self.length:
            self.InsertAtEnd(data)
        else:
            count = 0
            current = self.head
            while count < pos - 1:
                count += 1
                current = current.getNextAdd()
            NewNode.setNextAdd(current.getNextAdd())
            current.setNextAdd(NewNode)
            self.length += 1

    def DeleteFromBeginning(self):
        """Deleting an element from the beginning"""
        if self.length == 0:
            f"Linked List is Empty"
        else:
            self.head = self.head.getNextAdd()
            self.length -= 1
   
    def DeleteFromLast(self):
        """Deleting an element at last"""
        if self.length == 0:
            f"Linked List is Empty"
        else:
            currentNode = self.head
            previousNode = self.head

            while currentNode.getNextAdd() != None:
                previousNode = currentNode
                currentNode = currentNode.getNextAdd()
            previousNode.setNextAdd(None)
            self.length -= 1
    
    def DeleteFromPosition(self,pos):
        """Deleting an element from a given position"""
        count = 0
        currentNode = self.head
        previousNode = self.head
        if pos > self.length or pos < 0:
            f"The Position doesn't exist. Please enter a valid position"
        else:
            while currentNode.getNextAdd() != None or count < pos:
                count += 1
                if count == pos:
                    #previousNode = currentNode.getNextAdd()
                    previousNode.setNextAdd(currentNode.getNextAdd())
                    self.length -= 1
                    return
                else:
                    previousNode = currentNode
                    currentNode = currentNode.getNextAdd()

    def IterativeSum(self,Argument):
        """Helper function to add all the element"""
        """Iterative Approach for sum"""
        Sum = 0
        if Argument == 0:
            return 0
        else:
            while Argument != None:
                Sum += Argument.getData()
                Argument = Argument.getNextAdd()
        return Sum
    def RecursiveSum(self,Argument):
        """Helper Function to add all the element of a linked list Recursively"""
        if Argument is None:
            return 0
        else:
            return self.RecursiveSum(Argument.getNextAdd()) + Argument.getData()


    def SumOfAllElement(self,flag = True):
        """Method to add all the element"""
        if flag is True:
            return self.IterativeSum(Argument = self.head)
        return self.RecursiveSum(Argument = self.head)

    def IterativeMax(self,Argument):
        """Iterative Approach to find the maximum value of the linked list"""
        Max = -32768                           #Min-Int Value of 16-bit
        while Argument != None:
            if Argument.getData() > Max:
                Max = Argument.getData()
            Argument = Argument.getNextAdd()
        return Max
            
    def RecursiveMax(self,Argument):
        """Recursive Approach for finding the maximum value of the linked list"""
        x = 0
        if Argument is None:
            return -32768
        else:
            x = self.RecursiveMax(Argument.getNextAdd())
            if x > Argument.getData():
                return x
            else:
                return Argument.getData()
    
    def MaxElement(self,flag = True):
        """Method to find the Maximum element in a linked list"""
        if flag is True:
            return self.IterativeMax(Argument = self.head)
        return self.RecursiveMax(Argument = self.head)

    def IterativeMin(self,Argument):
        """Iterative Approach for finding minimum value in a linked list"""
        Min = 2147483647                        # Max-Int for 16bit
        while Argument != None:
            if Argument.getData() < Min:
                Min = Argument.getData()
            Argument = Argument.getNextAdd()
        return Min
    
    def RecursiveMin(self,Argument):
        """Recursive Approach for findng the minimum value of linked list"""
        x = 0
        if Argument is None:
            return 2147483647
        else:
            x = self.RecursiveMin(Argument.getNextAdd())
            if x < Argument.getData():
                return x
            else:
                return Argument.getData()
    
    def MinElement(self, flag = True):
        """Method for finding the minimum value in a linked list"""
        if flag is True:
            return self.IterativeMin(Argument = self.head)
        return self.RecursiveMin(Argument = self.head)
    
    def IterativeSearch(self, Argument, key):
        """Iterative Approach for searching key in a linked list"""
        while Argument != None:
            if key == Argument.getData():
                return Argument
            Argument = Argument.getNextAdd()
        return None

    def RecursiveSearch(self,Argument, key):
        """Recursive Approach for finding key element in a linked list"""
        if Argument is None:
            return None
        elif key == Argument.getData():
            return Argument
        else:
            return self.RecursiveSearch(Argument.getNextAdd(), key)

    def Search(self,key, flag = True):
        """Method for searching a key element in a linked list"""
        if flag is True:
            return self.IterativeSearch(Argument = self.head, key = key)
        return self.RecursiveSearch(Argument = self.head, key = key)
    
    def InsertAtStoredPosition(self,key):
        """Method for inserting an element at sorted position in a sorted linked list"""
        currentNode = self.head
        previousNode = None
        while currentNode != None and currentNode.getData() < key:
            previousNode = currentNode
            currentNode = currentNode.getNextAdd()
        NewNode = self.Node(Data = key)
        NewNode.setData(key)
        NewNode.setNextAdd(previousNode.getNextAdd())
        previousNode.setNextAdd(NewNode)
        self.length += 1
    
    def CheckIsSorted(self):
        """Method for checking whether the linked list is sorted or not"""
        x = -32768
        currentNode = self.head
        while currentNode != None:
            if x > currentNode.getData():
                return f'Linked List is Not Sorted'
            x = currentNode.getData()
            currentNode = currentNode.getNextAdd()
        return f"Linked List is Sorted"
    
    def RemoveDuplicate(self):
        """Method for Removing the duplicate element in a sorted list"""
        currentNode = self.head
        nextNode = currentNode.getNextAdd()
        while nextNode is not None:
            if currentNode.getData() != nextNode.getData():
                currentNode = nextNode
                nextNode = nextNode.getNextAdd()
            else:
                currentNode.setNextAdd(nextNode.getNextAdd())
                del nextNode
                nextNode = currentNode.getNextAdd()
    
    def Reverse(self):
        """Method to Reverse the linked List"""
        Pnode = self.head
        Qnode = None
        Rnode = None
        while Pnode is not None:
            Rnode = Qnode
            Qnode = Pnode
            Pnode = Pnode.getNextAdd()
            Qnode.setNextAdd(Rnode)
        self.head = Qnode 