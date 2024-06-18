# hangman
import random

word_list = ["welcome", "zookeeper", "shopping"]

#generated masked text
masked_text = []
selected_word = []

selected_index = random.randint(0,2)

word_length = len(word_list[selected_index])

for el in range(word_length):
  masked_text += "-"

selected_word = [*word_list[selected_index]]

while("".join(masked_text) != "".join(selected_word)):
  print(masked_text)
  customer_input = input("Enter the letter to find ").lower()
  for k,v in enumerate(selected_word):
    if(v == customer_input):
      masked_text[k] = customer_input

print(masked_text)