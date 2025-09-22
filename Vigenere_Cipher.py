import tkinter as tk
from tkinter import filedialog, messagebox
import unicodedata

alphabet_27 = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
alphabet_191 = ''.join(chr(i) for i in range(32, 223))

def normalize(text, alphabet):
    text = text.upper()
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    text = ''.join(c for c in text if c in alphabet)
    return text

def vigenere_cipher(text_input, key, alphabet):
    cipher_text = ""
    n = len(alphabet)
    for i, letter in enumerate(text_input):
        if letter in alphabet:
            key_char = key[i % len(key)]
            p = alphabet.index(letter)
            k = alphabet.index(key_char)
            c = (p + k) % n
            cipher_text += alphabet[c]
        else:
            cipher_text += letter
    return cipher_text

def load_file():
    file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            text_entry.delete("1.0", tk.END)
            text_entry.insert(tk.END, f.read())

def encrypt_text():
    text = text_entry.get("1.0", tk.END).strip()
    key = key_entry.get().strip().upper()

    if not text or not key:
        messagebox.showwarning("Error", "Debe ingresar texto y clave.")
        return

    alphabet = alphabet_27 if var_alphabet.get() == 27 else alphabet_191

    text_norm = normalize(text, alphabet)
    key_norm = normalize(key, alphabet)

    if not key_norm:
        messagebox.showwarning("Error", "La clave no contiene caracteres válidos del alfabeto seleccionado.")
        return

    result = vigenere_cipher(text_norm, key_norm, alphabet)

    output_entry.delete("1.0", tk.END)
    output_entry.insert(tk.END, result)

root = tk.Tk()
root.title("Cifrado Vigenère")

tk.Label(root, text="Texto a cifrar:").grid(row=0, column=0, sticky="w")
text_entry = tk.Text(root, height=5, width=50)
text_entry.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

tk.Button(root, text="Cargar archivo", command=load_file).grid(row=2, column=0, pady=5)

tk.Label(root, text="Clave:").grid(row=3, column=0, sticky="w")
key_entry = tk.Entry(root, width=30)
key_entry.grid(row=3, column=1, pady=5, sticky="w")

var_alphabet = tk.IntVar(value=27)
tk.Radiobutton(root, text="Alfabeto 27 (A-Z + Ñ)", variable=var_alphabet, value=27).grid(row=4, column=0, sticky="w")
tk.Radiobutton(root, text="Alfabeto 191 (ASCII extendido)", variable=var_alphabet, value=191).grid(row=4, column=1, sticky="w")

tk.Button(root, text="Cifrar", command=encrypt_text).grid(row=5, column=0, columnspan=2, pady=10)

tk.Label(root, text="Texto cifrado:").grid(row=6, column=0, sticky="w")
output_entry = tk.Text(root, height=5, width=50)
output_entry.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()