import hashlib

def calculate_checksum(file_path):

    with open(file_path, "rb") as f:

        file_hash = hashlib.sha256()

        while chunk := f.read(4096):

            file_hash.update(chunk)
        
    return file_hash.hexdigest()

def main():

    file_path = "example_file.txt"

    checksum = calculate_checksum(file_path)

    print("The Checksum Of ", file_path, " is ", checksum)

    with open(file_path, "w") as f:

        f.write("This File Has Been Modified")

    new_checksum = calculate_checksum(file_path)

    print("The New Checksum Is: ", new_checksum)

    if checksum == new_checksum:

        print("This File Has Not Been Tampered With !!")

    else:

        print("This File Is Corrupted !!!")

if __name__ == "__main__":
    main()