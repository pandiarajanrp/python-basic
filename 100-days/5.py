# Loops

states = ["CDMX", "Oxaca", "Yucatan"]

for state in states:
  print(state)


heights = "156 158 160 162 176 180"

heights_list = heights.split(" ")

total = 0
for height in heights_list:
  total += int(height)

print(total)
print(round(total/len(heights_list)))


#loop using range

for num in range(1, 21):
  print(num)
