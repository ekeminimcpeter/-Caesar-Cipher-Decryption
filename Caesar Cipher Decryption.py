# Author: Ekemini Peter
# Date: December 08, 2024
# Description: Original implementation of Caesar Cipher Decryption.
# Thanks to ChatGPT for spotting a subtle error - a missing parenthesis, and robust testing of code based on scope and requirement.
# Scope: Maintain character cases and non-alphabetic characters.

##################################################################################################

# Caesar cipher.

# Collect user text and shift value
encrypted_text = input("Enter your message to be decrypted: ")
shift_number = int(input("Enter your desired shift value from '1 and 25': "))
decrypted_text = ''

# Decrypt text according to shift value
try:                                # Check validitity of shift value.
    if shift_number in range(1,26): # Restrict user to shift range of 1–25 to ensure the decryption is both valid and non-trivial.
        for char in encrypted_text:
            if char.isalpha():
                if char.islower():
                    decrypted_char_code = ord(char) - shift_number # Compute code word for decrypting lower case text character 
                    if decrypted_char_code < ord('a'):
                        decrypted_char_code = decrypted_char_code + 26 # Cause a cyclic decrypting on lower case letters
                elif char.isupper():
                    decrypted_char_code = ord(char) - shift_number # Compute code word for decrypting upper case text character
                    if decrypted_char_code < ord('A'):
                        decrypted_char_code = decrypted_char_code + 26 # Cause a cyclic decryption on upper cases letters
                decrypted_text += chr(decrypted_char_code)
            else:
                decrypted_text += char
        print(decrypted_text)
    else:
        raise ValueError
    
# Manage exception error from non-valid shift value  
except ValueError:
    print("Error: Shift value is invalid! Enter a value between '1 and 25'")



