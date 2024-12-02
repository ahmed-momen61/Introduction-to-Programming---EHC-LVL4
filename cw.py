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