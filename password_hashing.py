import hashlib

def sha256_hash_password(example_password, input_password):

    example_sha256_hash = hashlib.sha256(example_password).hexdigest()
    input_sha256_hash = hashlib.sha256(input_password).hexdigest()

    print("Example Password: ", example_password.decode("ASCII"))
    print("Example SHA256 hash:", example_sha256_hash)
    print("Input password: ", input_password.decode("ASCII"))
    print("Input SHA256 hash: ", input_sha256_hash)

    if (example_sha256_hash == input_sha256_hash):
        print("Passwords Match!!")
    else:
        print("Passwords Do Not Match!!")
    
def main():
    
    example_password = "password123".encode("ASCII")
    input_password = input("Please Enter Your Password: ").encode("ASCII")

    sha256_hash_password(example_password, input_password)
    

if __name__ == "__main__":
    main()