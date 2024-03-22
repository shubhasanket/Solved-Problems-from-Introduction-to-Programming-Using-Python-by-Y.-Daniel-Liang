"""18.2 (Implement LinkedList) The implementations of methods clear(),
contains(Object o), and get(int index), indexOf(Object o) are omitted in
the text. Implement these methods.
"""

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # Return the head element in the list 
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element
    
    # Return the last element in the list 
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    # Add an element to the beginning of the list 
    def addFirst(self, e):
        newNode = Node(e) # Create a new node
        newNode.next = self.__head # link the new node with the head
        self.__head = newNode # head points to the new node
        self.__size += 1 # Increase list size

        if self.__tail == None: # the new node is the only node in list
            self.__tail = self.__head

    # Add an element to the end of the list 
    def addLast(self, e):
        newNode = Node(e) # Create a new node for e
    
        if self.__tail == None:
            self.__head = self.__tail = newNode # The only node in list
        else:
            self.__tail.next = newNode # Link the new with the last node
            self.__tail = self.__tail.next # tail now points to the last node
    
        self.__size += 1 # Increase size

    # Same as addLast 
    def add(self, e):
        self.addLast(e)

    # Adds the elements in otherList to this list.
    # Returns true if this list changed as a result of the call
    def addAll(self, otherList):
        for i in otherList:
            self.add(i)
        try:
            ret = len(otherList)
        except:
            ret = otherList.getSize()
        return bool(ret)

    # Removes all the elements in otherList from this list
    # Returns true if this list changed as a result of the call
    def removeAll(self, otherList):
##        print(set(otherList))
        temp = set(otherList) & set(self.returnElements())
##        print("...",temp)
        current = self.__head
        index = 0
        while current != None:
            if current.element in temp:
                self.removeAt(index)
            else:
                index += 1
            current = current.next   
        
        return bool(temp)

    # Retains the elements in this list that are also in otherList
    # Returns true if this list changed as a result of the call
    def retainAll(self, otherList):
        temp = set(self.returnElements()) - set(otherList)
        return self.removeAll(temp)

    
    def returnElements(self):
        lst = []
        current = self.__head
        while current != None:
            lst.append(current.element)
            current = current.next
        return lst

    # Insert a new element at the specified index in this list
    # The index of the head element is 0 
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e) # Insert first
        elif index >= self.__size:
            self.addLast(e) # Insert last
        else: # Insert in the middle
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node. 
    def removeFirst(self):
        if self.__size == 0:
            return None # Nothing to delete
        else:
            temp = self.__head # Keep the first node temporarily
            self.__head = self.__head.next # Move head to point the next node
            self.__size -= 1 # Reduce size by 1
            if self.__head == None: 
                self.__tail = None # List becomes empty 
            return temp.element # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self.__size == 0:
            return None # Nothing to remove
        elif self.__size == 1: # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None  # list becomes empty
            self.__size = 0
            return temp.element
        else:
            current = self.__head
        
            for i in range(self.__size - 2):
                current = current.next
        
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list. 
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None # Out of range
        elif index == 0:
            return self.removeFirst() # Remove first 
        elif index == self.__size - 1:
            return self.removeLast() # Remove last
        else:
            previous = self.__head
    
            for i in range(1, index):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0
    
    # Return the size of the list
    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["

        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string
        if result == "[":
            result += "]"
        return result

    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None
        self.__size = 0

    # Return true if this list contains the element o 
    def contains(self, e):
        cont = False
        current = self.__head
        while current != None and not cont:
            if current.element == e:
                cont = True
            current = current.next
        return cont

    # Remove the element and return true if the element is in the list 
    def remove(self, e):
        index = self.indexOf(e)
        ret = True if index != -1 else False
        if ret:
            self.removeAt(index)
        
        return ret

    # Return the element from this list at the specified index 
    def get(self, index):
        if index >= self.__size:
            print("Index beyond the range of the list")
            ret = None
        else:
            current = self.__head
            for i in range (index):
                current = current.next
            ret = current.element
   
        return ret

    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def indexOf(self, e):
        current = self.__head
        index = 0
        ret = -1
        while current != None:
            if current.element == e:
                ret = index
                break
            else:
                current = current.next
                index += 1
            
        return ret

    # Return the index of the last matching element in this list
    #  Return -1 if no match. 
    def lastIndexOf(self, e):
        print("Implementation left as an exercise")
        return 0

    # Replace the element at the specified position in this list
    #  with the specified element. */
    def set(self, index, e):
        print("Implementation left as an exercise")
        return None
    
    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.__head)
    
# The Node class
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class LinkedListIterator: 
    def __init__(self, head):
        self.current = head
        
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element    

def main():
    l1 = ["Tom", "George", "Jean", "Jane"]
    l2 = ["Tom", "George", "Micheal", "Michelle", "Daniel"]

    list1 = LinkedList()
    for u in l1:
        list1.add(u)
        
    list2 = LinkedList()
    for u in l2:
        list2.add(u)

##    print(type(list2))
##    print(list1,list2)
##
##    list1.addAll(list2)
##    print(list1)
##
##    list1.removeAll(list2)
##    print(list1)
##
##    list1.retainAll(list2)
##    print(list1)

    print(list1.contains("Jean"))
    print(list1)
    print(list1.getSize())
    print(list1.get(0))
    print(list1.get(list1.getSize()-2))

    print(list1.indexOf("George"))
if __name__ == "__main__":
    main()
##    print(1)
##main()
##print(__name__)
