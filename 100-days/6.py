#while loop

count = 0

# while count < 10:
#   count += 1
#   print(count)


#two pointer

list_data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

left_index = 0
right_index = len(list_data) - 1

sum = 0

while(left_index < right_index):
  sum += list_data[left_index] + list_data[right_index]
  left_index += 1
  right_index -= 1
  print(f"Left : {left_index}")
  print(f"Right : {right_index}")

print(sum)


strings = ["pandi", "raja", "john", "smith"]

filtered = filter(lambda x: len(x) > 4, strings)

print(list(filtered))