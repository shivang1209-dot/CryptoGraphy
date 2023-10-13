def caesar_bruteforce(ciphertext):

    for shift_key in range(0, 26):
        
        decrypted_plaintext = ""

        for char in ciphertext:
            
            if char.islower():

                char_index = ord(char) - ord("a")

                char_unshifted = (char_index - shift_key) % 26 + ord("a")

                char_decrypted = chr(char_unshifted)

                decrypted_plaintext += char_decrypted

            else:

                decrypted_plaintext += char

        print("Shift : " + str(shift_key) + ", Decrypted Text : " + decrypted_plaintext)

def main():

    ciphertext = input("Enter Ciphertext : ")

    caesar_bruteforce(ciphertext)

if __name__ == "__main__":
    
    main()