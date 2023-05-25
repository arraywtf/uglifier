import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import random

def uglify_html_file(file_path):
    with open(file_path, 'r') as file:
        html_code = file.read()

    ugly_code = uglify_html(html_code)

    duplicate_file_path = file_path.replace('.html', '_uglified.html')
    with open(duplicate_file_path, 'w') as duplicate_file:
        duplicate_file.write(ugly_code)

    print("Uglification complete. Duplicate file created:", duplicate_file_path)

def uglify_html(html_code):
    ugly_code = ""
    indentation_level = 0
    indent_char = "\t"

    for line in html_code.split('\n'):
        stripped_line = line.strip()

        if stripped_line.startswith("</"):
            indentation_level -= 1

        ugly_line = indent_char * indentation_level + stripped_line
        ugly_code += ugly_line + "\n"

        if stripped_line.startswith("<"):
            indentation_level += 1

    return ugly_code

def select_html_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
    if file_path:
        uglify_html_file(file_path)

window = ctk.CTk()
window.title("HTML Uglifier")
window.geometry("500x260")
window.resizable(False, False)
window.iconbitmap("icon.ico")

bg_color = "#d9d9d9"

window.configure(background=bg_color)
ctk.set_default_color_theme("green")

title_label = ctk.CTkLabel(window, text="HTML Uglifier", font=ctk.CTkFont("Arial", 24))
title_label.pack(pady=20)

title_label = ctk.CTkLabel(window, text="Still in development. \nEver wanted to make your code ugly? Well Uglifier is your solution.", font=ctk.CTkFont("Arial", 14))
title_label.pack(pady=20)


select_button = ctk.CTkButton(window, text="Select HTML File", font=ctk.CTkFont("Satoshi", 14),command=select_html_file)
select_button.pack(pady=10)

title_label = ctk.CTkLabel(window, text="developed by array", font=ctk.CTkFont("Arial", 10, "bold"))
title_label.pack(side=ctk.BOTTOM)

window.mainloop()