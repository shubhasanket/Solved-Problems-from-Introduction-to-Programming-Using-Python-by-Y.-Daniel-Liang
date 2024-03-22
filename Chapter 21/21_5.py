'''21.5 (Implement Set) Implement the union, difference,
and intersect methods in the Set class.
'''
# Define the default hash-table size
DEFAULT_INITIAL_CAPACITY = 4
  
# Define default load factor
DEFAULT_MAX_LOAD_FACTOR = 0.75 
     
# Define the maximum hash-table size to be 2 ** 30
MAXIMUM_CAPACITY = 2 ** 30 
  
class Set:
    def __init__(self, capacity = DEFAULT_INITIAL_CAPACITY, 
                 loadFactorThreshold = DEFAULT_MAX_LOAD_FACTOR):
        # Current hash-table capacity. Capacity is a power of 2
        self.capacity = capacity

        # Specify a load factor used in the hash table
        self.loadFactorThreshold = loadFactorThreshold
   
        # Create a list of empty buckets
        self.table = []
        for i in range(self.capacity):
            self.table.append([])
        
        self.size = 0 # Initialize set size

    # Add an entry (key, value) into the map 
    def add(self, key):
        if self.size >= self.capacity * self.loadFactorThreshold:          
            if self.capacity == MAXIMUM_CAPACITY:
                raise RuntimeError("Exceeding maximum capacity")
      
            self.rehash()
    
        bucketIndex = hash(key) % self.capacity
##        print("key:", key)
##        print(bucketIndex)
        # Add an entry (key, value) to hashTable[index]
        if not (key in self.table[bucketIndex]):
            self.table[bucketIndex].append(key)
            self.size += 1 # Increase size

    # Add all elements in a list to the set
    def add_list(self, l):
        for u in l:
            self.add(u)
            
    # Remove the entry for the specified key 
    def remove(self, key):
        bucketIndex = hash(key) % self.capacity
    
        # Remove the first entry that matches the key from a bucket
        if len(self.table[bucketIndex]) > 0:
            bucket = self.table[bucketIndex]
            for e in bucket:
                if e == key:
                    bucket.remove(e)
                    self.size -= 1 # Decrease size
                    break # Remove just one entry that matches the key

    # Return a set i.e the union of self and S
    def union(self, S):
        s = Set()
##        print("))))))))))))))))))))", s.table)
##        print(id(s))
##        print(id(self))
##        print(self.table)
        s.table = [[]+x for x in self.table]
        # need to execute the line above to make
        # a deep copy of s.table

        s.capacity = self.capacity
        s.size = self.size
##        print(s.table)
        s1 = S.table
        for bucket in s1:
            for u in bucket:
                s.add(u)
##                print(self.table)
##                print(u)
##                print(s.table)
##        print(s.table)
##        print("!!!!!!!!!!",self.table)
        return s

    # Return a set i.e the difference of self and S
    def difference(self, S):
        # Difference: self.table - S.table
        # Appending all the elements that belong to self.table
        # but not to S.table
        s = Set()
##        print(S.table)
##        print(self.table)
        for bucket in self.table:
            for u in bucket:
##                print(u)
                if not S.contains(u):
                    s.add(u)
        return s

    # Return a set i.e the intersection of self and S
    def intersect(self, S):
        if self.size < S.size:
            a = self.table
            b = S
        else:
            a = S.table
            b = self

        s = Set()
        for bucket in a:
            for u in bucket:
                if b.contains(u):
                    s.add(u)

        return s               
        
    # Return true if the specified key is in the map
    def contains(self, key):
        if self.get(key) != None:
            return True
        else:
            return False
    
    # Return the first value that matches the specified key 
    def get(self, key):
        bucketIndex = hash(key) % self.capacity
        if len(self.table[bucketIndex]) > 0:
            bucket = self.table[bucketIndex]
            for e in bucket:
                if e == key:
                    return e
                
        return None
  
    # Return all keys in a list
    def keys(self):
        keys = []
    
        for i in range(self.capacity):
            if len(self.table[i]) > 0:
                bucket = self.table[i] 
                for e in bucket:
                    keys.append(e)
    
        return keys

    # Return a string representation for the keys in this set
    def __str__(self):
        return str(self.keys())
                  
    # Remove all of the entries from this map 
    def clear(self):
        self.size = 0 # Reset map size
        
        self.table = [] # Reset map
        for i in range(self.capacity):
            self.table.append([])

    # Return the number of mappings in this map 
    def getSize(self):
        return self.size
        
    # Return true if this map contains no entries 
    def isEmpty(self):
        return size == 0
    
    # Rehash the map 
    def rehash(self):
        temp = self.keys() # Get elements
        self.capacity *= 2 # Double capacity    
        self.table = [] # Create a new hash table
        self.size = 0 # Clear size
        for i in range(self.capacity):
            self.table.append([])
            
        for e in temp:
            self.add(e) # Store to new table

    # Return the hash table as a string 
    def getTable(self):
        return str(self.table)
    
    # Return a string representation for this map 
    def setLoadFactorThreshold(self, threshold):
        self.loadFactorThreshold = threshold

def main():
    s1 = Set()
    s2 = Set()

    for i in range (10):
        s1.add(i)

    for j in range (5,15):
        s2.add(j)

    print("s1:", s1.keys())
    print("s2:", s2.keys())

    print("union of s1 and s2:", s1.union(s2).keys())
    print("s1 - s2:", s1.difference(s2).keys())
    print(s2.keys())
##    print(".....",s1.keys())
    print("s2 - s1:", s2.difference(s1).keys())
    print("s1 intersect s2:", s1.intersect(s2).keys())
    print("s1:", s1.keys())
    print("s2:", s2.keys())
    
if __name__ == "__main__":
    main()
















