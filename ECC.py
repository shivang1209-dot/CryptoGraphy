from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

def generate_signature(private_key, plaintext):

    ECC_private_key = ECC.import_key(private_key)
    sha256_hash = SHA256.neww(plaintext)
    digital_signature = DSS.new(ECC_private_key, "fips-186-3").sign(sha256_hash)

    return digital_signature

def verify_signature(public_key, plaintext, digital_signature):

    ECC_public_key = ECC_import_key(public_key)
    verification_sha256_hash = SHA256.new(plaintext)

    try:
        DSS.new(ECC_public_key, "fips-186-3").verify(verification_sha256_hash, digital_signature)
        return "\nSignature Is Valid !!"
    
    except:
        return "\nSignature Is Invalid !!"

def main():

    plaintext = input("Enter Your Secret Message: ").encode()

    ECC_key = ECC.generate(curve="P-256")
    private_key = ECC_key.export_key(format="PEM")
    public_key = ECC_key.public_key().export_key(format="PEM")
    digital_signature = generate_signature(private_key, plaintext)

    print("\nPrivate Key: ", private_key)
    print("\nPublic Key: ", public_key)
    print("\nDigital Signature: ", digital_signature.hex())
    print(verify_signature(public_key, plaintext, digital_signature))

if __name__ == "__main__":
    main()