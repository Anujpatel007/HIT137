def decrypt(cryptogram, shift):
    decrypted_text = ''
    for char in cryptogram:
        if char.isalpha():
            # with the specified amount shift the character
            decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A') if char.isupper() else
                                  (ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

def find_shift_key(cryptogram):
    for shift in range(26):
        decrypted_text = decrypt(cryptogram, shift)
        # check is there any patterns or words in the decrypted text
        if ' the ' in decrypted_text.lower() or ' and ' in decrypted_text.lower() or ' is ' in decrypted_text.lower():
            return shift
    return None

# given cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Finding the shift key
shift_key = find_shift_key(cryptogram)

if shift_key is not None:
    # by using the shift key output Decrypting the cryptogram
    original_quote = decrypt(cryptogram, shift_key)
    print("Shift Key:", shift_key)
    print("Original Quote:", original_quote)
else:
    print("Shift key not found.")