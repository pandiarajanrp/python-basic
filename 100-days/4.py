import random

rand_number = random.randint(1,100)
# print(rand_number)

#list

states = ["CDMX", "Oxaca", "Yucatan"]

states.append("Merida")

states.extend(["Morelos", "Taxco"])

# print(states)
# print(states.pop())
# print(states)


rock = 0
paper = 5
scissors = 2

user_input = int(input("Enter 0 for rock, 5 for paper, 2 for scissior "))

admin_data_set = [rock, paper, scissors]
admin_input = admin_data_set[random.randint(0,2)]

print(f"Admin Selected {admin_input}")
print(f"You selected {user_input}")

if (admin_input == user_input):
  print("DRAW!!!!")
elif ((admin_input == rock and user_input is not paper) or (admin_input == paper and user_input is not scissors) or (admin_input == scissors and user_input is not rock)):
  print("You Lose!!")
elif ((user_input == rock and admin_input is scissors) or (user_input == paper and admin_input is rock) or (user_input == scissors and admin_input is paper)):
  print("You Win!!")