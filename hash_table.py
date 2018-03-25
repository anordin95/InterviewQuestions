class HashTable():

	def __init__(self, size = 113):
		self.values = [None] * size 
		self.size = size
	
	def lookup(self, key):
		hashed_key = self.hash(key)
		lookup_chained_list = self.values[hashed_key]
		for (k, v) in lookup_chained_list:
			if k == key:
				return v
	
	def hash(self, key):
		return key % self.size

	def insert(self, key, value):
		hashed_key = self.hash(key)
		lookup_chained_list = self.values[hashed_key]
		if lookup_chained_list == None:
			self.values[hashed_key] = [(key, value)]
		else:
			self.values[hashed_key].append((key, value))
			

	def delete(self, key):
		hashed_key = self.hash(key)
		lookup_chained_list = self.values[hashed_key]
		for idx, (k, v) in enumerate(lookup_chained_list):
			if k == key:
				self.values[hashed_key].pop(idx)
		return v

ht = HashTable()
print "Inserting two elements with same hash..."
print ht.insert(22, "John")
print ht.insert(22 + 113, "Abby")

print "Looking up both elements... "
print ht.lookup(22)
print ht.lookup(22 + 113)

print "Deleting both elements..."
print ht.delete(22)
print ht.delete(22 + 113)

print "Looking up both elements..."
print ht.lookup(22)
print ht.lookup(22 + 113)



