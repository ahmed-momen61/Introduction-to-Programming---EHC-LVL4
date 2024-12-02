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