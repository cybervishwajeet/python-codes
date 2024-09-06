

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Example usage
plaintext = "Hello all I am Vishwa 26 "
shift = 3
ciphertext = caesar_cipher(plaintext, shift)
print("Ciphertext:", ciphertext)
