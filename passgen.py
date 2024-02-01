#!/usr/bin/env python

import string
import tkinter as tk
from tkinter import simpledialog, messagebox
import secrets
import pyperclip

class PasswordGeneratorApp:
    """A simple password generator application using Tkinter."""
    def __init__(self):
        """
        Initialize the application.
        """
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window

    def get_password_options(self):
        """Allow the user to select options for generating the password. 
           Returns:dict: A dictionary with length and selected options.
        """
        options = {
            'use_uppercase': tk.BooleanVar(),
            'use_lowercase': tk.BooleanVar(),
            'use_digits': tk.BooleanVar(),
            'use_punctuation': tk.BooleanVar(),
        }

        options_window = tk.Toplevel(self.root)
        options_window.title("Password Options")

        tk.Label(options_window, text="Password Length:").pack(pady=5)
        length_entry = tk.Entry(options_window)
        length_entry.pack(pady=5, padx=10)

        tk.Checkbutton(options_window, text="Uppercase", variable=options['use_uppercase']).pack()
        tk.Checkbutton(options_window, text="Lowercase", variable=options['use_lowercase']).pack()
        tk.Checkbutton(options_window, text="Digits", variable=options['use_digits']).pack()
        tk.Checkbutton(options_window, text="Punctuation", variable=options['use_punctuation']).pack()

        def on_generate():
            options_window.result = {
                'length': int(length_entry.get()),
                'options': {key: var.get() for key, var in options.items()}
            }
            options_window.destroy()

        generate_button = tk.Button(options_window, text="Generate Password", command=on_generate)
        generate_button.pack(pady=10)

        screen_width = options_window.winfo_screenwidth()
        screen_height = options_window.winfo_screenheight()
        x_coordinate = int((screen_width - options_window.winfo_reqwidth()) / 2)
        y_coordinate = int((screen_height - options_window.winfo_reqheight()) / 2)
        options_window.geometry(f"+{x_coordinate}+{y_coordinate}")

        options_window.wait_window()

        return options_window.result

    def generate_password(self, length=12, options=None):
        """Generate a random password based on the provided options.

        Args:
            length (int): Length of the password.
            options (dict): Options to include character types 
            (uppercase, lowercase, digits, punctuation).

        Returns:
            str: Generated password."""
        characters = ""
        if options['use_uppercase']:
            characters += string.ascii_uppercase
        if options['use_lowercase']:
            characters += string.ascii_lowercase
        if options['use_digits']:
            characters += string.digits
        if options['use_punctuation']:
            characters += string.punctuation

        if not characters:
            raise ValueError("You must select at least one character set.")

        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

    def copy_to_clipboard(self, password, password_window):
        """
        Copy the password to the clipboard and show a confirmation message.

        Args:
            password (str): Password to copy.
            password_window (tk.Toplevel): Window containing the generated password.
        """
        pyperclip.copy(password)
        messagebox.showinfo("Copied to Clipboard", "Password copied to clipboard!")
        password_window.destroy()  # Close the window after copying

    def generate_password_and_show(self):
        """
        Generate a password and show the graphical user interface.
        """
        options = self.get_password_options()

        if options['length'] is not None:
            password = self.generate_password(options['length'], options['options'])

            password_window = tk.Toplevel(self.root)
            password_window.title("Generated Password")

            password_label = tk.Label(password_window, text=f"Your password is:\n{password}")
            password_label.pack(padx=20, pady=20)

            copy_button = tk.Button(password_window, text="Copy", command=lambda: self.copy_to_clipboard(password, password_window))
            copy_button.pack(pady=10)

            screen_width = password_window.winfo_screenwidth()
            screen_height = password_window.winfo_screenheight()
            x_coordinate = int((screen_width - password_window.winfo_reqwidth()) / 2)
            y_coordinate = int((screen_height - password_window.winfo_reqheight()) / 2)
            password_window.geometry(f"+{x_coordinate}+{y_coordinate}")

    def run(self):
        """
        Run the main loop of the application.
        """
        self.root.deiconify()  # Show the main window
        self.root.withdraw()  # Hide the main window again
        self.generate_password_and_show()
        self.root.mainloop()

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.run()
