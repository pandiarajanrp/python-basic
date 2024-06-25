#calculator


def add(a, b):
  return a + b

def subract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def division(a, b):
  return a / b


operations = {
  "+": add,
  "-": subract,
  "*": multiply,
  "/": division
}

customer_chosen = input("Enter the operation to continue +, -, *, / ")
number1 = int(input("Enter number 1 "))
number2 = int(input("Enter number 2 "))


calc_operator = operations[customer_chosen]

result = calc_operator(number1, number2)

print(result)