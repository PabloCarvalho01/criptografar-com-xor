import tkinter as tk
from tkinter import font, messagebox
from Pablo.criptograf.encrypt_xor import encrypt_txt, decrypt_txt
from Pablo.criptograf.encrypt_image import encrypt_image, decrypt_image


def check_file_encrypt():
    path_file = entry_file_name.get()

    if path_file.endswith('.txt'):
        encrypt_txt(entry_file_name.get(), entry_key.get())
    elif path_file.endswith('.jpg'):
        encrypt_image(entry_file_name.get(), entry_key.get())
    else:
        messagebox.showinfo('Error', 'Unsupported file type')


def check_file_decrypt():
    path_file = entry_file_name.get()

    if path_file.endswith('.txt'):
        decrypt_txt(entry_file_name.get(), entry_key.get())
    elif path_file.endswith('.jpg'):
        decrypt_image(entry_file_name.get(), entry_key.get())
    else:
        messagebox.showinfo('Error', 'Unsupported file type')


window = tk.Tk()
window.title("Criptografia")
window.geometry("500x250")
window.configure(bg="#888888")

font = font.Font(family="Arial", size=12, weight="bold")


entry_file_name = tk.Entry(window, font=font, justify="center", width=20)
entry_file_name.insert(0, "EXEMPLE.TXT")
entry_file_name.place(x=50, y=50, width=200, height=40)


entry_key = tk.Entry(window, font=font, justify="center", width=20)
entry_key.insert(0, "01000101")
entry_key.place(x=50, y=120, width=200, height=40)


buttom_encrypt = tk.Button(window, text="ENCRYPT", font=font, bg="#FF5555", fg="black",bd=0, command= lambda: check_file_encrypt())
buttom_encrypt.place(x=300, y=50, width=150, height=40)
buttom_encrypt.config(highlightbackground="#FF5555")



buttom_decrypt = tk.Button(window, text="DECRYPT", font=font, bg="#B4FF8A", fg="black",bd=0, command=lambda: check_file_decrypt())
buttom_decrypt.place(x=300, y=120, width=150, height=40)
buttom_decrypt.config(highlightbackground="#B4FF8A")




window.mainloop()