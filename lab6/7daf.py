def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except IOError:
        print("Error: Unable to copy file.")

source_file = 'source.txt'
destination_file = 'destination.txt'

copy_file(source_file, destination_file)
