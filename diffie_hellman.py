from random import randint

def main():

    prime = 23
    primitive_root = 9

    bob_private_key = randint(1, prime - 1)
    alice_private_key = randint(1, prime - 1)

    bob_public_key = pow(primitive_root, bob_private_key, prime)
    alice_public_key = pow(primitive_root, alice_private_key, prime)

    shared_secret_key_bob = pow(alice_public_key, bob_private_key, prime)
    shared_secret_key_alice = pow(bob_public_key, alice_private_key, prime)
    
    if (shared_secret_key_alice == shared_secret_key_bob):
        print("Shared Secret Successfully !!")
        print("Bob's Secret key: ", bob_private_key)
        print("Alice' Secret Key: ", alice_private_key)
        print("Bob's Public key: ", bob_public_key)
        print("Alice' Public Key: ", alice_public_key)
        print("Bob's Shared Secret Key: ", shared_secret_key_bob)
        print("Alice's Shared Secret Key: ", shared_secret_key_alice)

    else:
        print("Shared Secret Computation Failed :( ")

if __name__ == "__main__":
    main()