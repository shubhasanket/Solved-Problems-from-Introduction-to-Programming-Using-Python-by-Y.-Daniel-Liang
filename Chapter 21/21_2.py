'''21.2 (Implement Map using open addressing with quadratic probing)
Implement Map using open addressing with quadratic probing. For simplicity,
use f(key) = key % size as the hash function, where size is the hash-table
size. Initially, the hash-table size is 4. The table size is doubled
whenever the load factor exceeds the threshold (0.5).
'''

# Define the default hash-table size
DEFAULT_INITIAL_CAPACITY = 4
  
# Define default load factor
DEFAULT_MAX_LOAD_FACTOR = 0.5 
     
# Define the maximum hash-table size to be 2 ** 30
MAXIMUM_CAPACITY = 2 ** 30 
  
class Map:
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
        
        self.size = 0 # Initialize map size

    # Add an entry (key, value) into the map 
    def put(self, key, value):
        if self.size >= self.capacity * self.loadFactorThreshold:          
            if self.capacity == MAXIMUM_CAPACITY:
                raise RuntimeError("Exceeding maximum capacity")
      
            self.rehash()
        
        # Quadratic probing
##        key
        k = 0
        while (self.table[(key+k**2)% self.capacity]): # k += 1 until an empty slot is found
            k += 1
        bucketIndex = (key+k**2) % self.capacity

        # Add an entry (key, value) to hashTable[index]
        self.table[bucketIndex].append([key, value])

        self.size += 1 # Increase size

##        print("Successfully inserted", (key, value))

    def search(self, key, entry):
        '''To search for an entry in the hash table, obtain the index,
            say k, from the hash function for the key. Check whether
            hashTable[k % n] contains the entry. If not, check whether
            hashTable[(k+1) % n] contains the entry, and so on, until
            it is found, or an empty cell is reached.
        '''
        k = 1
##        print(key % self.capacity)
        if not self.table[key % self.capacity]:
            return False
        elif self.table[key % self.capacity][0] == [key, entry]:
            pass
        else:
            while self.table[(key+k**2) % self.capacity][0] != [key, entry]:
                k += 1
##                print(k,k%self.capacity)
                if not self.table[(key+k**2)%self.capacity]:
                    return False
        return True  
 
    # Remove the entry for the specified key 
    def remove(self, key):
        bucketIndex = key % self.capacity
##        print(key,bucketIndex)
        if bucketIndex != 0:
            mem = bucketIndex-1
        else:
            mem = self.capacity-1
        check = True
        # Remove the first entry that matches the key from a bucket
        while bucketIndex != mem:
            if len(self.table[bucketIndex]) > 0:
                entry = self.table[bucketIndex]
##                print(key, entry)
                if entry[0][0] == key:
                    self.table[bucketIndex] = []
                    self.size -= 1 # Decrease size
                    check = False
                    break # Remove just one entry that matches the key
                
            bucketIndex = (bucketIndex+1) % self.capacity
##            print("...")
##        print(".....", bucketIndex)
        if bucketIndex == mem and check:
##            print("in here")
            if len(self.table[bucketIndex]) > 0:
                entry = self.table[bucketIndex]
                if entry[0][0] == key:
                    self.table[bucketIndex] = []
                    self.size -= 1 # Decrease size

    # Return true if the specified key is in the map
    def containsKey(self, key):
        if self.get(key) != None:
            return True
        else:
            return False
  
    # Return true if this map contains the specified value 
    def containsValue(self, value):
        for i in range(self.capacity):
            if len(self.table[i]) > 0:
                bucket = self.table[i]
                for entry in bucket:
                    if entry[1] == value:
                        return True
    
        return False
  
    # Return a set of entries in the map 
    def items(self):
        entries = []
    
        for i in range(self.capacity):
            if self.table[i] != None:
                bucket = self.table[i]
                for entry in bucket:
                    entries.append(entry)
        return tuple(entries)
    
    # Return the first value that matches the specified key 
    def get(self, key):
        bucketIndex = hash(key) % self.capacity
        if len(self.table[bucketIndex]) > 0:
            bucket = self.table[bucketIndex]
            for entry in bucket:
                if entry[0] == key:
                    return entry[1]
                
        return None
  
    # Return all values for the specified key in this map
    def getAll(self, key):
        values = []
        bucketIndex = hash(key) % self.capacity
        if len(self.table[bucketIndex]) > 0:
            bucket = self.table[bucketIndex]
            for entry in bucket:
                if entry[0] == key:
                    values.append(entry[1])
    
        return tuple(values)
  
    # Return a set consisting of the keys in this map
    def keys(self):
        keys = []
    
        for i in range(0, self.capacity):
            if len(self.table[i]) > 0:
                bucket = self.table[i] 
                for entry in bucket:
                    keys.append(entry[0])
    
        return keys
  
    # Return a set consisting of the values in this map 
    def values(self):
        values = []
    
        for i in range(self.capacity):
            if len(self.table[i]) > 0:
                bucket = self.table[i] 
                for entry in bucket:
                    values.append(entry[1])
        return values
                  
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
        temp = self.items() # Get entries
        self.capacity *= 2 # Double capacity    
        self.table = [] # Create a new hash table
        self.size = 0 # Clear size
        for i in range(self.capacity):
            self.table.append([])
            
        for entry in temp:
            self.put(entry[0], entry[1]) # Store to new table

    # Return the entries as a string 
    def toString(self):
        return str(self.items())
    
    # Return a string representation for this map 
    def setLoadFactorThreshold(self, threshold):
        self.loadFactorThreshold = threshold

    # Return the hash table as a string 
    def getTable(self):
        return str(self.table)

def main():
##    print(1)
    m = Map()
    m.put(30, "S")
    m.put(300145, "M")
    m.put(21, "H")
    print(m.getTable())
    print(m.search(300145, "M"))
    m.remove(30)
    print(m.getTable())
    m.remove(300145)
    print(m.getTable())
    m.remove(21)
    print(m.getTable())
    

if __name__ == "__main__":
    main()



































