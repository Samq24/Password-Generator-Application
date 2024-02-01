# Password Generator Application

This password generator script, is built using Python and the Tkinter library. It provides a simple and user-friendly interface for generating strong and secure passwords with customizable options.

## Key Features

### 1. User-Friendly Interface

The application is designed with a graphical user interface using Tkinter, making it accessible and easy to use.

### 2. Customizable Options

Users can customize the generated password by selecting options such as length, uppercase letters, lowercase letters, digits, and punctuation. This flexibility allows for tailored password generation.

### 3. Secure Password Generation

The script utilizes Python's `secrets` module to generate secure and random passwords. This ensures that the generated passwords are suitable for cryptographic use.

### 4. Clipboard Integration

The application includes a feature to copy the generated password to the clipboard. This functionality enhances user convenience by eliminating the need to manually select and copy the password.

## Code

### Password Options

The `get_password_options` method allows users to interactively choose options for generating the password. It includes options for password length and character sets (uppercase, lowercase, digits, punctuation).

### Password Generation

The `generate_password` method creates a random password based on the selected options. It concatenates character sets based on user preferences and uses the `secrets` module for secure randomness.

### Clipboard Integration

The `copy_to_clipboard` method copies the generated password to the clipboard using the `pyperclip` library. A confirmation message is displayed to notify the user of the successful copy.

## How to Use

1. Run the script.
2. Customize password options such as length, uppercase, lowercase, digits, and punctuation.
3. Click the "Generate Password" button.
4. The generated password is displayed in a new window.
5. Click the "Copy" button to copy the password to the clipboard.

## Dependencies

- Python 3.x
- Tkinter library
