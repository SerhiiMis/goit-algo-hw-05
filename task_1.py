class HashTable:
    def __init__(self, size):
        # Initialize the size of the hash table
        self.size = size
        # Create an empty hash table with 'size' number of slots
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Compute the hash value for the given key using Python's built-in hash function
        return hash(key) % self.size
    
    def insert(self, key, value):
        # Compute the hash value for the given key
        key_hash = self.hash_function(key)
        # Create a key-value pair to insert
        key_value = [key, value]
        # Get the slot (bucket) corresponding to the hash value
        slot = self.table[key_hash]

        # Iterate through the key-value pairs in the slot
        for i, kv in enumerate(slot):
            # Extract the key from the key-value pair
            k, _ = kv
            # If the key already exists in the slot, update its value
            if key == k:
                slot[i] = key_value
                return True

        # If the key doesn't already exist in the slot, append the new key-value pair
        else:
            slot.append(key_value)
            return True

    def delete(self, key):
        # Compute the hash value for the given key
        key_hash = self.hash_function(key)

        # Get the slot (bucket) corresponding to the hash value
        slot = self.table[key_hash]

        # Iterate through the key-value pairs in the slot
        for pair in slot:
            # If the key is found, remove the key-value pair
            if pair[0] == key:
                slot.remove(pair)
                return True
        # If the key is not found, return False
        return False

    def get(self, key):
        # Compute the hash value for the given key
        key_hash = self.hash_function(key)
        # Get the slot (bucket) corresponding to the hash value
        slot = self.table[key_hash]

        # Iterate through the key-value pairs in th slot
        for pair in slot:
            # If the key is found, return its corresponding value
            if pair[0] == key:
                return pair[1]
        # If the key is not found, return None
        return None# Create a hash table instance with size 5

H = HashTable(5)

# Insert key-value pairs
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

# Print the hash table after insertion
print("Hash table after insertion:")
print(H.table)

# Test retrieval of values
print("Retrieving values:")
print("apple:", H.get("apple"))     # Output: 10
print("orange:", H.get("orange"))   # Output: 20
print("banana:", H.get("banana"))   # Output: 30
print("none:", H.get("none"))       # Output: None

# Test deletion of keys
print("Deleting keys:")
print("Deleting apple:", H.delete("apple"))   # Output: True
print("Deleting none:", H.delete("none"))     # Output: False
print("apple:", H.get("apple"))              # Output: None
print("Deleting apple again:", H.delete("apple"))   # Output: False
print("none:", H.get("none"))                # Output: None

# Print the hash table after deletion
print("Hash table after deletion:")
print(H.table)

     
        