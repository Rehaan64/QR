import tkinter as tk
from tkinter import messagebox
import qrcode
import os
import webbrowser

def generate_qr():
    url = url_entry.get().strip()
    base_name = name_entry.get().strip()

    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    if not base_name:
        messagebox.showerror("Error", "Please enter a file name")
        return

    folder = r"C:\Users\Rehaan\PYTHONPROJECTS\QRCC\cods"
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, f"{base_name}.png")
    counter = 1

    # prevent overwrite
    while os.path.exists(file_path):
        file_path = os.path.join(folder, f"{base_name}_{counter}.png")
        counter += 1

    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    messagebox.showinfo("Success", f"QR Code saved as:\n{file_path}")

    url_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")
root.resizable(False, False)
root.wm_iconbitmap("qricon.ico")


tk.Label(root, text="QR Code Generator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter URL").pack()
url_entry = tk.Entry(root, width=45)
url_entry.pack(pady=5)

tk.Label(root, text="Enter File Name (without .png)").pack()
name_entry = tk.Entry(root, width=45)
name_entry.pack(pady=5)

tk.Button(
    root,
    text="Generate QR Code",
    font=("Arial", 12),
    bg="black",
    fg="white",
    command=generate_qr
).pack(pady=20)

#clear/reset button defining
def clear_all():
    url_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)

tk.Button(
    root,
    text="Clear",
    font=("Arial", 11),
    bg="#e74c3c",
    fg="white",
    command=clear_all
).pack(pady=5)

tk.Label(root, text="a project by REHAAN", font=("Arial", 16, "bold")).pack(pady=10)
tk.Button(
    root, text="REHAAN",
    font=("Arial", 10, "bold"),
    bg="violet", fg="white",
    padx=10, pady=4,
    cursor="hand2",
    relief="flat",
    command=lambda: webbrowser.open("https://github.com/Rehaan64")
).pack(pady=(0, 16))

root.mainloop()