from PIL import Image
import stepic


def main():

    example_image_path = "example_image.png"
    message = "This Is A Secret Message"

    example_image = Image.open(example_image_path).convert("RGBA")
    message_bytes = message.encode()

    steganography = stepic.encode(example_image, message_bytes)

    steganographic_image_path = "steganographic_image.png"

    steganography.save(steganographic_image_path)

    steganographic_image = Image.open(steganographic_image_path)
    decoded_message = stepic.decode(steganographic_image)

    print("Decoded Message: ", decoded_message)

if __name__ == "__main__":
    main()