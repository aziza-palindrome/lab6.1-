import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}.")

generate_files()
