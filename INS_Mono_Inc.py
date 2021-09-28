monoalpha_cipher = {
    'a': 'm',
    'b': 'n',
    'c': 'b',
    'd': 'v',
    'e': 'c',
    'f': 'x',
    'g': 'z',
    'h': 'a',
    'i': 's',
    'j': 'd',
    'k': 'f',
    'l': 'g',
    'm': 'h',
    'n': 'j',
    'o': 'k',
    'p': 'l',
    'q': 'p',
    'r': 'o',
    's': 'i',
    't': 'u',
    'u': 'y',
    'v': 't',
    'w': 'r',
    'x': 'e',
    'y': 'w',
    'z': 'q',
    ' ': ' ',
}
print("Dhruvin Prajapati")

inverse_monoalpha_cipher = {}
for key, value in monoalpha_cipher.items():
    inverse_monoalpha_cipher[value] = key

message = input("Enter Your Text :")
result = message.lower()
encrypted_message = []
for letter in result:
    encrypted_message.append(monoalpha_cipher.get(letter, letter))

print("Encypted Message :", ''.join(encrypted_message))

decrypt_Msg = encrypted_message
decrypted_message = []
for letter in decrypt_Msg:
    decrypted_message.append(inverse_monoalpha_cipher.get(letter, letter))

print("Decrypted Message:", ''.join(decrypted_message))
