# sets
# used to create unique items and non index accisible elements

#create
my_set = {1,2,3,4,5,6,7,8,9,10}
my_set2 = {4,5,6,7,8,9,10,11,12}
my_set3 = {10,11,12,13,14,15,16}

#add/update element
print("*** add/update ***")

my_set.add(11)

#add multiple
my_set.update([12,13,23,24,34,56])

print(my_set)

#access set elements
print("*** access ***")
for el in my_set:
  print(el)

#conditional check
print(5 in my_set)
print(10 not in my_set)

#delete item
print("*** delete ***")
my_set.remove(6) #find and delete
# my_set.remove(100) # throws key error
my_set.discard(10)
my_set.discard(100) #wont throw key error

my_set.pop() #remove from starting
my_set.pop()
my_set.pop()
my_set.pop()

print(my_set)

#union
print("*** union ***")
print(my_set|my_set2)
print(my_set.union(my_set2))

#intersection
print("*** intersection ***")
print(my_set&my_set2)
print(my_set.intersection(my_set2))

#difference
print("*** difference ***")
print(my_set-my_set2)
print(my_set.difference(my_set2))

#frozen
frozen_sets = frozenset(my_set)
#frozen_sets.add(45) #throws AttributeError 'frozenset' object has no attribute 'add'