def encrypt(plaintext, shift_key):
    
    ciphertext = ""

    for char in plaintext:

        if char.isupper():
            
            char_index = ord(char) - ord("A")

            char_shifted = (char_index + shift_key) % 26 + ord("A")

            char_encrypted = chr(char_shifted)

            ciphertext += char_encrypted
        
        elif char.islower():

            char_index = ord(char) - ord("a")

            char_shifted = (char_index + shift_key) % 26 + ord("a")

            char_encrypted = chr(char_shifted)

            ciphertext += char_encrypted

        else :

            ciphertext += char

    return ciphertext

def decrypt(ciphertext, shift_key):
    
    decrypted_plaintext = ""

    for char in ciphertext:

        if char.isupper():

           char_index = ord(char) - ord("A")

           char_unshifted = (char_index - shift_key) % 26 + ord("A")

           char_decrypted = chr(char_unshifted)

           decrypted_plaintext += char_decrypted

        elif char.islower():
           
            char_index = ord(char) - ord("a")

            char_unshifted = (char_index - shift_key) % 26 + ord("a")

            char_decrypted = chr(char_unshifted)

            decrypted_plaintext += char_decrypted
        
        else:

            decrypted_plaintext += char
    
    return decrypted_plaintext
        
def main():
    
    plaintext = input("Enter Plaintext: ")

    shift_key = int(input("Enter Shift Key: "))

    encrypted_text = encrypt(plaintext, shift_key)

    decrypted_text = decrypt(encrypted_text, shift_key)

    print(f"Encrypted Text : {encrypted_text} \nDecrypted Text : {decrypted_text}")


if __name__ == "__main__":
    
    main()