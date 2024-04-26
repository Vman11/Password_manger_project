import tkinter as tk
from tkinter import filedialog,simpledialog, messagebox
import hashlib
import os
import cv2
import numpy as np
import random
import image_hash
import pyperclip
from pathlib import Path
import decode as decode
import code as encode
import sys


class MainMenu:
    def __init__(self, master,OG_path,S_path):
        self.master = master
        self.master.title("PIC PASS")
        self.OG_path= OG_path
        self.S_path = S_path
        self.pwd =  simpledialog.askstring("Password", "Please enter a Password to encrypt/decrypt files:")


        
        self.label = tk.Label(master, text="PIC PASS", font=("Helvetica", 16))
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

        HIT = 0
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("File Selected", f"You selected: {file_path}")
            if (decode.decode(self.pwd,self.OG_path) == -1):
                messagebox.showinfo("ERROR","INCORRECT PASSWORD TERMINATING PROGRAM")
                sys.exit(1)

            if (decode.decode(self.pwd,self.S_path) == -1):
                messagebox.showinfo("ERROR","INCORRECT PASSWORD TERMINATING PROGRAM")
                sys.exit(1)
            changed_image = image_hash.random_change_image(file_path)
            label = self.get_input_label()
            image = cv2.imread(file_path)
            for file_name in os.listdir(self.OG_path):
                current_image = cv2.imread(self.OG_path+'/'+file_name)
                if image.shape == current_image.shape and not(np.bitwise_xor(image,current_image).any()):

                    HIT =1

            if label == None or label == '' or HIT ==1:
                if(encode.encode(self.pwd,self.OG_path) == -1):
                    messagebox.showinfo("ERROR","INCORRECT PASSWORD TERMINATING PROGRAM")
                    sys.exit(1)

                if (encode.encode(self.pwd,self.S_path) == -1):
                    messagebox.showinfo("ERROR","INCORRECT PASSWORD TERMINATING PROGRAM")
                    sys.exit(1)
                if HIT == 1:
                    messagebox.showinfo("ERROR","IMAGE ALREADY USED")
                else:
                    messagebox.showinfo("ERROR","ERROR PLEASE ADD A NAME: IMAGE IGNORED")
            else:
                image_hash.move_file(file_path,self.OG_path+r'/'+str(label)+'.png')
                cv2.imwrite(self.S_path+r'/'+hashlib.sha256(label.encode('utf-8')).hexdigest()+'.png', changed_image)
                print(hashlib.sha256(label.encode('utf-8')).hexdigest())
                if(encode.encode(self.pwd,self.OG_path) == -1):
                    messagebox.showinfo("ERROR","INCORRECT PASSWORD TERMINATING PROGRAM")
                    sys.exit(1)

                if (encode.encode(self.pwd,self.S_path) == -1):
                    messagebox.showinfo("ERROR","INCORRECT PASSWORD TERMINATING PROGRAM")
                    sys.exit(1)
                messagebox.showinfo("Success!","Image Added!")





    def open_ui1(self):

        file_path = filedialog.askopenfilename()
        if file_path:
            last_backslash_index = file_path.rfind('/')
            if (decode.decode(self.pwd,self.OG_path) == -1):
                messagebox.showinfo("ERROR","INCORRECT PASSWORD TERMINATING PROGRAM")
                sys.exit(1)

            if (decode.decode(self.pwd,self.S_path) == -1):
                messagebox.showinfo("ERROR","INCORRECT PASSWORD TERMINATING PROGRAM")
                sys.exit(1)
            image = cv2.imread(file_path)
            for file_name in os.listdir(self.OG_path):
                current_image = cv2.imread(self.OG_path+'/'+file_name)
                if image.shape == current_image.shape and not(np.bitwise_xor(image,current_image).any()):
                    last_backslash_index = file_name.rfind('.')
                    result = hashlib.sha256(file_name[:last_backslash_index].encode('utf-8')).hexdigest()
                    with open(self.S_path+r'/'+hashlib.sha256(file_name[:last_backslash_index].encode('utf-8')).hexdigest()+'.png',"rb") as f:
                        bytes = f.read() # read entire file as bytes
                        readable_hash = hashlib.sha256(bytes).hexdigest()
                        if(encode.encode(self.pwd,self.OG_path) == -1):
                            messagebox.showinfo("ERROR","INCORRECT PASSWORD TERMINATING PROGRAM")
                            sys.exit(1)

                        if (encode.encode(self.pwd,self.S_path) == -1):
                            messagebox.showinfo("ERROR","INCORRECT PASSWORD TERMINATING PROGRAM")
                            sys.exit(1)
                        messagebox.showinfo("Success!","Password Added to clipboard!")
                        pyperclip.copy(readable_hash)
                else:
                    if(encode.encode(self.pwd,self.OG_path) == -1):
                        messagebox.showinfo("ERROR","INCORRECT PASSWORD TERMINATING PROGRAM")
                        sys.exit(1)

                    if (encode.encode(self.pwd,self.S_path) == -1):
                        messagebox.showinfo("ERROR","INCORRECT PASSWORD TERMINATING PROGRAM")
                        sys.exit(1)
 
                    messagebox.showinfo("Error!","Image not found...")



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
    home_dir = Path.home()
    print(home_dir)
    OG_path =os.path.join(home_dir,'Orginal_images')
    if not os.path.exists(OG_path):
        os.makedirs(OG_path)
    
    S_path =os.path.join(home_dir,'Secure_images')
    if not os.path.exists(S_path):
        os.makedirs(S_path)

    root = tk.Tk()
    lbl = tk.Label(root, text = "") 
    lbl.pack() 
    main_menu = MainMenu(root,OG_path,S_path,)
    root.mainloop()
