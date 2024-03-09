def write_list_to_file(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"List has been written to '{filename}' successfully.")
    except IOError:
        print(f"Error: Unable to write to file '{filename}'.")

filename = 'output.txt'
my_list = ['apple', 'banana', 'orange', 'grape']

write_list_to_file(filename, my_list)
