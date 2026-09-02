import random as ran
import string as str

chars = " " + str.punctuation + str.digits + str.ascii_letters

chars = list(chars)
key = chars.copy()
ran.shuffle(key)

# print(f'chars : {chars}')
# print(f'key: {key}')


# encrpytion
message = input('Enter message to encrypt: ')
cipher_message = ""


for letter in message:
    index = chars.index(letter)
    cipher_message += key[index]


print(f"original message: {message}")
print(f"encrypted message: {cipher_message}")


# decrypt
cipher_message = input('copy message to decrypt: ')
message = ""


for letter in cipher_message:
    index = key.index(letter)
    message += chars[index]

print(f"encrypted message: {cipher_message}")
print(f"original message: {message}")
