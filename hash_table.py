from collections import namedtuple

hash_entry = namedtuple("hash_entry", "element info code")

class hash_table:
    
    def return_at(self, x):
        return self.array[x].element

    def find(self, x):
        current_pos = self.find_pos(x)
        if is_active(current_pos):
            return self.array[current_pos].element
        return None
    
    def insert(self, x):
        current_pos = self.find_pos(x)
        counter = counter + 1
        if is_active(current_pos):
            return
        self.array[current_pos] = self.hash_entry(x, "ACTIVE", counter)
    
    def remove(self, x):
        current_pos = self.find_pos(x)
        if is_active(current_pos):
            self.array[current_pos].info = "DELETED"
    
    def hash(self, key, table_size):  # hash function for the string
        hash_value = 0
        for i in range(0, len(key)):
            k = ''.join(format(ord(x), 'b') for x in key[i])
            hash_value = 37 * hash_value + int(k, 2)
        hash_value = hash_value % table_size
        if hash_value < 0:
            hash_value = hash_value + table_size
        return hash_value

    def return_code(self, x):
        current_pos = self.find_pos(x)
        return self.array[current_pos]
    
    def find_pos(self, x):
        current_pos = self.hash(x, len(self.array))
        while self.array[current_pos].info != "EMPTY" and self.array[current_pos].element != x:
            current_pos += 1
            if current_pos >= len(array):
                current_pos = current_pos - len(array)
        
        return current_pos

    def is_active(self, current_pos):
        return self.array[current_pos].info == "ACTIVE"

    def __init__(self, size = 4096):
        self.counter = 0
        self.array = [hash_entry(0, "EMPTY", 0)] * size

    
    

