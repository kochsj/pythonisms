class HashTable:
    def __init__(self, length=1024):
        self._length = length
        self._hash_table = [None]*self._length
        self.idx = 0

    def __iter__(self): 
        return self
  
    def __next__(self):  
        if self.idx > self._length-1:
            # self.idx = 0
            raise StopIteration 
        else: 
            self.idx += 1
            return self._hash_table[self.idx-1]


    def add(self, key, value=None):
        hsh = self._hash(key)

        if not self._hash_table[hsh]:
            self._hash_table[hsh] = []

        self._hash_table[hsh].append([key, value])

    def get(self, key):
        """Takes key as arguement; returns value from table at the hashed-key-index"""
        hashed_key = self._hash(key)
        key_index = self._hash_table[hashed_key]

        if key_index:
            for i in range(len(key_index)):
                if key == key_index[i][0]:
                    return key_index[i][1]
        return None

    def contains(self, key):
        """Takes key as arguement; Returns boolean if key is already in HashTable"""
        hashed_key = self._hash(key)
        key_index = self._hash_table[hashed_key]
        
        if key_index:
            if key == key_index[0][0]:
                return True
        return False
            
    def _hash(self, key):
        """
        Takes key as arguement
        Returns hash-index
        """
        #add ascii values of char together
        sum_chars = 0
        key = str(key)
        for char in key: 
            sum_chars += ord(str(char))
        #Square the sum
        square_sum = sum_chars**2
        #Floor devide by the first ascii value in key
        divide_square = square_sum // ord(key[0])
        #Mod length of hash table and return
        return (divide_square % self._length)

    def get_length(self):
        return self._length