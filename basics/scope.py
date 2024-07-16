#### Scope ####

cart_count = 10

def add_item():
  cart_count = 25
  print(f"inside add_item {cart_count}")

add_item()
print(f"outside add_item {cart_count}")


# how to use global variable inside function

tree_name = "Apple"

def print_tree_name():
  global tree_name
  tree_name = "Orange"
  print(tree_name)

print_tree_name()


#how to use global variable as constant
PI = 3.141579
URL= "https://www.google.com"
PREFIX="Mr"

#write like a factory function

def user_name(name):
  return f"{PREFIX} {name}"

print(user_name("Pandiarajan"))