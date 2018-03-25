class Dog():
	def __init__(self):
		pass
	def make_noise(self):
		print "Bark Bark"

class Cat():
	def __init__(self):
		pass
	def make_noise(self):
		print "Meow"

dog = Dog()
cat = Cat()

# dog.make_noise()
# cat.make_noise()

animals = [dog, cat]
for animal in animals:
	animal.make_noise()