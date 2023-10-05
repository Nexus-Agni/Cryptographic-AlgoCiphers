import string

def create_vigenere_matrix():
    alphabet = string.ascii_uppercase
    vigenere_matrix = [[' ' for _ in range(26)] for _ in range(26)]
    
    for row in range(26):
        for col in range(26):
            vigenere_matrix[row][col] = alphabet[(row + col) % 26]
    
    return vigenere_matrix

def vigenere_encrypt(plain_text, key):
    vigenere_matrix = create_vigenere_matrix()
    plain_text = plain_text.upper()
    key = key.upper()
    encrypted_text = ""

    for i in range(len(plain_text)):
        if plain_text[i] == ' ':
            encrypted_text += ' '
        else:
            row = ord(key[i % len(key)]) - ord('A')
            col = ord(plain_text[i]) - ord('A')
            encrypted_text += vigenere_matrix[row][col]

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    vigenere_matrix = create_vigenere_matrix()
    encrypted_text = encrypted_text.upper()
    key = key.upper()
    decrypted_text = ""

    for i in range(len(encrypted_text)):
        if encrypted_text[i] == ' ':
            decrypted_text += ' '
        else:
            row = ord(key[i % len(key)]) - ord('A')
            col = vigenere_matrix[row].index(encrypted_text[i])
            decrypted_text += chr(col + ord('A'))

    return decrypted_text


key = input("Enter a key: ")
plain_text = input("Enter plain text: ")
    
encrypted_text = vigenere_encrypt(plain_text, key)
decrypted_text = vigenere_decrypt(encrypted_text, key)
    
print("Vigenère Matrix:")
for row in create_vigenere_matrix():
    print(" ".join(row))
    
print("\nPlain Text:   ", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)