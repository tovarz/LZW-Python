from collections import namedtuple

class hash_table:
    # public:
    def return_at(x):
        return array[x].element

    def find(x):
        current_pos = find_pos(x)
        if is_active(current_pos):
            return array[current_pos].element
        return None
    
    def insert(x):
        current_pos = find_pos(x)
        counter = counter + 1
        if is_active(current_pos):
            return
        array[current_pos] = hash_entry(x, "ACTIVE", counter)
    
    def remove(x):
        current_pos = find_pos(x)
        if is_active(current_pos):
            array[current_pos].info = "DELETED"
    
    def hash(key, table_size):  # hash function for the string
        hash_value = 0
        for i in range(0, len(key)):
            hash_value = 37 * hash_value + key[i]
        hash_value = hash_value % table_size
        if hash_value < 0:
            hash_value = hash_value + table_size
        return hash_value

    def return_code(x):
        current_pos = find_pos(x)
        return array[current_pos]
    
    def find_pos(x):
        current_pos = hash(x, len(array))
        while array[current_pos].info != "EMPTY" and array[current_pos].element != x:
            current_pos += 1
            if current_pos >= len(array):
                current_pos = current_pos - len(array)
        
        return current_pos

    def is_active(current_pos):
        return array[current_pos].info == "ACTIVE"

    def __init__(self, size = 4096):
        __counter = 0
        __hash_entry = namedtuple("hash_entry", "element info code")
        __array = [None] * size

    
    

