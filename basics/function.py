def print_message(message):
  print(f"Message to display {message}")

def get_params(a, *args, values=[], **kwargs):
  print(a, args, values ,kwargs)

get_params("a", 1,2,3,4,5, values=[1,2,3,4,5], base=24, exp=34)


#return function inside a function

def function_caller(fun, *args, **kwargs):
  return fun(*args, **kwargs)

def sum(a, b):
  return a + b

result = function_caller(sum, 10,15)
print(result)


#clousures
def adder(value):
  def modifier_handler(add_value):
    return value + add_value
  return modifier_handler

adder_5 = adder(5) #return a factory method to send the param which will act as same in base function
adder_10 = adder(10)

print(adder_5(10), adder_5(20))
print(adder_10(15), adder_10(20))

#decorator
def function_handler(func):
  def process_function(*args, **kwargs):
    print(f"Function processing with args and kwargs {args} {kwargs}")
    result = func(*args, **kwargs)
    print(f"Result is {result}")

  return process_function

@function_handler
def add_data(el,el2):
  return el + el2

add_data(2,3)

#nonlocal

def outer_function():
  x = 10

  def inner_function():
    nonlocal x
    x = 20 # it wont rewrite the outer function variable until we give nonlocal
    print(f"Inner Function X: {x}")

  inner_function()
  
  print(f"Outer function X: {x}")

outer_function()
