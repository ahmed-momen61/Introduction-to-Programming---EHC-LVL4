BMP Steganography Tool A simple Pyhton program made to conceal and retrieve text messages inside the pixels of a BMP image file using the least significant bit method.

* Features Hide Messages: 
Users can encode secret messages into BMP Image Files. 
Extract Messages: Users can decode images files and see the hidden message that is embedded into the images. 

* How It Works:
In this practice, the instrument edits the least significant bit of every pixel for the purpose of concealing the binary version of the message.
A unique end flag (01001010) indicates the end of the message being encoded.

* Requirements:
compiler support pythone language 
BMP image format

* Usage:
Run the script
Choose an option:
1 to encode a message.
2 to decode a message.

* Example:
1 Encode a Message
- Enter the BMP image path: input_image.bmp
- Enter the message to encode: Hello, World!
- Enter the output BMP image name: output_image.bmp
- Message encoded and saved as: output_image.bmp

2 Decode a Message
- Enter the BMP image path to decode: output_image.bmp
- Decoded message: Hello, World!

* Notes
Supports only BMP images.
Ensure the message size fits within the image's pixel capacity.
