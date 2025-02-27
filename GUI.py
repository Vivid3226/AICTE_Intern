import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import os

# Global variables
theme_color = "#2C3E50"
button_color = "#FF5733"
hover_color = "#C70039"
text_color = "#FFFFFF"
background_image_path = "C:/Users/jadiy/OneDrive/Desktop/AICTE/project_supportfiles-main/Encrypted.jpg"  # Update this path if needed

def on_enter(e):
    e.widget.config(bg=hover_color)

def on_leave(e):
    e.widget.config(bg=button_color)

def load_image():
    global selected_image
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        image_label.config(text=file_path)
        selected_image = file_path

def encrypt_message():
    if not selected_image:
        messagebox.showerror("Error", "Please select an image first!")
        return
    
    msg = enc_message_entry.get()
    password = enc_password_entry.get()
    
    img = cv2.imread(selected_image)
    msg += chr(255)  # Add a delimiter to mark the end of the message

    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = ord(char)  # Convert char to ASCII value
        z += 1
        if z == 3:
            z = 0
            m += 1
        if m == img.shape[1]:
            m = 0
            n += 1
        if n == img.shape[0]:
            messagebox.showerror("Error", "Message too long for this image!")
            return

    encrypted_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_path, img)
    os.system(f"start {encrypted_path}")
    messagebox.showinfo("Success", "Message encrypted successfully!")

def decrypt_message():
    if not selected_image:
        messagebox.showerror("Error", "Please select an image first!")
        return

    img = cv2.imread(selected_image)
    message = ""

    n, m, z = 0, 0, 0
    while True:
        char_code = img[n, m, z]
        if char_code == 255:  # Stop reading at delimiter
            break
        message += chr(char_code)

        z += 1
        if z == 3:
            z = 0
            m += 1
        if m == img.shape[1]:
            m = 0
            n += 1
        if n == img.shape[0]:
            break

    # Display decrypted message in read-only text box
    dec_message_entry.config(state="normal")
    dec_message_entry.delete("1.0", tk.END)
    dec_message_entry.insert(tk.END, message)
    dec_message_entry.config(state="disabled")

    messagebox.showinfo("Decryption Successful", "Message decrypted successfully!")

def set_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg="gray", font=("Arial", 10, "italic"))
    entry.bind("<FocusIn>", lambda event: clear_placeholder(event, placeholder))
    entry.bind("<FocusOut>", lambda event: restore_placeholder(event, placeholder))

def clear_placeholder(event, placeholder):
    if event.widget.get() == placeholder:
        event.widget.delete(0, tk.END)
        event.widget.config(fg="black", font=("Arial", 10, "normal"))

def restore_placeholder(event, placeholder):
    if event.widget.get() == "":
        event.widget.insert(0, placeholder)
        event.widget.config(fg="gray", font=("Arial", 10, "italic"))

# Root window
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("600x600")

# Load background image
bg_image = Image.open(background_image_path)
bg_image = bg_image.resize((600, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Title Label
title_label = tk.Label(root, text="Image Steganography", font=("Arial", 18, "bold"), fg=text_color, bg=theme_color)
title_label.pack(pady=10)

# Image Selection Button
btn_select = tk.Button(root, text="Load Image", bg=button_color, fg=text_color, font=("Arial", 12, "bold"), command=load_image)
btn_select.pack(pady=5)
btn_select.bind("<Enter>", on_enter)
btn_select.bind("<Leave>", on_leave)

image_label = tk.Label(root, text="No Image Selected", fg=text_color, bg=theme_color)
image_label.pack()

# Encryption Section
tk.Label(root, text="Secret Message:", fg=text_color, bg=theme_color).pack(pady=5)
enc_message_entry = tk.Entry(root, width=40)
set_placeholder(enc_message_entry, "Enter secret message")
enc_message_entry.pack(pady=5)

tk.Label(root, text="Passcode:", fg=text_color, bg=theme_color).pack(pady=5)
enc_password_entry = tk.Entry(root, width=40, show="*")
set_placeholder(enc_password_entry, "Enter encryption password")
enc_password_entry.pack(pady=5)

btn_encrypt = tk.Button(root, text="Encrypt", bg=button_color, fg=text_color, font=("Arial", 12, "bold"), command=encrypt_message)
btn_encrypt.pack(pady=5)
btn_encrypt.bind("<Enter>", on_enter)
btn_encrypt.bind("<Leave>", on_leave)

# Decryption Section
tk.Label(root, text="Decryption Passcode:", fg=text_color, bg=theme_color).pack(pady=5)
dec_password_entry = tk.Entry(root, width=40, show="*")
set_placeholder(dec_password_entry, "Enter decryption password")
dec_password_entry.pack(pady=5)

tk.Label(root, text="Decrypted Message:", fg=text_color, bg=theme_color).pack(pady=5)
dec_message_entry = tk.Text(root, width=50, height=5, state="disabled")
dec_message_entry.pack(pady=5)

btn_decrypt = tk.Button(root, text="Decrypt", bg=button_color, fg=text_color, font=("Arial", 12, "bold"), command=decrypt_message)
btn_decrypt.pack(pady=5)
btn_decrypt.bind("<Enter>", on_enter)
btn_decrypt.bind("<Leave>", on_leave)

# Footer Label
tk.Label(root, text="Done by Om Jadiya", fg="silver", bg=theme_color, font=("Arial", 10, "bold")).pack(side="bottom", pady=10)

root.mainloop()
