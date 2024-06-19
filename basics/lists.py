letters = ['a', 'b', 'c', 'd','e','f']
matrix = [['a', 'b', 'c'], ['d','e','f']]

#sequence
same_number = [0] * 100

#concatenate
combined = letters + same_number

#iterable
numbers = list(range(20))
str_list = list("Hello World")

print(letters)
print(matrix)
print(numbers)
print(same_number)
print(combined)
print(str_list)

#accessing
print(letters[0]) #a
print(letters[-1]) #c

#set value
letters[0] = 'A'
print(letters)

#clone
letters_clone = letters[:]
print(letters_clone)

print("----- Slicing ------")
#slicing
from_beginning = letters[1:]
from_end = letters[:3]
with_range = letters[2:5]
print(from_beginning)
print(from_end)
print(with_range)

print("----- Step ------")
print(numbers[::2])
print(numbers[::-1]) # reverse

print("----- UnPacking ------")
first, second, *rest, last = numbers
print(first)
print(second)
print(rest)
print(last)

print("----- Looping ------")
for letter in letters:
  print(letter)

#with index using enumerate
for index, letter in enumerate(letters):
  print(index, letter)

print("----- Add/Remove ------")
#Add
numbers.append("g") #at end
numbers.insert(3, "x") #at given index
print(numbers)

#Remove
numbers.pop() #remove last
print(numbers)
numbers.pop(4) #remove with index
print(numbers)
numbers.remove(9) #remove by value. It will remove the first occurance
print(numbers)

del numbers[2:4] #delete with range
print(numbers)

numbers.clear() #reset
print(numbers)


print("----- Find ------")

print(letters.index("b"))
# print(letters.index("x")) #this will throw ValueError instead use by count or in operator
print(letters.count("x"))
if "x" in letters:
  print("X is in List")
