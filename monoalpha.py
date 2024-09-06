#Vedant Kale H3 2106090
def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_message += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encrypted_message += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            if char.isupper():
                decrypted_message += chr((ord(char) - 65 - key) % 26 + 65)
            else:
                decrypted_message += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message

message = "Hello all this is Vedant Kale"
key = 3

encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)