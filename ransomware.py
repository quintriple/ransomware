import os

def encrypt_file(filepath):
    key = b'abcdefghijklmnopqrstuvwxyz'  # encryption key
    encrypted = b''
    with open(filepath, 'rb') as file:
        data = file.read()
        for byte in data:
            encrypted += bytes([byte ^ key])  # XOR operation for encryption
        
    with open(filepath, 'wb') as file:
        file.write(encrypted)
    print(f'File {filepath} encrypted successfully.')

def decrypt_file(filepath):
    # Decryption process is the same as encryption (XOR operation)
    encrypt_file(filepath)
    print(f'File {filepath} decrypted successfully.')

def encrypt_files_in_directory(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            encrypt_file(filepath)

def decrypt_files_in_directory(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            decrypt_file(filepath)

# Usage example to encrypt files in a specific directory
directory_path = '/path/to/directory'
encrypt_files_in_directory(directory_path)

# To decrypt the files back, you can use:
# decrypt_files_in_directory(directory_path)
