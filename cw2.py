def text_to_binary(text):
    binary_message = ""
    for char in text:
        binary_message += format(ord(char), '08b')
    return binary_message

def binary_to_text(binary):
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text

def encode(image_path, message, output_path):
    with open(image_path, 'rb') as img_file:
        img_data = bytearray(img_file.read())

    binary_message = text_to_binary(message) + '11111111'
    message_index = 54

    for i in range(0, len(binary_message)):
        if message_index >= len(img_data):
            print("Message too long!")
            return

        bit = binary_message[i]
        byte = img_data[message_index]
        byte = (byte & 0b11111110) | int(bit)
        img_data[message_index] = byte
        message_index += 1

    if not output_path.endswith('.bmp'):
        output_path += '.bmp'