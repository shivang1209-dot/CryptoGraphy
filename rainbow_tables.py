import hashlib

def main():
    
    rainbow_table = {}

    common_passwords = ["password", "admin", "123456", "abcdef", "letmein"]

    for password in common_passwords:

        hash_value = hashlib.sha256(password.encode()).hexdigest()
        rainbow_table[hash_value] = password

    password_to_crack = input("Please Enter The Password You Wish To Crack: ")
    hashed_password = hashlib.sha256(password_to_crack.encode()).hexdigest()

    if hashed_password in rainbow_table:
        print("Password: ", {rainbow_table[hashed_password]}, "Found For Hash ", {hashed_password})
    else:
        print("Password Not Found In Rainbow Table.")

if __name__ == "__main__":
    main()
