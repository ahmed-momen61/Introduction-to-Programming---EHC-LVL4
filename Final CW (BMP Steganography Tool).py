def String_to_bin(text):
    bin_MSG = ""
    for char in text:
        bin_MSG += format(ord(char), '08b')
    return bin_MSG

def bin_to_String(binary):
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text

def encrypt_part(image_path, message, output_path):
    with open(image_path, 'rb') as image_file:
        image_data = bytearray(image_file.read())

    bin_MSG = String_to_bin(message) + '01001010'
    after_header1  = 54

    for i in range(0, len(bin_MSG)):
        if after_header1  >= len(image_data):
            print("Shorten your message, please!.")
            return

        bit = bin_MSG[i]
        byte = image_data[after_header1 ]
        byte = (byte & 0b11111110) | int(bit)
        image_data[after_header1 ] = byte
        after_header1 += 1

    if not output_path.endswith('.bmp'):
        output_path += '.bmp'

    with open(output_path, 'wb') as out_file:
        out_file.write(image_data)

    print(f"Your secret has been saved successfully and saved as: {output_path}")

def decrypt_part(image_path):
    with open(image_path, 'rb') as img_file:
        img_data = bytearray(img_file.read())

    bin_MSG = ""
    after_header2 = 54

    while after_header2 < len(img_data):
        bin_MSG += str(img_data[after_header2] & 1)
        if bin_MSG.endswith('01001010'):
            break
        after_header2 += 1

    bin_MSG = bin_MSG[:-8]
    
    if len(bin_MSG) % 8 != 0:
        bin_MSG = bin_MSG[:-(len(bin_MSG) % 8)]

    decrypted_message = bin_to_String(bin_MSG)
    print(f"The decrypted message: {decrypted_message}")
    
print("Welcome to [BMP MO' Steganography]\n **Use it wisely:)**")
print("Make your choice:")
print("1. Encrypt message")
print("2. decrypt message")

choice = input("Enter your choice: ")

if choice == "1":
    path = input("Enter the BMP image path: ")
    msg = input("Enter Your secret message: ")
    output = input("Enter the output image name: ")
    encrypt_part(path, msg, output)
elif choice == "2":
    path = input("Enter the image path to decrypt: ")
    decrypt_part(path)
else:
    print("Invalid choice!")
