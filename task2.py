import cv2
import numpy as np

def encrypt_decrypt_image(image_path, key, output_path):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found!")
        return

    # Apply XOR operation on each pixel
    encrypted_image = cv2.bitwise_xor(image, (key, key, key))

    # Save the resulting image
    cv2.imwrite(output_path, encrypted_image)
    print(f"Image saved at {output_path}")

# Example usage
if __name__ == "__main__":
    print("Simple Image Encryption/Decryption Tool")
    mode = input("Choose mode: [E]ncrypt or [D]ecrypt: ").lower()
    input_path = input("Enter image path: ")
    key = int(input("Enter secret key (e.g., 123): "))

    if mode == 'e':
        encrypt_decrypt_image(input_path, key, "encrypted_image.png")
    elif mode == 'd':
        encrypt_decrypt_image(input_path, key, "decrypted_image.png")
    else:
        print("Invalid mode selected.")
