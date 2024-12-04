#Converts the text into binary(1,0)
def String_to_bin(text):
    bin_MSG = ""        #Initialize an empty space to add the converted binary
    for char in text:
        bin_MSG += format(ord(char), '08b')     #convert each character into eight-bits with binary
    return bin_MSG

#Converts binary back into the original text (normal string)
def bin_to_String(binary):
    text = ""   #Initialize an empty space to add the convert encoded text
    for i in range(0, len(binary), 8):  # Each group of eight-bits represents one character
        byte = binary[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))   #convert the binary into integer then characters
    return text

#the part that encrypt the input message into the bmp image file Depending on the LSB styal 
def encrypt_part(image_path, message, output_path):
    #opening the image file using the binary read mode
    with open(image_path, 'rb') as image_file:
        image_data = bytearray(image_file.read())   #read the image as byte that can be modifaid 

#convert the text message into binary 
    bin_MSG = String_to_bin(message) + '01001010'   #add a (special end - 01001010) to make it easy to recognize.
    after_header1  = 54     #starting index after the bmp file header 

#replace each bit of the message with the last significant bit(LSB) of each pixel 
    for i in range(0, len(bin_MSG)):
        if after_header1  >= len(image_data):
            print("Shorten your message, please!.")     #displaying massage for the ussr if his message is too long 
            return

        bit = bin_MSG[i]
        byte = image_data[after_header1 ]
        byte = (byte & 0b11111110) | int(bit)   #edit only the last significant bit(LSB)
        image_data[after_header1 ] = byte
        after_header1 += 1

#extract a file with (.bmp extension)
    if not output_path.endswith('.bmp'):
        output_path += '.bmp'

## Save the encrypted image to the output file
    with open(output_path, 'wb') as out_file:
        out_file.write(image_data)

    print(f"Your secret has been saved successfully and saved as: {output_path}")

#the part that decrypt the secret message from the bmp image file Depending on the LSB styal
def decrypt_part(image_path):
    #opening the image file using the binary read mode 
    with open(image_path, 'rb') as img_file:
        img_data = bytearray(img_file.read()) #read the image as byte that can be modifaid

    bin_MSG = ""    #Initialize an empty space for the binary massage 
    after_header2 = 54       #starting index after the bmp file header

#Extract the last significant bit of each byte until the (special end - 01001010) is found
    while after_header2 < len(img_data):
        bin_MSG += str(img_data[after_header2] & 1)  #extract the LSB
        if bin_MSG.endswith('01001010'):    #Stop if you find the (special end - 01001010)ز
            break
        after_header2 += 1

    bin_MSG = bin_MSG[:-8] #remove the (special end - 01001010) from the binary message 
    
    #make sure of the binary message has Exactly 8-bits
    if len(bin_MSG) % 8 != 0:
        bin_MSG = bin_MSG[:-(len(bin_MSG) % 8)]

    decrypted_message = bin_to_String(bin_MSG) #convert the binary message into the text messge
    print(f"The decrypted message: {decrypted_message}")
 
#user interface
print("Welcome to [BMP MO' Steganography]\n **Use it wisely:)**")
print("Make your choice:")
print("1. Encrypt message")
print("2. decrypt message")

choice = input("Enter your choice: ")

#user has two opptations (encryption or decryption)
if choice == "1":
    path = input("Enter the BMP image path: ") #user input the bmp file path
    msg = input("Enter Your secret message: ")  #user input the secret massage
    output = input("Enter the output image name: ") # useer input the encrypted image name
    encrypt_part(path, msg, output) #call the encryption function
elif choice == "2":
    path = input("Enter the image path to decrypt: ")  #user input the encrypted bmp file path
    decrypt_part(path)  #call the decryption function
else:
    print("Invalid choice!") #involid choice error handleing 
