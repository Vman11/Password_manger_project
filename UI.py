import tkinter as tk
from tkinter import filedialog,simpledialog, messagebox
import hashlib
import os
import cv2
import numpy as np
import random
import image_hash
import pyperclip

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Menu")
        
        self.label = tk.Label(master, text="Main Menu", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.choose_file_button = tk.Button(master, text="New Password", command=self.choose_file)
        self.choose_file_button.pack(pady=5)

        self.button1 = tk.Button(master, text="CHECK IMAGE", command=self.open_ui1)
        self.button1.pack(pady=5)


        self.quit_button = tk.Button(master, text="Quit", command=self.quit_program)
        self.quit_button.pack(pady=5)
    
    
    def get_input_label(self):
        label = simpledialog.askstring("Input Label", "Please enter a label for the selected file:")
        return label

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("File Selected", f"You selected: {file_path}")
            changed_image = image_hash.random_change_image(file_path)
            label = self.get_input_label()
            print(label)
            if label == None or label == '':
                messagebox.showinfo("ERROR","ERROR PLEASE ADD A NAME: IMAGE IGNORED")
            else:
                image_hash.move_file(file_path,'D:\Password Manager Project\Original_Image\\'+str(label)+'.png')
                cv2.imwrite('Secure_Images\\'+str(label)+'.png', changed_image)
                messagebox.showinfo("Success!","Image Added!")



    def open_ui1(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            last_backslash_index = file_path.rfind('/')
            print()
            for file_name in os.listdir("Secure_Images/"):
                print(file_name)
                print(file_path[last_backslash_index+1:])
                if file_name ==file_path[last_backslash_index+1:]:
                     with open("D:\\Password Manager Project\\Secure_Images\\"+str(file_name),"rb") as f:
                        bytes = f.read() # read entire file as bytes
                        readable_hash = hashlib.sha256(bytes).hexdigest()
                        messagebox.showinfo("Success!","Password Added to clipboard!")
                        pyperclip.copy(readable_hash)


    def quit_program(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.master.destroy()

class UI1:
    def __init__(self, master):
        self.master = master
        self.master.title("UI 1")

        self.label = tk.Label(master, text="This is UI 1", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.back_button = tk.Button(master, text="Back to Main Menu", command=self.back_to_main_menu)
        self.back_button.pack(pady=5)

    def back_to_main_menu(self):
        self.master.destroy()
        root.deiconify()  # Restore main menu

class UI2:
    def __init__(self, master):
        self.master = master
        self.master.title("UI 2")

        self.label = tk.Label(master, text="This is UI 2", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.back_button = tk.Button(master, text="Back to Main Menu", command=self.back_to_main_menu)
        self.back_button.pack(pady=5)

    def back_to_main_menu(self):
        self.master.destroy()
        root.deiconify()  # Restore main menu

if __name__ == "__main__":
    root = tk.Tk()
    lbl = tk.Label(root, text = "") 
    lbl.pack() 
    main_menu = MainMenu(root)
    root.mainloop()
