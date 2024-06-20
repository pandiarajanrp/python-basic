def paint_cal(height, width, coverage):
  return (height * width) / coverage

# Ceasar Ciber Encryption

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Enter 'encode' for encode and 'decode' for decode ")
text = input(f"Enter text ").lower()
shift = int(input("Enter shift length "))

text_len = len(text)

def encode():
  encoded_text = ''
  for letter in text:
    idx = alphabets.index(letter)
    idx_shift = idx + shift
    new_position = (idx_shift - 26) if idx_shift > 25 else idx_shift
    encoded_text += alphabets[new_position]
  return encoded_text

def decode():
  decoded_text = ''
  for letter in text:
    idx = alphabets.index(letter)
    idx_shift = idx - shift
    decoded_text += alphabets[idx_shift]
  return decoded_text

#print(f"encoded {encode()}")
print(f"decoded {decode()}")
