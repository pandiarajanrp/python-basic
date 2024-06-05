#Datatypes
print("========== Data Types =============")
#String
print("Hello" + "World")

#Integer
print(123 + 456)

print(567_789_764)

#Float
print(3.13 + 4.56)

#Boolean
print(True)
print(False)

print("========== Type Casting =============")

# Type Casting
print(str(100)) # "100"

print(int("100") + int("120")) #220

print(float("100.5") + float("200.45")) #300.95

print(type("welcome")) #str

first_name = "Pandiarajan"
num_char = len(first_name)

print("Your name has " + str(num_char)+ " character")

#Operators in python
print("========== Operators =============")
#Operators Priority
# PEMDASR - Paranthese, Exponent(of), Mul, Div, Add, Sub, R(Right) from left to right

print(3 + 3)

print(7 - 5)

print(7 * 5)

print(200 / 5) #float

print(5 ** 3)

print(204 // 5) #40 -> return the divided by 5 and not remaining

print(204 % 5) #4 -> return remaining after divided by 5 

#floor
print(round(8 / 3))

#round of
print(round(8 / 3, 3))

#f-string
score = 56
height = 5.6
isMale = True
print(f"Your score is {score}, and height is {height}, and you are male {isMale}")