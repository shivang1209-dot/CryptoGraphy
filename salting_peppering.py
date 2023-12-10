import hashlib
from Crypto.Random import get_random_bytes

def hash_password(password, salt, pepper):

    salted_peppered_pass = salt + password.encode() +  pepper

    hashed_password = hashlib.sha256(salted_peppered_pass).hexdigest()

    return hashed_password

def main():
    password = input("Please Enter Your Password: ")

    salt = get_random_bytes(16)

    pepper = get_random_bytes(16)

    hashed_password = hash_password(password, salt, pepper)

    print("Hashed Password: ", hashed_password)


if __name__ == "__main__":
    main()