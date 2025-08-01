from tkinter import messagebox


def image_to_binary(file):
    with open(file, 'rb') as file:
        data = file.read()
        binary = ''
        for byte in data:
            binary += format(byte,'08b')
        return binary


def binary_to_bytes(binary):
    bytes_list = []
    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]
        bytes_list.append(int(byte, 2))
    return bytes(bytes_list)


def image_xor(binary_file,key):
    xor = []
    key_len = len(key)

    for i in range(len(binary_file)):
        bit = binary_file[i]
        key_bit = key[i % key_len]

        if bit == key_bit:
            xor.append('0')
        else:
            xor.append('1')

    return ''.join(xor)


def encrypt_image(file_original, key):
    file_binary = image_to_binary(file_original)
    image_cript = image_xor(file_binary, key)
    cript_bytes = binary_to_bytes(image_cript)

    with open(file_original, 'wb') as f:
        f.write(cript_bytes)
    messagebox.showinfo('Succes', 'Encrypt Successful')


def decrypt_image(file_original, key):
    file_binary = image_to_binary(file_original)
    image_decrypt = image_xor(file_binary, key)
    decrypt_bytes = binary_to_bytes(image_decrypt)

    with open(file_original, 'wb') as f:
        f.write(decrypt_bytes)
    messagebox.showinfo('Succes', 'Decrypt Successful')

















