str_text = 'Hello World'
print(str_text[1])
print(len(str_text))
print(str_text + ' Welcome to Python !!!')

#type cast
pi = 3.14
concat_str = 'The value of pi is '  + str(pi)

raw = r'this\t\n and that'

# this\t\n and that
print(raw)

multi = """It was the best of times.
It was the worst of times."""

# It was the best of times.
#   It was the worst of times.
print(multi)

str_manipulate = "Welcome to Python Strings"

print(str_manipulate.lower())
print(str_manipulate.upper())
print(str_manipulate.find('Python'))

# separate by space
print(str_manipulate.split())

# js split method
print([*str_manipulate])

letter = [x for x in str_manipulate]
print(letter)

print(list(str_manipulate))

lst = []
lst.extend(str_manipulate)
print(lst)

lst2 = []
lst2[:] = str_manipulate
print(lst2)

#join method in js
print("--".join([*str_manipulate]))


#slices:

str_to_slice = "Hello World"

print(str_to_slice[1:4])
print(str_to_slice[1:])
print(str_to_slice[:4])

print(str_to_slice[-1:])
print(str_to_slice[:-4])
print(str_to_slice[-4:])


# formatting

value = 2.791514
print(f'approximate value = {value:.2f}')  # approximate value = 2.79

car = {'tires':4, 'doors':2}
print(f'car = {car}') # car = {'tires': 4, 'doors': 2}
