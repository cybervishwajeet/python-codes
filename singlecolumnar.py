#Vedant Kale H3 2106090
def encrypt(plaintext, key):
    key_order = sorted(range(len(key)), key=key.__getitem__)
    ciphertext = ''.join(plaintext[i] for col in key_order for i in range(col, len(plaintext), len(key)))
    return ciphertext

def decrypt(ciphertext, key):
    key_order = sorted(range(len(key)), key=key.__getitem__)
    plaintext = [''] * len(ciphertext)
    index = 0
    for col in key_order:
        for i in range(col, len(ciphertext), len(key)):
            plaintext[i] = ciphertext[index]
            index += 1
    return ''.join(plaintext)

# Example usage
plaintext = "HELLO WORLD"
key = "COLUMNAR"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)