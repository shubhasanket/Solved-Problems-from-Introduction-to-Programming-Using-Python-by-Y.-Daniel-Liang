'''17.3 (Min-heap) The heap presented in the text is also known as a max-heap,
in which each node is greater than or equal to any of its children. A min-heap
is a heap in which each node is less than or equal to any of its children.
Revise the heap sort program to use a min-heap. Write a test program that
prompts the user to enter a list of integers and uses the min-heap to sort the
integers.
'''
class Heap:
    def __init__(self):
        self.__lst = []

    def add(self,e):
        self.__lst.append(e)
        currentIndex = len(self.__lst)-1

        while currentIndex > 0:
            parentIndex = (currentIndex-1)//2

            if self.__lst[currentIndex] < self.__lst[parentIndex]:
                self.__lst[currentIndex], self.__lst[parentIndex] = \
                    self.__lst[parentIndex], self.__lst[currentIndex]

            else:
                break # The tree is a lst now

            currentIndex = parentIndex

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
                if self.__lst[maxIndex] > self.__lst[rightChildIndex]:
                    maxIndex = rightChildIndex

            if self.__lst[currentIndex] > self.__lst[maxIndex]:
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
    
def heapSort(lst):
    heap = Heap()

    for v in lst:
        heap.add(v)

    for i in range(len(lst)):
        lst[i] = heap.remove()

def main():
    lst = [-44,-5,-3,3,3,1,-4,0,1,2,4,5,53]
    heapSort(lst)
    for v in lst:
        print(str(v) + " ", end = " ")

if __name__ == "__main__":
    main()
        
                

