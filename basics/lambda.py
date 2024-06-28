# lambda function
# small functions, mostly with single line of expression
# suitable for simple logical operations
# used for list map and filter functions

add = lambda a, b: a+b
print(add(10,5))

#IIFE
print((lambda a, b: a * b)(10,5))

#parameter value:
product = lambda x, y, z: x - y
print(product(y=10, x=5, z=20))

#default value:
calc = lambda x=10, y=15, z=20: x + y + z
print(calc(5))

#use *args
calc_args = lambda *args: sum(args)
print(calc_args(5,10,19))

higher_order_fn = lambda x, fun: x + fun(x)
print(higher_order_fn(10, lambda x: x * x))

odd_even = lambda x: x % 2 == 0 and 'even' or 'odd'
print(odd_even(98))

#list helper
num = [1,4,6,9,12,23,45,65,76,89,95]
print(list(filter(lambda x: x > 10, num)))
print(list(map(lambda x: x * 10, num)))
