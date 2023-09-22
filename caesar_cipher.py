
# Takes in a plaintext message
# and an integer key and encrypts
# using the Caesar cipher approach
def encrypt(mesg, key):
    #  implementing encryption approach
    result_e = ''
    for char in mesg:
        if char.isalpha(): # for Uppercase
            char_code = ord(char)
            key_char_code = char_code + key
            result_e += chr(((key_char_code - 65) % 26 + 65)) # Uppercase
        elif char.islower(): # for Lowercase
            result_e += chr(((key_char_code - 97) % 26 + 97)) # Lowercase
        else:
            result_e = result_e + char # keeping the space as it is

    print("Encrypted Text is:", result_e) # printing Encrypted text
# Takes in an encrypted message
# and an integer key and decrypts
# using the Caesar cipher approach
def decrypt(mesg, key):
    # implementing decryption approach
    result_d = ''
    for char in mesg:
        char_code = ord(char)
        key_char_code = char_code - key
        if char.isupper():
                result_d += chr(((key_char_code - 65 + 26) % 26) + 65) # Uppercase
        elif char.islower():
                result_d += chr(((key_char_code - 97  + 26) % 26) + 97) # Lowercase
        else:
            result_d = result_d + char # keeping the space as it is

    print("Decrypted Text is:", result_d) # printing Decrypted text
def main():
    encrypt("Hello World", 34)
    encrypt("Network cybersecurity", -5)
    decrypt("O gs voiqrk Xoiq", 32)

if __name__ == '__main__':
    main()
