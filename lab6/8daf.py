import os

def check_access_and_delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.R_OK | os.W_OK):
            try:
                os.remove(path)
                print(f"File '{path}' deleted successfully.")
            except OSError as e:
                print(f"Error: {e.strerror}")
        else:
            print(f"Error: Access denied to file '{path}'.")
    else:
        print(f"Error: File '{path}' does not exist.")

file_path = "/path/to/your/file"

check_access_and_delete_file(file_path)
