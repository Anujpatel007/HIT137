def decrypt_caesar(ciphertext, shift):
    """Decrypts a Caesar cipher with a given shift."""
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Shift character back to its original position
            base = ord('A') if char.isupper() else ord('a')
            new_char_code = (ord(char)) - base - shift) % 26 + base
            decrypted_text += chr(new_char_code)
        else:
            # Keep non-alphabetical characters as they are
            decrypted_text += char
    return decrypted_text

#Store the encrypted code
code = """tybonny_inevnoyr = 100"""
zl_qvpg = {'xrl1': 'inyhr1', 'xr12': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xr14'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    V += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba" zrg!")
          
vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(z1 frg)"""

# Decrypt the code
decrypted_code = decrypt_caesar(code, 13)

# Print the decrypted code
print(decrypted_code)