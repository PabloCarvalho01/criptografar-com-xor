from tkinter import messagebox

def txt_to_binary(file):
    with open(file, 'rb') as file:
        data = file.read()
        result = ''
        for byte in data:
            result +=  format(byte, '08b')

        list = []

        for i in range(0, len(result), 8):
            list.append(result[i:i + 8])

        return list


def binary_to_encrypt(file_binary, file_to_encrypt, key):
    encrypted = []

    for i in range(len(file_binary)):
        for j in range(len(file_binary[i])):
            if file_binary[i][j] == key[j]:
                encrypted.append('0')
            else:
                encrypted.append('1')

    key_encrypted = ''.join(encrypted)

    with open(file_to_encrypt, 'w') as file_key:
        file_key.write(key_encrypted)

    return key_encrypted


def encrypt_to_binary(file_original, file_binary, key):
    list = []
    for i in range(0, len(file_binary), 8):
        list.append(file_binary[i:i + 8])

    descrypted = []

    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == key[j]:
                descrypted.append('0')
            else:
                descrypted.append('1')

    key_encrypted = ''.join(descrypted)


    with open(f'{file_original}', 'w') as file_key:
        file_key.write(key_encrypted)

    return key_encrypted


def binary_to_txt(file_original, binary):
    text = ''

    for i in range(0, len(binary), 8):
        block = binary[i:i + 8]
        letter = chr(int(block, 2))
        text += letter

    with open(f'{file_original}', 'w', encoding='utf-8') as file:
        file.write(text)


def encrypt_txt(file_original, key):
    binary = txt_to_binary(file_original)
    binary_to_encrypt(binary, file_original, key)
    messagebox.showinfo('Succes', 'Encrypt Successful')


def decrypt_txt(file_original, key):
    with open(file_original, 'r') as file:
        encrypted_data = file.read()

    decrypted_binary = encrypt_to_binary(file_original, encrypted_data, key)
    binary_to_txt(file_original, decrypted_binary)
    messagebox.showinfo('Succes', 'Decrypt Successful')








