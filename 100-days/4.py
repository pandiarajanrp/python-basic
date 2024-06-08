import random

rand_number = random.randint(1,100)
print(rand_number)

#list

states = ["CDMX", "Oxaca", "Yucatan"]

states.append("Merida")

states.extend(["Morelos", "Taxco"])

print(states)
print(states.pop())
print(states)
