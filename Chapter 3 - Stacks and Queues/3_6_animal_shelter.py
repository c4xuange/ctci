# 3.6 Animal Shelter

# An animal shelter, which holds only dogs and cats, operates on a strictly FIFO basis.
# People must adopt either the "oldest" of all animals, or they can select whether they
# would prefer a dog or a cat. Create the data structures to maintain this system and
# implement operations like enqueue, dequeueAny, dequeueCat, and dequeueDog.

# Thoughts:
# - maintain all animals in a queue
# - keep track of head cat and head dog, use two linked lists to keep track of cats and dogs

class Animal:
	def __init__(self, specie, name):
		self.type = specie #"cat" or "dog"
		self.name = name
		self.nxt_any = None
		self.nxt_same = None

	def __str__(self):
		return self.type + ", " + self.name

class AnimalShelter:
	head = tail = None
	head_cat = last_cat = None
	head_dog = last_dog = None

	def enqueue(self, specie, name):
		animal = Animal(specie, name)
		if self.head == None:
			self.head = self.tail = animal
		else:
			self.tail.nxt_any = animal
			self.tail = animal

		if animal.type == "cat":
			if not self.head_cat:
				self.head_cat = self.last_cat = animal
			else:
				self.last_cat.nxt_same = animal
				self.last_cat = animal
		else:
			if not self.head_dog:
				self.head_dog = self.last_dog = animal
			else:
				self.last_dog.nxt_same = animal
				self.last_dog = animal


	def dequeueAny(self):
		if not self.head:
			return "Sorry, no more animals at this moment"

		animal = self.head
		if self.head.nxt_any == None:
			self.head = self.tail = None
		else:
			self.head = self.head.nxt_any

		if animal.type == "cat":
			if self.head_cat == self.last_cat:
				self.head_cat = self.last_cat = None
			else:
				self.head_cat = self.head_cat.nxt_same
		else:
			if self.head_dog == self.last_dog:
				self.head_dog = self.last_dog = None
			else:
				self.head_dog = self.head_dog.nxt_same

		return animal

	def dequeueCat(self):
		if self.head_cat == self.head:
			return self.dequeueAny()
		elif not self.head_cat:
			return "Sorry, no more cats at the moment"
		else:
			cat = self.head_cat
			self.head_cat = self.head_cat.nxt_same
			if not self.head_cat:
				self.last_cat = None
			self.dequeueAnimal(cat)
			return cat

	def dequeueDog(self):
		if self.head_dog == self.head:
			return self.dequeueAny()
		elif not self.head_dog:
			return "Sorry, no more dogs at the moment"
		else:
			dog = self.head_dog
			self.head_dog = self.head_dog.nxt_same
			if not self.head_dog:
				self.last_dog = None
			self.dequeueAnimal(dog)
			return dog

	def dequeueAnimal(self, animal):
		curr = self.head
		while curr.nxt_any != animal:
			curr = curr.nxt_any
		curr.nxt_any = animal.nxt_any

	def checkShelter(self):
		curr = self.head
		while curr != None:
			print(curr)
			curr = curr.nxt_any

if __name__ == "__main__":
	AS = AnimalShelter()
	print(AS.dequeueAny())
	AS.enqueue("cat", "Mel") #head, head_cat
	AS.enqueue("cat", "Sprinkles")
	AS.enqueue("dog", "Bonnie") #head_dog
	AS.enqueue("dog", "Tyson")
	AS.enqueue("cat", "Snuggles")
	print(AS.dequeueAny()) # cat, Mel
	print(AS.dequeueDog()) # dog, Bonnie
	print(AS.dequeueCat()) # cat, Sprinkles
	print(AS.dequeueCat()) # cat, Snuggles
	print(AS.dequeueCat()) # sorry, no more cats
	print(AS.dequeueDog()) # dog, Tyson
	print(AS.dequeueAny()) # sorry, no more animals
	AS.enqueue("cat", "Ginger")
	print(AS.dequeueDog()) # sorry, no more dogs
	print(AS.dequeueAny()) # cat, Ginger



