#MyLinkedList.py contains the LinkedList class with all the functions
#described in problems 18.1-3. 
#And also the Node and LinkedListIterator classes.

#You can use this for subsequent problems in other chapters

##    def __iter__(self):
##        return self.linkedListGenerator()
##
##    def linkedListGenerator(self):
##        current = self.__head
##        while current != None:
##            element = current.element
##            current = current.next
##            yield element

## NOTE: Adding  __len__ and __getitem__ methods allows us to use the
## len() and reversed() functions on a LinkedList. reversed() will now
## return a reversed object and you can use a for loop to traverse it
## in reverse.

class LinkedList:

    #### All the routines below are from author's source code Listing 18.2
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


    #18.2.2.1
    # Add an element to the beginning of the list
    def addFirst(self, e):
        newNode = Node(e) # Create a new node
        newNode.next = self.__head # link the new node with the head
        self.__head = newNode # head points to the new node
        self.__size += 1 # Increase list size

        if self.__tail == None: # the new node is the only node in list
            self.__tail = self.__head


    #18.2.2.2
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


    #18.2.2.3
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


    #18.2.2.4
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


    #18.2.2.5
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

    #18.2.2.6
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
        # Added the following if - otherwise an empty list does
        # not print properly. BUG in author's code
        if self.__head == None:
            return ("[]")
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string

        return result

    # Clear the list - Although the author asks to write this routine
    #in problem 2 - he has give it in Listing 18.2
    def clear(self):
        self.__head = self.__tail = None
        self.__size = 0   #BUG - not in source code


##    # Return an iterator for a linked list
##    def __iter__(self):
##        return LinkedListIterator(self.__head)

##    # Generator see section 18.4 of the chapter
##    
##    # Return an iterator for a linked list
##    # Alternate way to go throught the list without using
##    # the class LinkedListIterator
    def __iter__(self):
        return self.linkedListGenerator()

    def linkedListGenerator(self):
        current = self.__head
        while current != None:
            element = current.element
            current = current.next
            yield element




    #### All the above routines are from author's source code

    #### Problem 18.1 ########
    # Problem 18.1 asks us to implement set operations in LinkedList.
    # Implement the following set methods addAll, removeAll, retainAll
    # As he is asking for set operations we wrote the contains function
    # and used it to prevent adding duplicates in addAll etc.
    # The author has asked us to write the contain function in the
    # next problem 18.2
    
    # Adds the elements in otherList to this list.
    # Returns true if this list changed as a result of the call
    # UNION
    def addAll(self, otherList):
           
        if otherList.getSize() == 0:
            return False
        modified = False
        for i in otherList:
            if not self.contains(i):
                #Add only if the item in otherList is not already there
                self.add(i)
                modified = True
        return modified
    
    # Removes all the elements in otherList from this list
    # Returns true if this list changed as a result of the call
    # DIFFERENCE
    def removeAll(self, otherList):
        #If either list is empty come out with False
        if otherList.getSize() == 0:
            return False

        if self.getSize() == 0:
            return False
        j = 0
        modified = False
        #Removing elements from the beginning affects the head
        #we deal with that case separately
        #Remove elements from the start of the list
        while otherList.contains(self.getFirst()):
            self.__head = self.__head.next
            self.__size -= 1
            modified = True
        if self.__head == None:
            self.__tail = None
            return modified
        
        #There is at least one item and the first item is not in the otherlist
        p = self.__head
        q = p.next

        while q != None:
            if otherList.contains(q.element):
                if self.__tail == q:
                    self.__tail = p
                p.next = q.next
                q = q.next
                self.__size -= 1
                modified = True
            else:
                p = p.next
                q = q.next
       
        return modified
    
    # Retains the elements in this list that are also in otherList
    # Returns true if this list changed as a result of the call
    # INTERSECTION
    def retainAll(self, otherList):
        # If this list empty - then there is no change
        # as the intersection is empty
        if self.getSize() == 0:
            return False

        
        # If the other list is empty, the intersection is empty
        # so make this list empty  
        if otherList.getSize() == 0:
            if self.getSize() > 0:
                self.clear()
                return True
            # This list was already empty so nothing changed
            return False

        # There is at least one element each in this list and the other list
        j = 0
        modified = False
        #Removing elements from the beginning affects the head
        #we deal with that case separately
        #Remove elements from the start of the list that are not in otherList

        a = self.getFirst()
        while a and not otherList.contains(a):
            self.__head = self.__head.next
            self.__size -= 1
            modified = True
            a = self.getFirst()
            
        if self.__head == None:
            self.__tail = None
            return modified
        
        #There is at least one item and the first item is  in the otherlist
        p = self.__head
        q = p.next

        while q != None:
            if not otherList.contains(q.element):
                if self.__tail == q:
                    self.__tail = p
                p.next = q.next
                q = q.next
                self.__size -= 1
                modified = True
            else:
                p = p.next
                q = q.next
       
        return modified

    # The above routines were written for problem 18.1

    # Although the author asks us to write the contains routine in problem 18.2
    # we need it for problem 18.1 as he wants us to write set routines which
    # do not have duplicates
    
    # Return true if this list contains the element o 
    def contains(self, e):
        found = False
        j = self.__head
        while j != None:
            if j.element == e:
                return True
            j = j.next
            
        #print("Implementation left as an exercise")
        return False


    #### Problem 18.2 ########

    # Return the element from this list at the specified index 
    def get(self, index):
        if self.getSize()==0:
            return None
        if index < 0 or index >= self.getSize():
            return None
        k = 0
        p = self.__head
        while p != None:
            if k == index:
                return p.element
            else:
                p = p.next
                k = k + 1
        return None        
        #print("Implementation left as an exercise")

    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def indexOf(self, e):
        k = 0
        p = self.__head
        while p != None:
            if p.element == e:
                return k
            else:
                p = p.next
                k = k + 1
        return -1   
        


    #### Problem 18.3 ########


    # Remove the element and return True if the element is in the list
    # False otherwise
    def remove(self, e):
        if self.__size == 0:
            return False
        #Check if the first element equals e
        p = self.__head

        if p.element == e:
            print(p.element, e)
            if p == self.__tail:
                self.__tail = None
            self.__head = p.next
            self.__size -=1
            return True
            
        found = False
        q = p.next
        while q != None:
            if q.element == e:
                p.next  = q.next
                self.__size -=1
                if q == self.__tail:
                    self.__tail = p
                return True    
            else:
                p = q
                q = q.next
                
        #print("Implementation left as an exercise")
        return False

        

       
    # Return the index of the last matching element in this list
    # Return -1 if no match. 
    def lastIndexOf(self, e):
        c = d = -1
        j = self.__head
        
        while j != None:
            c += 1
            if j.element == e:
                d = c
            j = j.next

       
        return d

    # Replace the element at the specified position in this list
    #  with the specified element. */
    def set(self, index, e):
        if index < 0 or index >self.__size-1 or self.__size == 0:
            return None
        p = self.__head
        for i in range(index):
            p = p.next
        p.element = e
        return index
        
    # Not given by author nor as a problem    
    # Return elements via index operator
    # s1.__getitem__(0) is the same as s1[0]
##    def __getitem__(self, index):
##        return self.get(index)
    
    # Not given by author nor as a problem 
    # Return the length of the list (same as getSize)
    # To allow the len function of this list
    def __len__(self):
        return self.__size

    #Python writes __reverse__ magic method automatically if
    #__len__() and __getitem__ functions are there
    def myReverse(self):
        for x in range(self.__len__() - 1, -1, -1):
            yield self.__getitem__(x)
        
#The Node Class and LinkedListIterator also from author's Listing 18.2
    
# Node class
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        
# LinkedListIterator class
##class LinkedListIterator: 
##    def __init__(self, head):
##        self.current = head
##        
##    def __next__(self):
##        if self.current == None:
##            raise StopIteration
##        else:
##            element = self.current.element
##            self.current = self.current.next
##            return element    


if __name__ == "__main__":

    first = ["Tom", "George", "Peter", "Jean", "Jane"]
##    for i in first:
##        print(i,id(i))
    print(first)
    list1 = LinkedList()
    n = len(list1)
    a = iter(list1)
    print(a)
    for i in a:
        print(i)
##    print(type(a))
##    print(iter(list1).next())
    
##    
##    for i in first:
##        list1.add(i)
##
##    for j in list1:
##        print(j)
##        for k in list1:
##            print("\t",k,id(j),id(k))


    
##    while True:
##        try:
##            a = next(i)
##            print(a)
####            j = iter(list2)
####            while True:
####                try:
####                    b = next(j)
####                    print("\t",b)
####                except StopIteration as ex: #Reached end of loop using j
####                    print("Exception:",ex)
####                    break
##        except StopIteration as ex:
##            print(a,"????", ex)
##            #print(next(i))
##            break
##
##        print("End of loop")         
##                
        

##    #
##    a = iter(list1)
##    b = iter(list1)
##    print(id(a),id(b))
##
##    print("Displaying how to iterators are independent")
##    print("Printing using iterator a the first two items")
##    print(next(a))
##    print(next(a))
##    print("Printing using iterator b the first two items")
##    print(next(b))
##    print(next(b))
##    print("Printing using iterator a the third items")
##    print(next(a))    
##    print(next(a))    
##    print(next(a))
##    try:
##        print(next(a))
##    except:
##        print("*****")
##    print(next(b))    

    ''' 
    n = list1.getSize()
    print("SIZE:", n, len(list1))


    print("Original:",list1)

    print("REVERSE")
    #Python writes __reverse__ magic method automatically if
    #__len__() and __getitem__ functions are there

    #If you comment __getitem__ and try reversed you will get an error
    #TypeError: 'LinkedList' object is not reversible
    z = reversed(list1)
    x = reversed(list1)

    for i in z:
        print(i)
        for j in x:
            print("\t",j)
        x = reversed(list1)    
##    print("OUR REVERSE")
##    w = list1.myReverse()
##    v = list1.myReverse()
##    for i in w:
##        print(i)
##        for j in v:
##            print("\t",j)
##        v = reversed(list1)    

    #get
    print("GET")    
    for i in range(n):
        k = list1.get(i)
        print(i, k, end = " ")

    print()

    s = "Jean"
    a = list1.lastIndexOf(s)

    if a > -1:
        print("Found last occurence of "+s+" at",a)
    else:
        print(s+" not found")
    '''
