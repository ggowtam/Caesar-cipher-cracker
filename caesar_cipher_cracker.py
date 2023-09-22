mesg = "Yrzc Trvjri"
for shift in range(0,25):
    plaintext = ""
    for char in mesg:
        if not char.isalpha():  # to keep punctuation unchanged
            plaintext = plaintext + char
        elif char.isupper():
            c= ord(char)
            p=c-shift
            plaintext = plaintext + chr(65 + (p - 65) % 26)  # uppercase

        else:
            c= ord(char)
            p=c-shift
            plaintext = plaintext + chr(97 + (p - 97) % 26)  # lowercase 

    shift = shift + 1
    print("Cracked key", shift,":", plaintext)