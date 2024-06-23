#create
print("*** create ***")

numbers = 1,2,3,4,5,6,7
print(numbers)

duplicates = 1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,4,5,6,7

squares = (1,4,9,16,25,36,49,64)
print(squares)

alphabets = ['a','b','c','d','e','f']
alphas = tuple(alphabets)
print(alphas)

#access
print("*** access ***")
print(numbers[5])
#print(numbers[20]) #throws index error
print(10 in numbers) #membership test

#modify
print("*** modify ***")
#numbers[5] = 34 #throws TypeError as tuples cant be modify

print("*** concatinate ***")
print(numbers + squares)

print("*** looping ***")
for i in numbers:
  print(i)

print("*** slicing ***")
print(numbers[2:5])
print(numbers[-2:])
print(numbers[-5:-2])

print("*** delete ***")
#del numbers
#print(numbers) #thorws NameError as tuple deleted completely

print("*** methods ***")
print(len(numbers))

print(duplicates.count(1))

print(duplicates.count(2))

print(duplicates.index(1)) #return fist index of an item even if it has duplicate

print(duplicates.index(6)) #find index by value

