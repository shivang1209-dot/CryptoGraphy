import hashlib

def hash(plaintext):
    md5_hash = hashlib.md5(plaintext).hexdigest()
    sha1_hash = hashlib.sha1(plaintext).hexdigest()
    sha256_hash = hashlib.sha256(plaintext).hexdigest()

    print("MD5 Hash: ", md5_hash)
    print("SHA1 Hash: ", sha1_hash)
    print("SHA256 Hash:", sha256_hash)

def main():

    plaintext = input("Enter Plaintext: ").encode("ASCII")
    hash(plaintext)

if __name__ == "__main__":
    main()