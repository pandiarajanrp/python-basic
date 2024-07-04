# Type of Objects in python
# List
# Dictionaries
# Files
# Sets
# Program unit types
# Numbers
# String
# Tuples
# Other core types
# Implemenatation related types

#Explicit type conversion
"""
int()
float()
ord()
hex()
oct()
tuple()
set()
list()
dict()
str()
complex()
chr()
"""

#check type
print(type(25) == int)


#file types
sample_file = open("./sample.txt", "w")
sample_file.write("Hello World")
sample_file.close()

#Sets
#hold only unique elements
set_1 = set("INDIA")
set_2 = set(["USA", "United States of America", "USA"])
print(set_1)
print(set_2)

#complex
age = 60
comp_age = complex(age)
print(comp_age) #print real and imaginary value 60+0j

#tuple
country = "INDIA"
tup_country = tuple(country)
print(tup_country) # ('I', 'N', 'D', 'I', 'A')

#tuple to list
list_country = list(tup_country)
print(list_country) # ['I', 'N', 'D', 'I', 'A']

#bin, hec, oct
base = 10
base_bin = bin(base)
base_hex = hex(base)
base_oct = oct(base)
print(base_bin) # 0b1010
print(base_hex) # 0xa
print(base_oct) # 0o12

#char - get ascii char from code
char_for = 71
print(chr(char_for)) #G
print(chr(700)) # '
print(chr(2997)) # வ


#ord get unicode char
uni_code = 'U'
print(ord(uni_code)) # 85
print(ord("வ")) # 2997
print(ord("7")) # 55


