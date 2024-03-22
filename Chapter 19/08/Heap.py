'''Implementing a Heap
'''
class Heap:
    def __init__(self):
        self.__lst = []

    # Add a new item into the lst
    def add(self, e):
        self.__lst.append(e) # Append to the lst
        # The index of the last node
        currentIndex = len(self.__lst)-1

        while currentIndex > 0:
            parentIndex = (currentIndex - 1)//2
            # Swap if the current item is greater that its parent
            if self.__lst[currentIndex] > self.__lst[parentIndex]:
                self.__lst[currentIndex], self.__lst[parentIndex] = \
                    self.__lst[parentIndex], self.__lst[currentIndex]
            else:
                break # The tree is a lst now

            currentIndex = parentIndex

    # Remove the root from the lst
    def remove(self):
        if len(self.__lst) == 0:
            return None

        removedItem = self.__lst[0]
        self.__lst[0] = self.__lst[len(self.__lst)-1]
        self.__lst.pop(len(self.__lst)-1)

        currentIndex = 0
        while currentIndex < len(self.__lst):
            leftChildIndex = 2 * currentIndex + 1
            rightChildIndex = 2 * currentIndex + 2

            if leftChildIndex >= len(self.__lst):
                break
            maxIndex = leftChildIndex
            if rightChildIndex < len(self.__lst):
                if self.__lst[maxIndex] < self.__lst[rightChildIndex]:
                    maxIndex = rightChildIndex

            if self.__lst[currentIndex] < self.__lst[maxIndex]:
                self.__lst[maxIndex], self.__lst[currentIndex] = \
                    self.__lst[currentIndex],self.__lst[maxIndex]
                currentIndex = maxIndex
            else:
                break

        return removedItem

    def getSize(self):
        return len(self.__lst)

    def isEmpty(self):
        return self.getSize() == 0

    def peek(self):
        return self.__lst[0]

    def getLst(self):
        return self.__lst
    
##def heapSort(lst):
##    heap = Heap()
##
##    for v in lst:
##        heap.add(v)
##
##    for i in range(len(lst)):
##        lst[i] = heap.remove()
##
##def main():
##    lst = [-44,-5,-3,3,3,53,1,-4,0,1,2,4,5]
##    heapSort(lst)
##    for v in lst:
##        print(str(v) + " ", end = " ")
##
##if __name__ == "__main__":
##    main()
##
##



    
