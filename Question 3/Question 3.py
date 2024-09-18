# On The LINE NUMBER 69 AND 70 AND UNCOMMENT TO SEE THE WORKING OF DECRYPTION FUNCTION
# THE KEY IS 13
# FOR DECRYPTING OF THE CODE STARTS FROM LINE NUMBER 73 

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key  # Decrypt by Minusing the key
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
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

key = 13
encrypt_code = """
                tybony_inevnoyr = 100
                zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

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
                erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

                qrs zbqvsl_qvpg():
                    ybpny_inevnoyr = 10
                    zl_qvpel['xrl4'] = ybpny_inevnoyr

                zbqvsl_qvpg(5)

                qrs hcqngr_tybony():
                    tybony tybony_inevnoyr
                    tybony_inevnoyr += 10

                sbe v va enatr(5):
                    cevag(v)
                    v += 1

                vs z1_frg vf abg Abar naq z1_qvpg['xrl4'] == 10:
                    cevag("Pbaqvgvba zrg!")

                vs 5 abg va zl_qvpg:
                    cevag("5 abg sbhaq va gur qvpgvbanel!")

                cevag(tybony_inevnoyr)
                cevag(zl_qvpg)
                cevag(zl_frg)
"""
# decrypted_code = decrypt(encrypt_code, key)
# print(decrypted_code)


global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers()  # true the function call and removed the unnecessary argument

def modify_dict():
    global my_dict  # having the global keyword
    local_variable = 10
    my_dict['key4'] = local_variable  # The dictionary key

modify_dict()  # The function call

def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
    i += 1

if my_set is not None and my_dict.get('key4') == 10:  # Corrected the condition and dictionary key access
    print("Condition met!")

if 5 not in my_dict.values():  # The Required condition
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)