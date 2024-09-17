def encrypt(text, key):
    """Encrypts text using the Caesar cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key #Add key for encryption
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
        return encrypted_text
    
def decrypt(encrypted_text, key):
    """Decrypts text using the Caesar cipher."""
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key #Substract key for decryption
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted < ord ('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
        decrypted_text += chr(shifted)
    else:
        decrypted_text += char
    return decrypted_text

total = 0
for i in range(5):
    for j in range(5): #Corrected range
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2

original_code = "Nggnpx ng qnja"
key = total #Key is obtained from the corrected code
print("Key:", key)
print("Encrypted code:", original_code)
decrypted_code = decrypt(original_code, key)
print("Decrypted code:", decrypted_code)

key = total #Key stored in 'total'