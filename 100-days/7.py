# hangman
import random

word_list = ["welcome", "zookeeper", "shopping"]

selected_index = random.randint(0,2)

print(selected_index)

selected_word = word_list[selected_index]

print(selected_word)

masked_word_list = selected_word.split(",")

print(masked_word_list)

masked_word = map(lambda x: "_", masked_word_list)

print(list(masked_word))